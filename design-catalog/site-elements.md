# Site element inventory

- **Date:** 2026-09-16
- **Legend:** **M** must-have for v1, **N** nice-to-have, **X** out of scope for v1
- Every row names the content or asset it depends on. Rows whose dependency is unresolved are called out in `assets-needed.md`.

## Pages

| Page | Priority | Purpose | Depends on |
|---|---|---|---|
| `/` Home | M | The quote, the room, what is pouring right now, hours, where to find us | Hero photo, tagline, hours |
| `/menu` | M | Live beer list plus the full non-beer menu as real text | Untappd embed (have), current drinks menu prices |
| `/about` | M | Three owners, the Czech side-pull program, the 8 ball, what "meantime" means | Owner bios, one photo of the three |
| `/visit` | M | Address, map, hours, parking and transit, accessibility, what to expect, food policy | Address (have), accessibility facts |
| `/pals` | M | The Pal membership: what it costs, what it gets you, how to join | Current terms, join mechanism |
| `/events` | N | Pop-ups, parties, tap takeovers, Pal parties | Whether they run a calendar at all |
| `/shop` | X for v1 | Merch. The current store is empty; either stock it or unpublish it | Owner decision, inventory |
| `/privacy` | M | Required once any analytics or mailing list exists | Provider choices |

Four pages today become five or six. That is still small enough to stay static and hand-maintained.

## Global

| Element | Priority | Notes |
|---|---|---|
| Header with real wordmark | M | SVG, not a PNG. Falls back to live type if the SVG is missing |
| Nav: Menu, About, Visit, Pals | M | Four items. Cart link goes away with the empty store |
| Footer: address, hours, Instagram, email, credits | M | Same block every page |
| Skip link | M | Already present in the Squarespace build; keep the behaviour |
| Favicon, apple-touch-icon, 512px PWA icon, webmanifest | M | Use the triangle M mark |
| `LocalBusiness` / `BarOrPub` JSON-LD with real address, geo, hours, phone or email, priceRange | M | Replaces the current empty-string block |
| Per-page title and meta description | M | Kill "Homepage" everywhere |
| Per-page OG image, 1200x630 | M | Current one is a 1500x400 logo over http |
| `sitemap.xml`, `robots.txt`, `llms.txt` | M | Umbo pattern |
| Analytics | N | Owner decision. Note Untappd's embed already fires a Segment pixel on the menu page |
| Reduced-motion handling | M | Marquee must stop under `prefers-reduced-motion` |

## Home

| Element | Priority | Notes |
|---|---|---|
| Hero: wordmark or the quote at display size | M | "Life is what happens while you're in the meantime." is the best asset on the current site. Keep it, set it in the new display face |
| Hero photo | M | Only one usable photo exists today. Needs at least one more |
| "What's pouring" strip | M | Three to six current taps pulled from the same Untappd source, linking to the full menu. This is the differentiator from every peer site |
| Hours block with today highlighted | M | Hours are already on the site but static and undifferentiated |
| Address plus map link | M | |
| Voice band (marquee): HOME OF FOAM // LAGER BAR // TASTY BEVERAGES | M | Already a brand device on `/menu`. Promote it, mark it up as a decorative strip rather than an h1 |
| Short "what this place is" paragraph | M | Two sentences, in the printed-menu voice. Currently the site says nothing about itself |
| Pal membership teaser | M | Highest-value content the site is missing |
| Instagram strip or curated gallery | N | Needs either an embed decision or hand-picked images |
| Mailing list capture | N | Provider decision. Kit is the Umbo precedent |

## Menu

| Element | Priority | Notes |
|---|---|---|
| Untappd embed (On Tap, Retail) | M | Carry over unchanged: location 51955, theme 177723. Keep the "updated at" stamp visible, it is the credibility |
| **Non-beer menu as real HTML text** | M | Replaces `MenuForWebsiteMARCH.png`. House specials, cocktails, non-alcoholic, wine by glass and bottle, with prices |
| Half pours and full pours note | M | On the printed menu, absent from the site |
| Magic 8 ball shot as a feature, not a line item | N | Best piece of theatre they have |
| Mlíko shot explainer | N | One sentence on what a side pull is and why the foam is the point |
| Food policy line | M | No kitchen, bring your own food, pop-ups happen |
| Menu schema JSON-LD | N | Only after the text menu exists |
| Owner-editable path for the text menu | M | Decide: a single data file the owner edits, or we edit on request. Must be written down, not assumed |

## About

| Element | Priority | Notes |
|---|---|---|
| Origin story: coffee in California to beer in Detroit, the 8 Degrees Plato space | M | Press quotes exist; owners should approve the retelling |
| Three owner bios with photos | M | Photos needed |
| The Czech program: two LUKR side pulls, mlíko, Midwest Leisure with Florian East | M | |
| Room photos | M | |
| What "meantime" means | M | One drink or six, nobody is counting |

## Visit

| Element | Priority | Notes |
|---|---|---|
| Address, embedded map | M | Use OpenStreetMap embed. Google's `output=embed` gets blocked in frames (Umbo precedent) |
| Hours, including the Tuesday closure | M | |
| Parking and transit, QLine stop | M | Needs local verification |
| Accessibility: entrance, restroom, seating | M | Owner must supply. Do not guess |
| Age policy, dogs, large groups, buyouts | N | Owner input |
| Contact: email, Instagram, phone if they want one published | M | `408-504-4770` is unverified aggregator data. Do not publish until confirmed |

## Pals

| Element | Priority | Notes |
|---|---|---|
| What it is, price, what you get | M | Launch terms were $80 first year, $60 after, 15% off, 25% off Mondays, $5 house lager, merch discount, three parties. Must be re-confirmed |
| How to join | M | In person, or a link if they sell it online |
| Member parties | N | Ties to `/events` if that page ships |

## Explicitly out of scope for v1

- Rebuilding the merch store. Either the owners stock it or we unpublish it; a storefront is not a v1 deliverable.
- Online ordering or reservations. A 25-to-50-seat neighborhood bar with walk-in service does not need either.
- Scraping Untappd. The embed is the supported path, and the Fly Trap precedent is that public ordering pages do not get scraped.
- A CMS. Four to six static pages, edited in the repo.
