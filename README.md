# meantime

Website for **Meantime**, a lager bar at 3409 Cass Ave, Detroit, MI 48201.

- Live (current, being replaced): https://www.meantimeoncass.com/
- Instagram: https://www.instagram.com/meantimeoncass
- Jira: SUMMIT-178 (build), SUMMIT-195 (go-live gate)

Static multi-page site, no build step, served from GitHub Pages.

The GitHub Pages deploy is a **preview** and is closed to search engines on
purpose (`Disallow: /` plus `noindex`). See `PRE-LAUNCH.md` for how to open it
up at cutover.

## Layout

| Path | What |
|---|---|
| `PRE-LAUNCH.md` | Go-live checklist. **Read this before pointing the domain here** |
| `design-catalog/` | Research: current-site audit, brand intel, competitive scan, element inventory, brand guidelines |
| `assets/` | CSS, JS, images |

## Local preview

Any static server at the repo root, e.g. `python3 -m http.server 8770`.
