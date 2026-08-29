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

This is how the OWASP copy is actually published. The site lives on an orphan
`gh-pages` branch, not in `docs/`: `docs/` already holds the project's own
documentation, so serving Pages from there would drop an `index.html` on top of
it and let Jekyll process the Markdown.

```sh
git clone --depth 1 https://github.com/OWASP/OWASP-Open-Source-Intelligence-Standard.git
cd OWASP-Open-Source-Intelligence-Standard
git checkout --orphan gh-pages
git rm -r --cached .
find . -mindepth 1 -maxdepth 1 -not -name '.git' -exec rm -rf {} +
rsync -a --exclude '.git' ../oovs-site/ ./
git add -A && git commit -m "Publish the public site on gh-pages"
git push -u origin gh-pages
```

Then: **Settings → Pages → Source: Deploy from a branch → `gh-pages` / `root`.**
This keeps `main` free of website files.

The OWASP organisation has a verified Pages domain, so the canonical URL is
`https://owasp.org/OWASP-Open-Source-Intelligence-Standard/`. The
`owasp.github.io` address redirects to it.

Needs repository admin rights. OWASP staff have said Pages sites will have to
migrate to the new CMS eventually.

All internal links are relative, so the site works from a subdirectory without
changes.

## Cache: bump the asset version when you change CSS or JS

GitHub Pages serves the HTML with `max-age=600` but CSS and JS with
`max-age=14400`, four hours. A deploy that changes both therefore lands new
markup against a stale stylesheet, which looks broken rather than merely old.

Both are requested with a version token to avoid this:

```html
<link rel="stylesheet" href="./assets/css/site.css?v=20260829">
<script src="./assets/js/site.js?v=20260829" defer></script>
```

Bump the token in all three pages whenever you edit `site.css` or `site.js`. The
changed URL misses both the CDN and browser caches, so the update is picked up
immediately instead of in four hours.

## Keeping it accurate

Every claim on the site is verifiable from the released standard. Where counts
appear in prose, check them against the release before changing the version
number in the footer.

External references are cited as landing pages, not as direct file paths.
A deep link to a PDF broke once already when the publisher reorganised its
files; landing pages survive that.

Deliberate omissions, which should stay omitted until they are true: adoption
claims, endorsement claims, certification language, and named external
reviewers.
