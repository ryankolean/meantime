# Pre-launch checklist

This repo is currently a **preview**, served from GitHub Pages at
<https://ryankolean.github.io/meantime/>. It is deliberately not indexable.

Everything below has to happen before this site becomes the real
meantimeoncass.com. Tracked as a go-live gate in **SUMMIT-195**.

## Why the preview is blocked from search engines

The pages are authored for the production host. Their canonical tags, `og:url`
and `og:image` all point at `https://www.meantimeoncass.com/...`. Today that
host is the old Squarespace site, which serves only `/`, `/home`, `/menu`,
`/store` and `/store/merch`.

So on the preview:

- `about`, `visit` and `pals` are **new pages** with no production counterpart.
  Their canonicals pointed at URLs that 404. Those tags are removed for now.
- every `og:image` points at `meantimeoncass.com/assets/img/og-*.png`, which the
  Squarespace site does not serve, so shared links unfurl without an image.

Rather than paper over that, the preview is closed to crawlers:
`Disallow: /` in `robots.txt`, plus `noindex, nofollow` on every page.

## At cutover

1. **`robots.txt`** - replace `Disallow: /` with `Allow: /`. Leave the sitemap
   line. **This is the one that actually matters**: shipping the current file to
   production deindexes the entire site.
2. **Remove the `noindex, nofollow` meta** from `index.html`, `menu.html`,
   `about.html`, `visit.html` and `pals.html`. Leave `styleguide.html` noindexed,
   it is an internal page.
3. **Restore canonical and `og:url`** on the three pages they were stripped from.
   `scripts/set-base-url.sh` rewrites tags that already exist; it cannot re-add
   these, so they go back by hand:

   ```html
   <link rel="canonical" href="https://www.meantimeoncass.com/about">
   <meta property="og:url" content="https://www.meantimeoncass.com/about">
   ```

   and the same for `visit` and `pals`.
4. **Confirm the URL shape.** The canonicals assume extensionless paths
   (`/about`, not `/about.html`). If the new host serves `.html`, run
   `scripts/set-base-url.sh` and fix the paths in `sitemap.xml` to match, or the
   canonicals will 404 again on the new host.
5. **Re-check `og:image`.** The five images under `assets/img/og-*.png` only
   resolve once this repo is what answers for the domain.
6. **Re-run the link audit** against the live host. Every `href` and `src` on all
   six pages should resolve; do not trust a build status.

## Before any of that

See `design-catalog/assets-needed.md`. The blocking items are still open, in
particular confirmed menu prices, contact details and the accessibility facts
for the Visit page.

## A note for the owners

If you are taking this site over: the drinks card on the menu page is typed out
from the printed card, so **the prices on the site are only right as long as the
printed card is**. When the card changes, `menu.html` changes with it. The tap
list above it is live from Untappd and looks after itself.

The wordmark is set in **Gango Black** by Adam Fathony. The site uses your logo
artwork rather than the font, so nothing is licensed to us. If you want the
wordmark as live text anywhere, that needs whoever drew the logo to hand over
their licence, or a webfont licence bought from MyFonts.
