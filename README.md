# meantime

Website for **Meantime**, a lager bar at 3409 Cass Ave, Detroit, MI 48201.

- Live (current, being replaced): https://www.meantimeoncass.com/
- Instagram: https://www.instagram.com/meantimeoncass
- Jira: SUMMIT-178

Static multi-page site, no build step, served from GitHub Pages.

## Layout

| Path | What |
|---|---|
| `design-catalog/` | Research: current-site audit, brand intel, competitive scan, element inventory, brand guidelines |
| `assets/` | CSS, JS, images |
| `scripts/` | Base-URL rewrite, social preview image generator |

## Local preview

Any static server at the repo root, e.g. `python3 -m http.server 8770`.

## Social preview images

The five `assets/img/og-*.png` cards are generated, not hand-made:

```
python3 scripts/make-og-images.py
```

Headless Chrome sets each 1200x630 card in the site's own display face, and the
script measures the rendered pixels back against the layout grid before writing.
Copy and line breaks live in `PAGES` at the top of the script. Needs Chrome and
Pillow; the webfonts are cached in `scripts/.cache/` on the first run.
