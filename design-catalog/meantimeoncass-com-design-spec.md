# Design Spec: meantimeoncass.com

## Meta
- **URL:** https://www.meantimeoncass.com/
- **Extracted:** 2026-09-16
- **Method:** computed styles read via JS in a rendered Chromium session at 1440x900 and 375x812. Screenshots captured at 1440.
- **Platform:** Squarespace 7.1 (fluid engine), Adobe Fonts (Typekit) for webfonts, Untappd for Business embed on the menu page, Squarespace Commerce for the store.
- **Site type:** Neighborhood lager bar, open since May 2025.
- **One-line character:** Three-page Squarespace shell carrying a genuinely good logo. Big editorial serif headline on warm off-white, one photo, hours, and a link out to a live beer list. Almost none of the brand's real personality (the printed menu artwork, the voice, the room) is on the site.

## Pages (complete, from sitemap.xml)

| URL | Title tag | Notes |
|---|---|---|
| `/home` (served at `/`) | `Meantime Homepage` | Hero quote, one photo, Location + Hours, Instagram icon |
| `/menu` | `Menu - Meantime Homepage` | Untappd for Business embedded live menu plus a static PNG of the non-beer menu |
| `/store` | `Store 2 - Meantime Homepage` | Empty. Renders "No results found" |
| `/store/merch` | not captured | Category page under the empty store |

There is no about page, no events page, no contact page, no Pal membership page, and no phone number anywhere on the site.

## Color palette (measured)

| Role | Value | Notes |
|---|---|---|
| Section background | `#F5F2EF` rgb(245,242,239) | Warm off-white. Largest painted area on the page |
| Body background | `#FAC8D3` rgb(250,200,211) | Pink. Only visible as a band where sections do not cover it, apparently unintentional |
| Ink | `#1A120B` rgb(26,18,11) | Espresso brown-black. Body copy, nav, hours |
| Heading black | `#000000` | h1 and h3 render pure black, not the ink token. Two near-blacks in use |
| Accent yellow | `#FDD757` rgb(253,215,87) | The 54px "Menu" call to action on the homepage |
| Overlay | `rgba(26,18,11,0.5)` | Image scrim |

The logo source file (`Meantime_Horizontal+Logo_Full+Color.png`, 1500x400) quantizes to `#1A120C` ink, `#FDD757` yellow, `#FBC9D8` pink. The site's pink is within two points per channel of the logo pink, so treat `#FBC9D8` as the brand value and the site value as drift.

### Contrast (computed, WCAG 2.1)

| Pair | Ratio | AA normal | AA large |
|---|---|---|---|
| ink `#1A120B` on cream `#F5F2EF` | 16.59:1 | pass | pass |
| ink on pink `#FBC9D8` | 12.73:1 | pass | pass |
| ink on yellow `#FDD757` | 13.24:1 | pass | pass |
| yellow `#FDD757` on cream `#F5F2EF` | **1.25:1** | **fail** | **fail** |
| yellow on pink `#FBC9D8` | 1.04:1 | fail | fail |
| yellow on ink | 13.24:1 | pass | pass |

**The homepage's primary call to action is yellow text on off-white at 1.25:1.** It fails AA by a wide margin at any size. Yellow is only usable as a background, or as type on ink.

## Typography (measured)

- **Display:** `kepler-std-condensed-display` 400 (Adobe Fonts). Loaded in 400/700, roman and italic.
- **UI and body:** `aktiv-grotesk` (Adobe Fonts), 400/500/700, roman and italic.
- **Also loaded:** `Poppins` 500 and Squarespace's own UI font. Poppins does not appear in any rendered text, so it is template residue costing a request.
- **Neither webfont is the logo face.** The wordmark is a heavy geometric lowercase display face with angular shear cuts on the m, t and e. It appears nowhere on the site as live type, only as a PNG.

| Element | Desktop 1440 | Mobile 375 | Notes |
|---|---|---|---|
| h1 | 129.2px / 114.11px lh / -0.01em | 80.31px / 70.93px | Fluid. Line height 0.883, tight and intentional |
| h3 | 42.5px / 47.94px | not captured | Section labels ("Location", "Hours") |
| p | 17px / 27.2px / -0.02em, weight 500 | 16px | aktiv-grotesk |
| Hours rows | 15.27px | not captured | Smaller than body copy |
| Nav links | 16px, uppercase, -0.32px | not captured | |

Character: one large editorial serif statement, everything else small sans. No mid-scale, so the page has only two real levels of hierarchy.

## Layout and grid

- Single Squarespace fluid-engine column, two full-bleed sections (1233px and 857px tall at 1440).
- Page scrollHeight 1616px at 1440, 1516px at 375. The entire homepage is about two screens.
- Header: PNG logo left, "Menu" link and a cart counter right. Two nav items total.
- No footer beyond the Location/Hours block and a single Instagram icon.
- **Mobile:** no horizontal overflow at 375 (scrollWidth 375 equals clientWidth 375). The h1 scales to 80px, very large for the viewport but not broken.

## Components

- **Buttons:** none. Both calls to action are plain text links. The button probe returned a 0px-radius, 0px-border, transparent element, so there is no button system to inherit.
- **Cards:** none on the site itself. The Untappd embed brings its own card styling for beer entries.
- **Forms:** none. No mailing list capture, no contact form.
- **Imagery:** one photograph on the homepage (`R0000415~2.JPG`, rendered 1325x621) showing the room: a striped vintage sofa, cut flowers, and full beer glasses on a low table. Alt text on all four logo instances is the string "Meantime Homepage", which is wrong on every one.
- **Iconography:** one Instagram glyph from Squarespace's social icon font.

## The menu page

- `/menu` runs an **Untappd for Business embedded menu**: `business.untappd.com/locations/51955/themes/177723/js` plus `embed-menu-preloader.untappdapi.com`. Location id **51955**, theme **177723**. Not an iframe; it injects into the page.
- The embed renders "On Tap" (Draft, On Deck) and "Retail" (New Retail This Week, Bottles). Each entry carries beer name, style, ABV, IBU, brewery, brewery city, Untappd rating, description, and a label image from `labels.untappd.com`. It stamps a timestamp, observed as "Updated on Sep 16, 6:28 PM EDT".
- It also fires a Segment tracking pixel (`api.segment.io/v1/pixel/track`) on menu view.
- The beer list is therefore **already live and self-maintaining**. This is the most important finding for the rebuild: the beer program does not need hand entry, and the same embed can move to a new site unchanged.
- The **non-beer menu is a static PNG**, `MenuForWebsiteMARCH.png` (served 1500x1159). It carries house specials, cocktails, non-alcoholic drinks, and the full wine list with prices. The filename says March. It is invisible to search engines and to screen readers, cannot be edited without re-exporting artwork, and its prices may be six months stale.
- A marquee repeats "HOME OF FOAM LAGER BAR TASTY BEVERAGES" three times as a scrolling strip. It is marked up as `h1`, so the page has four `h1` elements, one of which is the concatenated marquee string.

## SEO and metadata (measured)

- Title tags are Squarespace defaults: `Meantime Homepage`, `Menu - Meantime Homepage`, `Store 2 - Meantime Homepage`. The word "Homepage" sits in the site title, so it appears in every browser tab, every share card, and every search result.
- **No meta description** on the homepage.
- `og:title` and `og:site_name` are both "Meantime Homepage". `og:image` is the horizontal logo, served over `http://`, at 1500x400, the wrong aspect for most social cards.
- Two JSON-LD blocks. The `WebSite` block names the site "Meantime Homepage". The `LocalBusiness` block has **`"address": ""` and `"openingHours": ""`**, both empty strings, and no name, telephone, geo, or price range. That is worse than having no structured data at all.
- `robots.txt` is the Squarespace default. `sitemap.xml` lists four URLs.
- No `llms.txt`, no FAQ content, no Event schema, no Menu schema.

## Animations and interactions

Not meaningfully present. No scroll reveals, carousels, or hover systems were detectable. The marquee on `/menu` is the only motion on the site.

## Responsive behavior

- 1440: as described above.
- 375: clean, no overflow, h1 80px, body 16px, hours 15px.
- Squarespace's hamburger takes over at its own breakpoint. Nothing custom.

## Characteristic elements

1. **A real logo doing nothing.** The mark (a yellow and a pink triangle forming an M) and the heavy lowercase wordmark are distinctive, and they appear only as a header PNG.
2. **One quote as the entire homepage.** "Life is what happens while you're in the meantime." set at 129px is the site's whole idea, and it works.
3. **Off-white and espresso with a yellow that cannot be read.** Two-thirds of a good palette, applied wrong.
4. **A live beer list bolted onto a dead site.** The Untappd embed is current to the minute while the food and cocktail menu is a PNG from March.
5. **An empty store.** `/store` is published, linked from the cart, and returns "No results found".
6. **No story, no people, no room.** Three owners, a Czech side-pull program, a magic 8 ball, and a membership club, none of it on the site.

## Review and changelog

- Standards review: not run.
- Patches applied: none. This document is observation only.
