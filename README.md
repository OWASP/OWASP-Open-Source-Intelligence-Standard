# OOVS — public site

A static, three-page site introducing the OWASP OSINT Verification Standard to
non-technical audiences: government and defence evaluators, oversight and legal
readers, industry, journalism, and civil society.

It deliberately does not duplicate the repository or the OWASP project page. No
code, no command lines, no schema discussion.

## Design constraints

- Pure black and white only. No gradients, no shadows, no accent colours.
- System fonts only, so nothing is fetched from a third-party CDN. The site
  loads on locked-down government networks and works offline once cached.
- No frameworks, no build step, no dependencies. Three HTML files, one
  stylesheet, one small script.
- Total transferred weight is a few tens of kilobytes.

## Accessibility

- Black on white is a 21:1 contrast ratio, far above the 4.5:1 minimum.
- All type is set in relative units with fluid scaling, so browser and OS text
  sizing work.
- Navigation targets are at least 44px tall.
- Skip link, semantic landmarks, `aria-current` on the active nav item, and
  visible focus rings.
- Animation is suppressed entirely under `prefers-reduced-motion`.
- Dark appearance is supported by inverting to white-on-black. To force the
  light appearance everywhere, delete the `prefers-color-scheme` block near the
  end of `assets/css/site.css`.
- A print stylesheet renders link targets, since this audience prints.

## Structure

```
index.html          The argument: problem, what it does, failure modes,
                    self-verification, doctrine, audience, scope, status
requirements.html   The ten requirements in plain language, plus the
                    assessment model and rejected alternatives
adoption.html       Adoption ladder, evaluator checklist, pilot pattern
assets/css/site.css The whole design system
assets/js/site.js   Scroll reveal only; the site is complete without it
assets/img/mark.svg Monochrome mark: many mentions resolving to one origin
```

## Publish on GitHub Pages

### Option A — your own repository (recommended)

Best for a portfolio: the URL is yours, and it does not put promotional content
in an OWASP organisation repository.

```sh
cd oovs-site
git init -b main
git add .
git commit -m "Add OOVS public site"
git remote add origin git@github.com:<your-user>/oovs.git
git push -u origin main
```

Then: **Settings → Pages → Source: Deploy from a branch → `main` / `root` → Save.**

Live at `https://<your-user>.github.io/oovs/` within a minute or two.

Use `<your-user>.github.io` as the repository name instead if you want it at the
root of your GitHub domain.

### Option B — the OWASP project repository

Copy these files into a `docs/` folder on the OWASP repository and enable Pages
from `main` / `docs`. Live at
`https://owasp.github.io/OWASP-Open-Source-Intelligence-Standard/`.

This needs repository admin rights, and OWASP staff have said Pages sites will
have to migrate to the new CMS later. Option A avoids both problems.

All internal links are relative, so the site works from a subdirectory without
changes.

## Keeping it accurate

Every number on the site is verifiable from the released standard: ten
requirements, ten acceptance tests, eight automated check families, and
twenty-three fingerprinted files per release. If a release changes those, update
the `.stats` block in `index.html`.

Deliberate omissions, which should stay omitted until they are true: adoption
claims, endorsement claims, certification language, and named external
reviewers.
