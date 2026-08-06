#!/usr/bin/env python3
"""Validate OOVS/OOSIS schemas, examples, semantics, fixtures, links, and manifest."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Callable
from urllib.parse import unquote, urlsplit

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError
except ModuleNotFoundError:  # pragma: no cover - exercised by a clean machine, not CI
    print(
        "Validation dependency missing. Run: "
        "python3 -m pip install -r requirements-validation.txt",
        file=sys.stderr,
    )
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
OOVS_DIR = ROOT / "oovs" / "v0.1"
FIXTURE_MANIFEST = ROOT / "tests" / "fixtures" / "manifest.json"
RELEASE_MANIFEST = ROOT / "releases" / "v0.1.0" / "manifest.json"
RELEASE_MANIFEST_SCHEMA = ROOT / "releases" / "manifest.schema.json"
IGNORED_MARKDOWN = {Path("docs/08-founding-meeting-agenda.md")}
SKIP_DIRS = {".git", ".venv", "venv", "build", "dist", "site"}


class ValidationFailure(ValueError):
    """A deterministic validation failure suitable for an expected-negative fixture."""


def relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationFailure(f"{relative(path)}: file not found") from exc
    except json.JSONDecodeError as exc:
        raise ValidationFailure(
            f"{relative(path)}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def require_object(document: Any, path: Path) -> dict[str, Any]:
    if not isinstance(document, dict):
        raise ValidationFailure(f"{relative(path)}: root must be an object")
    return document


def error_path(parts: Any) -> str:
    rendered = "$"
    for part in parts:
        rendered += f"[{part}]" if isinstance(part, int) else f".{part}"
    return rendered


def validate_schema_file(schema_path: Path) -> dict[str, Any]:
    schema = require_object(load_json(schema_path), schema_path)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise ValidationFailure(
            f"{relative(schema_path)}: invalid Draft 2020-12 schema: {exc.message}"
        ) from exc
    return schema


def validate_instance(instance_path: Path, schema_path: Path) -> dict[str, Any]:
    schema = validate_schema_file(schema_path)
    instance = require_object(load_json(instance_path), instance_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(instance),
        key=lambda item: tuple(str(part) for part in item.absolute_path),
    )
    if errors:
        details = "; ".join(
            f"{error_path(error.absolute_path)}: {error.message}" for error in errors
        )
        raise ValidationFailure(
            f"{relative(instance_path)}: JSON Schema validation failed against "
            f"{relative(schema_path)}: {details}"
        )
    return instance


def canonical_requirements() -> list[dict[str, Any]]:
    document = require_object(load_json(OOVS_DIR / "requirements.json"), OOVS_DIR / "requirements.json")
    requirements = document.get("requirements")
    if not isinstance(requirements, list):
        raise ValidationFailure("oovs/v0.1/requirements.json: requirements must be an array")
    return [item for item in requirements if isinstance(item, dict)]


def canonical_requirement_ids() -> set[str]:
    return {str(item.get("id")) for item in canonical_requirements()}


def semantic_oig(document: dict[str, Any], path: Path, *, require_full: bool = True) -> None:
    nodes = document.get("nodes")
    relationships = document.get("relationships")
    if not isinstance(nodes, list) or not isinstance(relationships, list):
        raise ValidationFailure(f"{relative(path)}: nodes and relationships must be arrays")

    node_ids = [node.get("id") for node in nodes if isinstance(node, dict)]
    if len(node_ids) != len(nodes) or len(set(node_ids)) != len(node_ids):
        raise ValidationFailure(f"{relative(path)}: nodes require unique IDs")

    relationship_ids = [item.get("id") for item in relationships if isinstance(item, dict)]
    if len(relationship_ids) != len(relationships) or len(set(relationship_ids)) != len(relationship_ids):
        raise ValidationFailure(f"{relative(path)}: relationships require unique IDs")

    known = set(node_ids)
    for relationship in relationships:
        if not isinstance(relationship, dict):
            raise ValidationFailure(f"{relative(path)}: relationship must be an object")
        for key in ("source_ref", "target_ref"):
            if relationship.get(key) not in known:
                raise ValidationFailure(
                    f"{relative(path)}: relationship {relationship.get('id')} references "
                    f"unknown node {relationship.get(key)}"
                )
        for evidence_ref in relationship.get("evidence_refs", []):
            if evidence_ref not in known:
                raise ValidationFailure(
                    f"{relative(path)}: relationship {relationship.get('id')} references "
                    f"unknown evidence node {evidence_ref}"
                )


def semantic_ottm(document: dict[str, Any], path: Path, *, require_full: bool = True) -> None:
    record_id = document.get("id")
    if not isinstance(record_id, str) or not re.fullmatch(r"OTTM-[A-Z]+-[0-9]{3}", record_id):
        raise ValidationFailure(f"{relative(path)}: invalid OTTM identifier")
    if path.parent.name == "examples" and path.stem != record_id:
        raise ValidationFailure(
            f"{relative(path)}: filename must match record ID {record_id}"
        )
    reliability = document.get("reliability")
    if not isinstance(reliability, dict):
        raise ValidationFailure(f"{relative(path)}: reliability record is required")


def semantic_requirements(
    document: dict[str, Any], path: Path, *, require_full: bool = True
) -> None:
    items = document.get("requirements")
    if not isinstance(items, list):
        raise ValidationFailure(f"{relative(path)}: requirements must be an array")
    if require_full and len(items) != 10:
        raise ValidationFailure(f"{relative(path)}: exactly 10 requirements are required")

    ids: list[str] = []
    ordinals: list[int] = []
    test_refs: list[str] = []
    for item in items:
        if not isinstance(item, dict):
            raise ValidationFailure(f"{relative(path)}: each requirement must be an object")
        requirement_id = str(item.get("id"))
        ids.append(requirement_id)
        ordinal = item.get("ordinal")
        if isinstance(ordinal, int):
            ordinals.append(ordinal)
        expected_id = f"OOVS-v0.1.0-{ordinal:02d}" if isinstance(ordinal, int) else ""
        if requirement_id != expected_id:
            raise ValidationFailure(
                f"{relative(path)}: requirement ID {requirement_id} does not match ordinal {ordinal}"
            )
        statement = item.get("normative_statement")
        if not isinstance(statement, str) or "MUST" not in statement:
            raise ValidationFailure(
                f"{relative(path)}: {requirement_id} needs a normative MUST/MUST NOT statement"
            )
        applicability = item.get("applicability")
        if isinstance(applicability, dict) and applicability.get("mode") == "conditional":
            if not applicability.get("not_applicable_when"):
                raise ValidationFailure(
                    f"{relative(path)}: conditional {requirement_id} needs an objective not-applicable condition"
                )
        refs = item.get("test_refs", [])
        if isinstance(refs, list):
            test_refs.extend(str(value) for value in refs)

    if len(ids) != len(set(ids)):
        raise ValidationFailure(f"{relative(path)}: duplicate requirement ID")
    if require_full and ordinals != list(range(1, 11)):
        raise ValidationFailure(f"{relative(path)}: requirement ordinals must be 1 through 10 in order")
    if len(test_refs) != len(set(test_refs)):
        raise ValidationFailure(f"{relative(path)}: duplicate acceptance-test reference")


def semantic_tests(document: dict[str, Any], path: Path, *, require_full: bool = True) -> None:
    tests = document.get("tests")
    if not isinstance(tests, list):
        raise ValidationFailure(f"{relative(path)}: tests must be an array")
    if require_full and len(tests) != 10:
        raise ValidationFailure(f"{relative(path)}: exactly 10 acceptance tests are required")

    known_requirements = canonical_requirement_ids()
    test_ids: list[str] = []
    requirement_refs: list[str] = []
    for test in tests:
        if not isinstance(test, dict):
            raise ValidationFailure(f"{relative(path)}: each test must be an object")
        test_id = str(test.get("id"))
        requirement_ref = str(test.get("requirement_ref"))
        test_ids.append(test_id)
        requirement_refs.append(requirement_ref)
        if requirement_ref not in known_requirements:
            raise ValidationFailure(
                f"{relative(path)}: test {test_id} references unknown requirement {requirement_ref}"
            )
        ordinal = requirement_ref.rsplit("-", 1)[-1]
        expected_test_id = f"OOVS-v0.1.0-T{ordinal}"
        if test_id != expected_test_id:
            raise ValidationFailure(
                f"{relative(path)}: test {test_id} must be {expected_test_id} for {requirement_ref}"
            )

    if len(test_ids) != len(set(test_ids)):
        raise ValidationFailure(f"{relative(path)}: duplicate test ID")
    if len(requirement_refs) != len(set(requirement_refs)):
        raise ValidationFailure(f"{relative(path)}: more than one primary test maps to a requirement")
    if require_full and set(requirement_refs) != known_requirements:
        missing = sorted(known_requirements.difference(requirement_refs))
        raise ValidationFailure(f"{relative(path)}: tests do not cover requirements: {missing}")


def semantic_assessment(
    document: dict[str, Any], path: Path, *, require_full: bool = True
) -> None:
    results = document.get("results")
    if not isinstance(results, list):
        raise ValidationFailure(f"{relative(path)}: results must be an array")

    requirements_by_id = {str(item["id"]): item for item in canonical_requirements()}
    refs = [str(item.get("requirement_ref")) for item in results if isinstance(item, dict)]
    if len(refs) != len(results) or len(refs) != len(set(refs)):
        raise ValidationFailure(f"{relative(path)}: assessment results require unique requirement references")
    unknown = sorted(set(refs).difference(requirements_by_id))
    if unknown:
        raise ValidationFailure(f"{relative(path)}: assessment references unknown requirements: {unknown}")
    if require_full and set(refs) != set(requirements_by_id):
        missing = sorted(set(requirements_by_id).difference(refs))
        raise ValidationFailure(f"{relative(path)}: assessment omits requirements: {missing}")

    for result in results:
        if not isinstance(result, dict):
            continue
        requirement_ref = str(result.get("requirement_ref"))
        status = result.get("status")
        if status == "not_applicable":
            mode = requirements_by_id[requirement_ref].get("applicability", {}).get("mode")
            if mode != "conditional":
                raise ValidationFailure(
                    f"{relative(path)}: always-applicable {requirement_ref} cannot be not_applicable"
                )
        if status == "implemented" and not result.get("evidence_refs"):
            raise ValidationFailure(
                f"{relative(path)}: implemented {requirement_ref} needs an evidence reference"
            )

    expected_overall = (
        "meets_all_applicable"
        if all(
            isinstance(item, dict)
            and item.get("status") in {"implemented", "not_applicable"}
            for item in results
        )
        else "does_not_meet"
    )
    if document.get("overall_result") != expected_overall:
        raise ValidationFailure(
            f"{relative(path)}: overall_result must be {expected_overall} for recorded statuses"
        )

    target = document.get("target", {})
    period = target.get("period", {}) if isinstance(target, dict) else {}
    if period.get("start") and period.get("end") and period["start"] > period["end"]:
        raise ValidationFailure(f"{relative(path)}: assessment period start is after end")
    if document.get("assessed_at") and document.get("next_review_at"):
        if document["assessed_at"] > document["next_review_at"]:
            raise ValidationFailure(f"{relative(path)}: next review is before assessment date")


def normalize_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    return " ".join(text.split()).casefold()


def validate_markdown_parity() -> int:
    requirements = canonical_requirements()
    markdown_path = OOVS_DIR / "standard.md"
    markdown = markdown_path.read_text(encoding="utf-8")
    pattern = re.compile(r"^### (OOVS-v0\.1\.0-[0-9]{2}) — (.+)$", re.MULTILINE)
    matches = list(pattern.finditer(markdown))
    headings = [(match.group(1), match.group(2).strip()) for match in matches]
    expected = [(str(item["id"]), str(item["title"])) for item in requirements]
    if headings != expected:
        raise ValidationFailure(
            f"{relative(markdown_path)}: requirement headings do not match requirements.json"
        )

    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        section = normalize_markdown(markdown[match.start():end])
        requirement = requirements[index]
        for field in ("objective", "normative_statement"):
            expected_text = normalize_markdown(str(requirement[field]))
            if expected_text not in section:
                raise ValidationFailure(
                    f"{relative(markdown_path)}: {requirement['id']} {field} differs from requirements.json"
                )
    return len(requirements)


SemanticValidator = Callable[[dict[str, Any], Path], None]


def run_semantic(name: str, document: dict[str, Any], path: Path) -> None:
    validators: dict[str, SemanticValidator] = {
        "oig": lambda doc, target: semantic_oig(doc, target),
        "ottm": lambda doc, target: semantic_ottm(doc, target),
        "oovs_requirements": lambda doc, target: semantic_requirements(doc, target),
        "oovs_requirements_partial": lambda doc, target: semantic_requirements(
            doc, target, require_full=False
        ),
        "oovs_tests": lambda doc, target: semantic_tests(doc, target),
        "oovs_tests_partial": lambda doc, target: semantic_tests(
            doc, target, require_full=False
        ),
        "oovs_assessment": lambda doc, target: semantic_assessment(doc, target),
    }
    try:
        validator = validators[name]
    except KeyError as exc:
        raise ValidationFailure(f"{relative(path)}: unknown semantic validator {name}") from exc
    validator(document, path)


def validate_fixtures() -> tuple[int, int]:
    manifest = require_object(load_json(FIXTURE_MANIFEST), FIXTURE_MANIFEST)
    positive = manifest.get("positive")
    negative = manifest.get("negative")
    if not isinstance(positive, list) or not isinstance(negative, list):
        raise ValidationFailure(f"{relative(FIXTURE_MANIFEST)}: positive/negative must be arrays")

    for entry in positive:
        if not isinstance(entry, dict):
            raise ValidationFailure(f"{relative(FIXTURE_MANIFEST)}: fixture entry must be an object")
        instance_path = ROOT / str(entry["instance"])
        schema_path = ROOT / str(entry["schema"])
        document = validate_instance(instance_path, schema_path)
        run_semantic(str(entry["semantic"]), document, instance_path)

    for entry in negative:
        if not isinstance(entry, dict):
            raise ValidationFailure(f"{relative(FIXTURE_MANIFEST)}: fixture entry must be an object")
        instance_path = ROOT / str(entry["instance"])
        schema_path = ROOT / str(entry["schema"])
        try:
            document = validate_instance(instance_path, schema_path)
            run_semantic(str(entry["semantic"]), document, instance_path)
        except ValidationFailure as exc:
            expected = str(entry.get("expected_error", "")).lower()
            if expected and expected not in str(exc).lower():
                raise ValidationFailure(
                    f"{relative(instance_path)}: failed as expected, but error did not contain "
                    f"{expected!r}: {exc}"
                ) from exc
        else:
            raise ValidationFailure(
                f"{relative(instance_path)}: negative fixture unexpectedly passed"
            )

    return len(positive), len(negative)


def validate_all_schemas() -> int:
    schema_paths = sorted(
        path
        for path in ROOT.rglob("*.schema.json")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )
    for path in schema_paths:
        validate_schema_file(path)
    return len(schema_paths)


def validate_local_links() -> int:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    checked = 0
    failures: list[str] = []

    markdown_paths = sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
        and path.relative_to(ROOT) not in IGNORED_MARKDOWN
    )
    for markdown_path in markdown_paths:
        content = markdown_path.read_text(encoding="utf-8")
        for match in link_pattern.finditer(content):
            raw_target = match.group(1).strip()
            if not raw_target or raw_target.startswith("#") or raw_target.startswith("<"):
                continue
            parsed = urlsplit(raw_target)
            if parsed.scheme or parsed.netloc:
                continue
            target_text = unquote(parsed.path)
            if not target_text:
                continue
            target_path = (markdown_path.parent / target_text).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                failures.append(
                    f"{relative(markdown_path)}: link escapes repository: {raw_target}"
                )
                continue
            checked += 1
            if not target_path.exists():
                failures.append(
                    f"{relative(markdown_path)}: missing local link target {raw_target}"
                )

    if failures:
        raise ValidationFailure("local link validation failed: " + "; ".join(failures))
    return checked


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_release_manifest() -> int:
    manifest = validate_instance(RELEASE_MANIFEST, RELEASE_MANIFEST_SCHEMA)
    files = manifest.get("canonical_files")
    if not isinstance(files, list):
        raise ValidationFailure(f"{relative(RELEASE_MANIFEST)}: canonical_files must be an array")

    seen: set[str] = set()
    for entry in files:
        if not isinstance(entry, dict):
            raise ValidationFailure(f"{relative(RELEASE_MANIFEST)}: file entry must be an object")
        file_name = str(entry.get("path"))
        if file_name in seen:
            raise ValidationFailure(f"{relative(RELEASE_MANIFEST)}: duplicate path {file_name}")
        seen.add(file_name)
        target = (ROOT / file_name).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError as exc:
            raise ValidationFailure(
                f"{relative(RELEASE_MANIFEST)}: path escapes repository: {file_name}"
            ) from exc
        if not target.is_file():
            raise ValidationFailure(
                f"{relative(RELEASE_MANIFEST)}: canonical file missing: {file_name}"
            )
        actual = sha256(target)
        if entry.get("sha256") != actual:
            raise ValidationFailure(
                f"{relative(RELEASE_MANIFEST)}: hash mismatch for {file_name}; expected {actual}"
            )

    version = str(manifest.get("version"))
    if version not in str(manifest.get("release_id")):
        raise ValidationFailure(
            f"{relative(RELEASE_MANIFEST)}: release_id must contain the version {version}"
        )

    requirements_version = str(
        require_object(load_json(OOVS_DIR / "requirements.json"), OOVS_DIR / "requirements.json").get(
            "spec_version"
        )
    )
    if requirements_version != version:
        raise ValidationFailure(
            f"{relative(RELEASE_MANIFEST)}: manifest version {version} does not match "
            f"requirements spec_version {requirements_version}"
        )

    normative = {
        str(entry.get("path")) for entry in files if isinstance(entry, dict) and entry.get("role") == "normative"
    }
    if "oovs/v0.1/standard.md" not in normative:
        raise ValidationFailure(
            f"{relative(RELEASE_MANIFEST)}: the normative standard must be a canonical file"
        )
    return len(files)


def main() -> int:
    try:
        schema_count = validate_all_schemas()
        positive_count, negative_count = validate_fixtures()
        parity_count = validate_markdown_parity()
        link_count = validate_local_links()
        manifest_file_count = validate_release_manifest()
    except ValidationFailure as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1

    print(
        "Validated "
        f"{schema_count} JSON Schema(s), "
        f"{positive_count} positive fixture(s), "
        f"{negative_count} expected-failure fixture(s), "
        f"{parity_count} Markdown/JSON requirement pair(s), "
        f"{link_count} local link(s), and "
        f"{manifest_file_count} release-manifest file hash(es)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
