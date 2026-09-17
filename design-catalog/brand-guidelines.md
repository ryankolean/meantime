# Meantime - brand guidelines and design system

- **Date:** 2026-09-16
- **Status:** proposed for owner approval. Every value below is either measured from an existing Meantime asset or justified against one. Nothing here is invented for decoration.
- **Evidence base:** `Meantime_Horizontal+Logo_Full+Color.png` (logo source), `MenuForWebsiteMARCH.png` (printed menu), computed styles from meantimeoncass.com, press coverage. See `meantimeoncass-com-design-spec.md` and `instagram-brand-intel.md`.

---

## 1. Color

### Core palette

| Token | Hex | Where it comes from | Role |
|---|---|---|---|
| `--ink` | `#1A120B` | Measured on the live site; logo quantizes to `#1A120C` | All body text, nav, rules, and the dark section ground |
| `--cream` | `#F5F2EF` | Measured, the live site's dominant section background | Default page ground |
| `--pink` | `#FBC9D8` | Measured from the logo file | Section ground, bands, highlights. Never text |
| `--yellow` | `#FDD757` | Measured from the logo file | Section ground, bands, the mark. Never text on a light ground |
| `--paper` | `#FFFFFF` | Printed menu ground | Cards and menu panels that need to sit above cream |
| `--muted` | `#5C5046` | Derived: ink lightened to the lightest value that still clears AA on all three grounds | Secondary text, captions, timestamps |

Six values. Three of them are the logo. No gradients, no shadows, no fifth hue.

### Contrast (WCAG 2.1, computed)

| Foreground | Ground | Ratio | AA normal | AA large |
|---|---|---|---|---|
| `--ink` | `--cream` | 16.59:1 | pass | pass |
| `--ink` | `--pink` | 12.73:1 | pass | pass |
| `--ink` | `--yellow` | 13.24:1 | pass | pass |
| `--ink` | `--paper` | 18.50:1 | pass | pass |
| `--muted` `#5C5046` | `--cream` | 7.00:1 | pass | pass |
| `--muted` | `--pink` | 5.37:1 | pass | pass |
| `--muted` | `--yellow` | 5.59:1 | pass | pass |
| `--cream` | `--ink` | 16.59:1 | pass | pass |
| `--pink` | `--ink` | 12.73:1 | pass | pass |
| `--yellow` | `--ink` | 13.24:1 | pass | pass |
| ~~`--yellow`~~ | ~~`--cream`~~ | **1.25:1** | **fail** | **fail** |
| ~~`--yellow`~~ | ~~`--pink`~~ | **1.04:1** | **fail** | **fail** |

Every pair the system permits clears AA for normal text. The two struck rows are the mistake on the live site today (the homepage call to action is yellow on off-white at 1.25:1) and they are forbidden.

### Rules

1. **Ink is the only text color on light grounds.** `--muted` is allowed for secondary text. Nothing else.
2. **Pink and yellow are grounds, never type.** On ink, cream/pink/yellow may all be used as type.
3. **Section alternation:** cream is the default. Pink and yellow appear as full-bleed bands used sparingly, at most one of each per page. Ink is the closing band (footer, or one dark feature section).
4. **Pink and yellow never touch each other** except inside the logo mark, where they already do.
5. Do not introduce a hover tint. Hover states change weight, underline, or the ground swap, not the hue.

---

## 2. Typography

### Faces

| Role | Face | Source | Why this one |
|---|---|---|---|
| Display | **Instrument Serif** 400 + italic | Google Fonts | The live site's one good typographic move is a high-contrast condensed display serif (`kepler-std-condensed-display`) set very large with tight leading. Instrument Serif is the closest freely licensable analog: condensed, high-contrast, editorial, built for large sizes. The italic covers the printed menu's italic-serif joke lines |
| UI and body | **Archivo** 400 / 500 / 700 | Google Fonts | The site's body face is `aktiv-grotesk`, an Adobe-licensed neo-grotesque. Archivo is the nearest free grotesque with the same slightly warm, slightly condensed character, and it holds up in the small, letter-spaced, all-caps labels the printed menu uses everywhere |
| Wordmark | The logo's own face, **unidentified** | owner | Shipped as SVG artwork, not as webfont type. Until the source is supplied, the wordmark is an image with a text alternative |

Both webfonts are self-hostable, which matters: the current site's Adobe Fonts kit does not transfer to a repo we control.

Retire `Poppins`. It loads on the live site and renders nothing.

### Scale

Fluid between 375 and 1440. Values are the two endpoints.

| Token | Mobile 375 | Desktop 1440 | Line height | Tracking | Face | Use |
|---|---|---|---|---|---|---|
| `--fs-display` | 56px | 120px | 0.88 | -0.01em | Instrument Serif | The hero quote, one per page |
| `--fs-h1` | 40px | 72px | 0.95 | -0.01em | Instrument Serif | Page titles |
| `--fs-h2` | 30px | 44px | 1.05 | -0.01em | Instrument Serif | Section headings |
| `--fs-h3` | 22px | 26px | 1.2 | 0 | Archivo 700 | Sub-sections, menu group names |
| `--fs-label` | 12px | 13px | 1.2 | 0.18em, uppercase | Archivo 700 | The printed menu's letter-spaced small-caps labels |
| `--fs-body` | 17px | 18px | 1.6 | -0.01em | Archivo 400 | Body copy. Larger than the live site's 15-17px |
| `--fs-small` | 15px | 15px | 1.5 | 0 | Archivo 400 | Captions, hours rows, timestamps |

The live site's leap from a 129px h1 straight to 15px hours rows leaves no middle. `--fs-h2` and `--fs-h3` exist to fill it.

Body copy never goes below 15px. The current hours block at 15.27px is the floor, not the target.

---

## 3. Space, shape, and line

- **Spacing scale (px):** 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Section padding is 64 mobile / 128 desktop.
- **Measure:** body text maxes at 66 characters. Display text maxes at 16 words a line.
- **Container:** 1200px max, 20px gutters mobile, 40px desktop.
- **Radius: 0 everywhere.** The mark is three hard triangles and the printed menu is hairline boxes. Rounded corners are off-brand.
- **Borders:** 1px `--ink` hairlines, and 2px for emphasis boxes. Straight from the printed menu.
- **Shadows: none.** Depth comes from the color bands.
- **Dividers:** either a 1px ink rule, or the triangle motif (below) centered between sections.

---

## 4. The motif: the triangle

The mark is a yellow triangle, a pink triangle, and an ink triangle locked into a square that reads as an **M**. That triangle is the structural device for the whole site, the way the scallop shell is for Umbo.

Permitted uses:
- Section divider: one small ink triangle, or the three-triangle mark, centered.
- List bullets: a solid ink triangle instead of a disc.
- "More" and link affordances: a small right-pointing triangle after the label, which the Untappd embed already uses (`More Info`).
- Band edges: a sawtooth of triangles along the top or bottom edge of a pink or yellow band. Use once per page at most.
- Empty and loading states: the mark, at rest.

Never rotate the mark, never outline it, never animate it into a spinner.

---

## 5. Components

### Buttons

The live site has no button system. This one is deliberately blunt, to match the printed menu.

| Variant | Ground | Text | Border | Hover | Use |
|---|---|---|---|---|---|
| Primary | `--ink` | `--cream` | none | ground goes `--yellow`, text goes `--ink` | One per view. "See what's pouring" |
| Secondary | transparent | `--ink` | 2px `--ink` | ground fills `--ink`, text `--cream` | Everything else |
| Quiet | transparent | `--ink` | none, underlined | underline thickens to 2px | Inline links |

All buttons: Archivo 700, uppercase, 0.08em tracking, 14px, padding 14px 24px, radius 0, no transition longer than 150ms.

### Links in body copy

Ink, underlined at 1px with a 3px offset, thickening to 2px on hover and focus. Never a color change, since the only accent colors available fail on light grounds.

### Focus

2px `--ink` outline with a 2px offset on cream and paper; 2px `--cream` outline on ink bands. Never removed.

### Menu rows

Item name (Archivo 700, 18px) and price (Archivo 500, tabular figures) on one line with a dotted ink leader between them; description underneath in Instrument Serif italic, `--muted`, 16px. That is the printed menu's exact structure, and it is what makes the text menu feel like the paper one.

### Cards

Only for beer entries and owner bios. `--paper` ground, 1px ink border, radius 0, 24px padding.

### The marquee

`HOME OF FOAM // LAGER BAR // TASTY BEVERAGES` scrolling horizontally on a pink or yellow band, Archivo 700 uppercase, ink. It already exists on `/menu`. It must be marked up as a decorative element with `aria-hidden`, not as a heading, and it must stop under `prefers-reduced-motion: reduce`.

### Forms

Ink 1px border, 0 radius, 16px padding, label above in `--fs-label`. Error text in ink, bold, with a triangle bullet. No red, since red is not in the palette.

---

## 6. Motion

- Transitions: 150ms ease for color and border, 250ms for transforms. Nothing longer.
- No scroll-jacking, no parallax, no fade-in-on-scroll that leaves content invisible if the observer never fires. Content is visible by default and enhancement is additive. (Umbo precedent: reveal-on-scroll left a hidden-tab site rendering as text only.)
- `prefers-reduced-motion: reduce` stops the marquee and removes every transform.

---

## 7. Photography

- The room as it actually is: striped sofa, cut flowers, low tables, full glasses, mid-century furniture, warm light.
- Beer at the moment of the side pull, foam intact. The mlíko pour is the single most photogenic thing in the building.
- People, mid-laugh, mid-conversation, not posed with product.
- No stock, no cold blue tones, no top-down flat lays, no beer-nerd macro of a tulip glass on a black background.
- Treatment: warm, slightly grainy, unretouched. Crops are square or 3:2.

---

## 8. Logo

- **Lockups:** horizontal (mark plus wordmark), wordmark alone, mark alone. All three exist as PNG; SVG is needed.
- **Clear space:** the height of the mark's short edge on all four sides.
- **Minimum size:** wordmark 120px wide, mark 24px.
- **Color:** full color on cream or paper. All-ink on pink or yellow. All-cream on ink. Never on a photograph without a solid panel behind it.
- **Never:** recolor, stretch, outline, add effects, set the wordmark in a substitute typeface, or use the mark as a bullet at text size (the plain triangle does that job).
- Alt text is `Meantime`, not `Meantime Homepage`. The live site gets this wrong on all four instances.

---

## 9. Voice

The printed menu is the voice document. Banner line, verbatim:

> **WE'RE GLAD YOU'RE HERE // LAUGH TOO LOUD // STAY FOR ANOTHER**

### Rules

1. Short. Most lines are under eight words.
2. Dry and Midwestern. "ope, just gonna sneak past ya".
3. Never explain the joke, and never repeat one twice on the same page.
4. No beer-nerd credentialing. The bar pours a Czech pilsner through a side pull and a Capri Sun for $2 with the same face.
5. Second person, present tense. The reader is already a regular.
6. Lowercase is fine in display type. Labels are uppercase.
7. The "meantime" wordplay is load-bearing, so ration it: the tagline, and at most one other place on the site. It stops being clever the third time.

### Do / don't

| Do | Don't |
|---|---|
| "No kitchen. Bring food, we don't mind." | "Meantime does not offer a food program at this time." |
| "Two side pulls, pouring Czech lagers the way they're meant to be poured." | "We leverage authentic LUKR side-pull faucet technology." |
| "Ask the 8 ball. It decides." | "Try our signature Magic 8 Ball Shot experience!" |
| "Monday 3-10. Tuesday we rest." | "Please note our modified Tuesday hours." |
| "Stay for another." | "In the meantime, why not stay in the meantime?" |

---

## 10. Open items

These are the choices this document cannot make on its own. They are tracked in `assets-needed.md`.

1. The wordmark typeface and its license, which decides whether the wordmark can ever be live text.
2. Whether pink or yellow is the primary accent band. The logo weights them equally; the site needs a lead.
3. Photography. The system above assumes a real photo set exists. Today there is one usable image.
4. Whether Pal membership sells online, which decides if any commerce stays on the site.
