# Globant Adobe Studio — Brand Reference
## Single source of truth for all visual artifacts

**Brand identity**: Globant · Adobe Studio  
**Logo**: Globant wordmark + `#BFD732` chevron. Always Globant branding — never "GUT", "gut", or any sub-brand name.

**Logo assets** (bundled):
- Logotipo (wordmark + chevron): `assets/globant-logotipo-light.png` → light backgrounds
- Isotipo (chevron only): `assets/globant-isotipo.png` → standalone mark or favicon
- Dark variant: CSS `filter: brightness(0) invert(1)` on logotipo → white version for dark slides
- Chevron color in PNG: `#BFD732`

---

## 1. Typography

### Primary font — Plus Jakarta Sans (Adobe Studio default)
```html
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
```
| Element | Weight | Size |
|---|---|---|
| Hero / main title | 800 ExtraBold | 48–64px |
| Section title | 700 Bold | 32–40px |
| Card header | 600 SemiBold | 16–20px |
| Body | 400 Regular | 14–16px |
| Subtitle | 300 Light | 14px |

---

### Presentation font system — Heebo + Libre Baskerville
Used when producing slide decks and presentation artifacts.

```html
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Heebo:wght@100;300;400;700;900&display=swap" rel="stylesheet">
```

**Title mixing rule** — both fonts alternate within the same headline:
- **Heebo Bold** → structural/main words
- **Libre Baskerville italic** → 1–3 emphasis words embedded in the headline (never entire title)

Real examples:
- `Titular` *(Heebo bold)* + `donde destaques con esta tipo` *(Libre Baskerville italic)* + `lo que necesites.` *(Heebo bold)*
- `Resumen` *(Heebo regular)* + `Ejecutivo.` *(Libre Baskerville italic)*
- `Comprensión` *(Heebo bold)* + `As Is` *(Libre Baskerville italic)*

**Presentation type scale**:
| Element | Font | Weight | Size | Line height |
|---|---|---|---|---|
| Main title (2–3 lines) | Heebo + Libre Baskerville | Bold + Italic | ~36px / 18pt | 1.0–1.1 |
| Main title (full width, 1 line) | Heebo + Libre Baskerville | Bold + Italic | ~36px | 1.0 |
| Hero title (large format) | Heebo + Libre Baskerville | Bold + Italic | ~60px / 30pt | 1.0 |
| Subtitle | Heebo | Regular | ~20px / 10pt | 1.15 |
| Body paragraph | Heebo | Regular | 16–20px / 8–10pt | 1.15 |
| Bullet text | Heebo | Regular | 16–20px | 1.15 |
| Bold inline emphasis | Heebo | Bold 700 | same as surrounding | — |
| Decorative section number | Heebo | ExtraBold | 80–120px | — |
| KPI / metric | Heebo | ExtraBold | 28–40px | 1.0 |
| Breadcrumb | Heebo | Regular | 10–11px | — |
| Diagram label | Heebo | Bold | 12–14px | 1.2 |
| Diagram descriptor | Heebo | Regular | 10–11px | 1.3 |
| Card number header | Heebo | Bold | 20–24px | — |
| Card body text | Heebo | Regular | 12–14px | 1.3 |
| Table header | Heebo | Bold | 12–13px | — |
| Table cell | Heebo | Regular | 11–12px | 1.3 |

**Bullet rules**:
- Always round bullet (•) — never dashes, arrows, or custom markers
- Text: Heebo Regular — never italic in bullets
- Bold inline: Heebo Bold for key terms only
- Optional container: thin outline box, `border: 1px solid #000` (light), border-radius 6px

**Absolute rules**:
- Never all-caps anywhere — headings, labels, buttons, diagrams
- Libre Baskerville italic: headline accent words ONLY — never body, bullets, labels, tables, or diagrams
- Body is always Heebo Regular — no serif in paragraphs
- Line-height never exceeds 1.15

**Exception — "Uso preferente" / "Uso puntual no preferente" labels**:
- These are annotation labels used in brand guide documents to mark preferred vs non-preferred usage
- "Uso preferente": purple/violet filled pill, white Heebo Bold text
- "Uso puntual no preferente": orange filled pill, white Heebo Bold text
- These labels are meta-annotations only — never use in client-facing deliverables

---

## 2. Color System

Every artifact commits to one mode — light or dark. Always produce both variants.

### Light mode (content, workshop, operational)
```css
--bg:              #FFFFFF;
--text-primary:    #000000;
--text-secondary:  #3D3D3D;
--text-muted:      #7A7A7A;
--accent-green:    #C5FF02;   /* PRIMARY accent */
--accent-green-lt: #E8FF80;   /* Light funnel / diagram tints */
--accent-green-dk: #5A8A00;   /* Dark funnel / diagram bottom */
--border:          #000000;   /* Card borders, dividers */
--border-light:    #E0E0E0;   /* Table rows, subtle separators */
--card-header-bg:  #000000;   /* Number card header fill */
--card-header-text:#FFFFFF;
```

### Dark mode (formal, cover, premium)
```css
--bg:              #000000;
--text-primary:    #FFFFFF;
--text-secondary:  #CCCCCC;
--text-muted:      #888888;
--accent-green:    #C5FF02;   /* Same — always #C5FF02 */
--accent-green-lt: #E8FF80;
--accent-green-dk: #5A8A00;
--border:          #FFFFFF;
--border-light:    rgba(255,255,255,0.15);
--card-header-bg:  #000000;   /* Same fill, visible via border */
--card-header-text:#FFFFFF;
```

### Half-and-half split slide
One valid layout uses left panel dark (`#000000`) + right panel light (`#FFFFFF`) side by side:
- Left: dark bg, white text, title + body with `#C5FF02` left border accent on text block
- Right: white bg, black text, numbered list or diagram content
- Dividing line: none — the bg color change is the separator
- Logo: top-right of full slide (always)

### Accent color usage map
| Element | Value |
|---|---|
| Primary CTA button fill | `#C5FF02` |
| Secondary CTA border | `#000000` (light) / `#FFFFFF` (dark) |
| Dark CTA fill | `#000000` |
| Chart / bar fill | `#C5FF02` |
| Funnel top (lightest) | `#E8FF80` |
| Funnel bottom (darkest) | `#5A8A00` |
| Timeline line fill | `#C5FF02` |
| Numbered step circle fill | `#C5FF02` |
| Icon circle background | `#C5FF02` |
| Venn center fill | `#C5FF02` |
| Venn circle strokes | `#CCCCCC` (light) / `#FFFFFF` (dark) |
| Map location dots | `#C5FF02` |
| Vertical separator line | `#C5FF02`, 1px |
| Card active/highlighted header | `#C5FF02` (replaces black header) |
| Table row dividers | `#C5FF02` thin underline |
| Left border text accent | `#C5FF02`, 3px solid left |
| Arrow connector between cards | `#C5FF02` filled circle + `→` |
| Wireframe orb | `#CCCCCC` strokes (light) / `#FFFFFF` strokes (dark), ~15% opacity |

**Logo chevron**: `#BFD732` — logo context only, never as UI accent  
**Never use**: `#BFD732` in UI · Any color outside this system · `#C5FF02` on icons

---

## 3. Logo

**Brand name**: Globant · Adobe Studio  
**Never say or write**: "gut", "GUT", "Gut" — the sub-brand name is never used in client artifacts

**Logo variants**:
- Light bg → black Globant wordmark + `#BFD732` chevron
- Dark bg → all white lockup

**Position in slides**: top-right corner — always  
**Confidentiality**: "Propiedad de Globant | Información confidencial" — rotated 90°, bottom-left, Heebo Regular ~9px, very small

---

## 4. Iconography

**Style**: Lineal (outline), thin stroke — never filled, never emoji, never illustrated  
**Color (light bg)**: `#000000`  
**Color (dark bg)**: `#FFFFFF`  
**Icon on `#C5FF02` circle bg**: `#000000` lineal icon  
**Never**: `#C5FF02` on standalone icons  

**Icon + circle treatment** (used in action/initiative grids):
- `#C5FF02` filled circle, ~48px diameter
- Lineal black icon centered inside
- Label below: Heebo Bold ~14px

**Source**: flaticon.com — outline/line style only

**Categories**: General · Flechas · Calendarios · Menús · Comunicación · Business · Atención · Dispositivos · Developer · System · Inteligencia artificial · Marketing · Transporte

---

## 5. Layout Templates

Every slide uses one of these. Always produce light and dark variants unless noted.

---

### TEMPLATE A — Standard two-column with photo (most common)
```
┌────────────────────────────────────────────────────────┐
│ / Apartado en el que estés          [Globant logo]    │
├────────────────────────────────────────────────────────┤
│  [Dual-font title, 2–3 lines]        [Photo block]   │
│  [Subtitle Heebo Regular]            [flush right,    │
│  [Body text]                          top & bottom,   │
│  [Optional bullet box w/ border]      ~43% width,     │
│  [Pill buttons, left-aligned]         no border-rad]  │
│  [Orb fragment bottom-left]                           │
└────────────────────────────────────────────────────────┘
```
- Column split: left ~57% · right photo ~43%
- Photo: no border-radius, no shadow, flush to right/top/bottom edge

---

### TEMPLATE B — Full-width title + diagram below/right
Used for: funnel, Venn, bubble process, bar chart, timeline.
```
┌────────────────────────────────────────────────────────┐
│ / Apartado                          [Globant logo]    │
├────────────────────────────────────────────────────────┤
│ [Full-width dual-font title — 1 line]                 │
│ [Subtitle — 1 line, Heebo Regular]                    │
│                                                        │
│  [Left col ~40% body text]   [Right col ~60% diagram] │
│                                                        │
│ [Orb bottom-left]                                     │
└────────────────────────────────────────────────────────┘
```

---

### TEMPLATE C — Section divider (dark mode only)
```
┌────────────────────────────────────────────────────────┐
│                             [Globant logo — white]    │
│  [Large wireframe number — left ~30%]                 │
│  [decorative, mesh texture, ~15% opacity]             │
│              [Dual-font title — center-right, 2 lines]│
│  [Propiedad de Globant... rotated bottom-left]        │
└────────────────────────────────────────────────────────┘
```
No light variant — dark only.

---

### TEMPLATE D — Photo collage grid
```
┌────────────────────────────────────────────────────────┐
│ / Apartado                          [Globant logo]    │
│  [Section number — Heebo ExtraBold, ~15% opacity]     │
│  [Dual-font title]                  [Photo mosaic]    │
│  [Body text]                        [staggered 2×2,   │
│                                      no border-rad,   │
│                                      slight offset]   │
│  [Orb bottom-left]                                    │
└────────────────────────────────────────────────────────┘
```
Photo rules: staggered layout, ~20px vertical offset between photos, touch or overlap, never rigid grid, never frames or shadows.

---

### TEMPLATE E — Map slide
```
┌────────────────────────────────────────────────────────┐
│ / Apartado                          [Globant logo]    │
│  [Dual-font title top-left, 2 lines]                  │
│  [World map ~75% width]           │ [Panel ~25%]      │
│  [#C5FF02 location dots]          │ [title + bullets] │
│                    (1px #C5FF02 vertical separator)   │
│  [KPI stats free-floating bottom] [descriptor below]  │
└────────────────────────────────────────────────────────┘
```
Map: flat monochromatic SVG — `#CCCCCC` landmasses on white / `#2A2A2A` on black. No 3D, no gradients.

---

### TEMPLATE F — Half-and-half split
```
┌──────────────────┬─────────────────────────────────────┐
│ DARK (#000000)   │ LIGHT (#FFFFFF)                     │
│                  │                                     │
│ [Large title     │ [Numbered list or diagram]          │
│  30pt, multi-    │ [01 Label: description text]        │
│  line, dual-font]│ [02 Label: description text]        │
│                  │ [03 Label: description text]        │
│ [Body with       │                                     │
│  #C5FF02 left    │                                     │
│  border accent]  │                                     │
│ [Orb bottom-left]│                                     │
└──────────────────┴─────────────────────────────────────┘
```
- Left panel: `#000000` bg, white text, dual-font title at ~30pt
- Right panel: `#FFFFFF` bg, black text, numbered steps
- Numbered step format: large number Heebo ExtraBold ~60px (left) + bold label: descriptor text (right)
- Logo: top-right spanning full slide width

---

### TEMPLATE G — Full-width card grid
Used when content needs equal-weight columns without a photo.
```
┌────────────────────────────────────────────────────────┐
│ / Apartado                          [Globant logo]    │
│ [Full-width dual-font title — centered or left]       │
│ [Subtitle — centered or left]                         │
│                                                        │
│ [Card 1] [Card 2] [Card 3] [Card 4]  ← 4 col grid    │
│                                                        │
│ [Orb bottom-left]                                     │
└────────────────────────────────────────────────────────┘
```
See card component patterns below.

---

### TEMPLATE H — Icon action grid (2×3 or 3×2)
Used for: initiatives, actions, capabilities.
```
┌────────────────────────────────────────────────────────┐
│ / Apartado                          [Globant logo]    │
│  [Title — left ~35%]    [Icon grid — right ~65%]      │
│  [Subtitle]             [2 rows × 3 cols]             │
│  [Body text]            [Each cell: icon circle +     │
│                          bold label + descriptors]    │
│  [Orb bottom-left]      [Vertical lines between cols] │
└────────────────────────────────────────────────────────┘
```
Grid separated by thin vertical lines (`#E0E0E0` light / `rgba(255,255,255,0.15)` dark).

---

## 6. Card Components

### Numbered header card (4-column grid)
Used for steps, phases, pillars:
```
┌──────────────────┐
│ [#000 bg]  01    │  ← Header: black fill, Heebo Bold white, centered
│                  │
│  Titular         │  ← Heebo Bold ~16px, centered
│  Lorem Ipsum 1   │
│                  │
│  Body text here  │  ← Heebo Regular ~12px, centered
│  body text here  │
└──────────────────┘
```
- Card border: 1px `#000000` (light) / `#FFFFFF` (dark)
- Header fill: always `#000000`, white text
- Active/highlighted card header: `#C5FF02` fill, black text
- Between cards: `#C5FF02` filled circle with `→` arrow (connector)

### Icon header card (4-column with icon)
```
┌──────────────────┐
│ [#000 bg]  ▽     │  ← Header: black fill + lineal white icon, centered
│  Titular         │
│                  │
│  Body text here  │
│  body text here  │
└──────────────────┘
```
- Active/highlighted: `#C5FF02` header fill, black icon, black text

### Photo + CTA card (4-column)
```
┌──────────────────┐
│ [Photo — top,    │  ← Full-width photo, no border-radius, ~40% card height
│  no border-rad]  │
│                  │
│  Card title      │  ← Heebo Bold ~16px, centered
│  Heebo Bold      │
│                  │
│  Descriptor text │  ← Heebo Regular ~12px, centered
│                  │
│ [CTA pill button]│  ← Centered below text, pill shape
└──────────────────┘
```
- Card border: none (cards separated by thin `#C5FF02` or `#E0E0E0` vertical line)
- CTA button: green (primary) or dark (secondary) — alternated across cards

### Timeline card (above + below horizontal line)
```
[Card above] → [dot on line] → [Card above]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ← #C5FF02 thick line
[Card below] ← [dot on line] ← [Card below]
```
- Timeline line: `#C5FF02`, thick (~8px), spans full width
- Dots: `#000000` filled circle on line
- End circles: `#C5FF02` large circle (~60px) with icon inside
- Cards above: numbered black-header cards
- Cards below: plain bordered cards with body text
- Footer bar: black full-width strip with text + tool logos (Figma, Google Sheets etc.)

---

## 7. Diagram System

### Funnel
- 4 layers: top (lightest, widest) → bottom (darkest, narrowest)  
- Color ramp: `#E8FF80` → `#C5FF02` → `#8BC400` → `#5A8A00`
- Layer labels: Heebo Regular ~11px centered, Heebo Bold ~12px for key term
- Right-side descriptors: Heebo Regular ~10px with thin `#C5FF02` underline per item

### Venn / overlapping circles
- Strokes: `#CCCCCC` (light) / `#FFFFFF` (dark), 1px, no fill
- Center intersection: `#C5FF02` filled circle (solid, ~40px)
- Center label: Heebo Bold ~12px, black text on green
- Connector arrow: thin `#C5FF02` curved line from center to bottom label
- Numbered badges: `#C5FF02` filled circle, Heebo Bold black text, outside each circle
- Bottom synthesis label: Heebo Bold + Libre Baskerville italic mix, ~20px
- Entity labels above diagram (e.g. "GLOBANT · ADOBE STUDIO — CLIENT — STAKEHOLDERS"): Heebo Regular small, spaced across top, connected by thin `#C5FF02` lines

### Bubble / circle process (horizontal chain)
- Circles: filled with green ramp (`#E8FF80` → `#5A8A00`), slightly overlapping
- Label inside: Heebo Bold white ~14px
- Descriptor below: Heebo Regular ~10–11px
- Section title above: Heebo Bold ~18px
- Connector between groups: `#C5FF02` horizontal arrow

### Bar chart
- Bars: `#C5FF02`, no gradient, no 3D
- Chart box: thin white/black border
- Grid lines: thin horizontal, low opacity
- Axis labels: Heebo Regular ~10px
- Dark slide: `#000000` bg, white border box, `#C5FF02` bars

### Numbered step list (right column or standalone)
- Large number: Heebo ExtraBold ~60px, `#FFFFFF` (dark) / `#000000` (light)
- Bold label: `Label:` Heebo Bold ~14px, followed by Heebo Regular descriptor
- Row separator: none (generous vertical spacing)

### Table
- Header row: black fill, white Heebo Bold text, centered
- Column headers: Heebo Bold ~12px, black text, no fill
- Cells: Heebo Regular ~11px
- Row dividers: thin `#C5FF02` underline
- Used alongside Venn or other diagrams in split layout

### Org chart circular (team / capability wheel)
Used for: team structure, service layers, delivery model.

**Structure**:
- Center: client logo placeholder — small square, red fill, white "Logo cliente" label, Heebo Bold ~10px
- Inner dashed ring label: "Capa Operativa" — Heebo Regular ~11px, centered above ring
- Outer ring: `#C5FF02` stroke 2px — boundary of the wheel
- Outer ring label: "Capa de gestión y supervisión" — Heebo Regular ~11px, top-center outside ring
- Role nodes (inner + outer ring): `#000000` filled circle ~64px, white lineal icon centered, white Heebo Bold role name ~10px below icon
- Anchor nodes: 2–3 `#C5FF02` filled circles ~80px at key positions (left, right, top) — "Project Manager", "Director Servicios al cliente" labels in Heebo Bold ~11px
- Annotation badge: `#C5FF02` filled pill, Heebo Bold ~10px label (e.g., "Equipo ilustrativo") — positioned outside ring at ~10-o'clock
- Icons inside nodes: lineal white, ~20px, representing role function

**Light bg**: `#FFFFFF` slide, `#000000` role nodes, `#C5FF02` anchors + outer ring  
**Dark bg**: `#000000` slide — same node and accent treatment

### Icon + text 3-column grid (open, no cards)
Used for: capabilities, services, integrated tasks — 3–6 items with icon + label + descriptor.

```
[Icon ~32px]  Bold label.     [Icon]  Bold label.     [Icon]  Bold label.
Descriptor text Heebo          Descriptor text          Descriptor text
Regular ~11px, 2–4 lines
```
- Icons: lineal `#000000` (light) / `#FFFFFF` (dark) — NOT inside circles for this pattern
- Label: Heebo Bold ~13px, period after label
- Descriptor: Heebo Regular ~11px, line-height 1.3
- 3 equal columns, no borders, no cards — whitespace separates columns
- Up to 2 rows (6 items total)
- Positioned below body text in left column, or full-width below title block

---

## 8. Button System

**Pill shape** (`border-radius: 999px`) is default for all contexts.  
**Rectangular** (`border-radius: 8px`) for UI/dashboard contexts only.

```css
.btn-base { font-family: 'Heebo', sans-serif; font-weight: 700; font-size: 14px; padding: 12px 24px; border-radius: 999px; display: inline-flex; align-items: center; gap: 8px; }

.btn-primary   { background: #C5FF02; color: #000000; border: none; }           /* Green fill */
.btn-secondary { background: transparent; color: #000000; border: 2px solid #000000; }  /* Outline */
.btn-dark      { background: #000000; color: #FFFFFF; border: none; }           /* Black fill */

/* Dark mode secondary */
.btn-secondary-dark { border-color: #FFFFFF; color: #FFFFFF; }

/* Chevron suffix */
.btn-chevron::after { content: ' »'; font-weight: 900; }
```

**Placement**: bottom of content column, left-aligned, side by side (~16px gap). Never centered, never stacked, never inside a box.  
**Pairing**: green + dark is the standard pair. Never two green buttons together.  
**Label**: sentence case, never all-caps.

---

## 9. KPI / Metric Circles

```css
.circle { width: 120px; height: 120px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Heebo', sans-serif; font-weight: 700; font-size: 28px; }
.circle-filled        { background: #C5FF02; color: #000000; }
.circle-outline-green { background: transparent; border: 3px solid #C5FF02; color: #000000; }
.circle-outline-black { background: transparent; border: 3px solid #000000; color: #000000; }
/* Dark mode outline: border #FFFFFF, color #FFFFFF */
```

---

## 10. Structural Elements

### Breadcrumb / section label
```
/ Apartado  en el que estés
```
- Font: Heebo Regular ~10–11px, muted gray
- "/ Apartado" in Heebo Bold, rest in Regular
- Top-left of every content slide

### Vertical separator line
- `#C5FF02`, 1px, full-height of content area
- Used in: map slides (divides map from panel), split content, table next to diagram

### Left border text accent
- `3px solid #C5FF02`, left side of text block
- Used in dark-panel body text to add visual anchor

### Wireframe orb (decorative)
- Always bottom-left, partial (never full circle)
- Opacity: 15–20%
- Light bg: `#CCCCCC` strokes / Dark bg: `#FFFFFF` strokes
- Reference as image/SVG asset — do not approximate in CSS
- May overlap adjacent photo or diagram edge decoratively

### Adobe Studio decorative elements (non-presentation UI)
Mesh orb: `radial-gradient(circle at 35% 35%, rgba(12,204,144,0.4) 0%, rgba(84,144,228,0.2) 40%, transparent 70%)`  
Dot grid: `radial-gradient(circle, rgba(12,204,144,0.3) 1px, transparent 1px)`, `background-size: 20px 20px`

---

## 11. Photography Rules

- Rectangular crop, no border-radius, no shadow, no frame
- Flush to slide edge on right/top/bottom
- Human-centered: people in real/lifestyle contexts preferred
- Editorial/dark tones work for both light and dark slides
- Collage: staggered layout, ~20px vertical offset, photos touch or overlap — never rigid grid

---

## 12. Strict Prohibitions

- ❌ "gut", "GUT", "Gut" anywhere in any artifact — use Globant · Adobe Studio
- ❌ All-caps text anywhere
- ❌ Libre Baskerville in body, bullets, labels, tables, or diagrams
- ❌ Line-height > 1.15
- ❌ Any color outside the defined system
- ❌ `#BFD732` as UI accent — logo chevron only
- ❌ `#C5FF02` on icons (standalone)
- ❌ Filled or illustrated icons — lineal only
- ❌ Centered layouts — always left-anchored (exception: full-width card grids may center within cards)
- ❌ Stacked buttons or centered buttons (outside card CTAs)
- ❌ Photos with border-radius or drop shadow
- ❌ 3D or gradient map landmasses
- ❌ Pie charts — use bars, circles, or funnels
- ❌ Omitting logo or confidentiality text on any slide
- ❌ Inventing colors, fonts, or components not in this file

## 13. Flag before producing
- Color outside defined system
- Font outside approved set
- Diagram type not listed in section 7
- Template variant not listed in section 5
- Any logo treatment other than Globant · Adobe Studio

---

## 14. Web & UI Design Principles (adapted from globant.com)

These principles complement the hard rules above. They govern composition, spacing, motion, and interaction for any web or digital artifact. **They never override the color, font, or logo rules** — they extend them into web/UI contexts.

### Layout & Grid
- **Base grid**: 12-column, 1440px max-width desktop · 4-column mobile
- **Outer margin**: 80px desktop · 24px mobile
- **Column gutter**: 24px
- **Section vertical rhythm**: 120px between major sections desktop · 64px mobile
- **Card internal padding**: 32px desktop · 20px mobile
- **Border-radius convention**: 0px (cards, images, hero blocks — sharp edges are a brand signature) · 8px max for interactive elements like buttons and inputs · 999px for pill CTAs only

### Spacing system (8px base unit)
```
4px   — micro (icon gap, badge padding)
8px   — xs (tight inline spacing)
16px  — sm (component internal)
24px  — md (between related elements)
32px  — lg (between components)
48px  — xl (section sub-blocks)
64px  — 2xl (section padding mobile)
80px  — 3xl (section padding desktop)
120px — 4xl (major section breaks)
```

### Typography — web scale (Plus Jakarta Sans)
| Token | Size | Weight | Line height | Use |
|---|---|---|---|---|
| display-xl | 72px | 800 | 1.05 | Hero headline |
| display-lg | 56px | 800 | 1.1 | Section hero |
| h1 | 48px | 700 | 1.1 | Page title |
| h2 | 36px | 700 | 1.15 | Section title |
| h3 | 24px | 600 | 1.2 | Card title |
| h4 | 20px | 600 | 1.3 | Sub-section label |
| body-lg | 18px | 400 | 1.6 | Lead paragraph |
| body | 16px | 400 | 1.6 | Standard body |
| body-sm | 14px | 400 | 1.5 | Secondary text, captions |
| label | 12px | 600 | 1.4 | Tags, labels, nav items |
| micro | 11px | 400 | 1.4 | Legal, footnotes |

### Color application — web UI
Following globant.com visual language:
- **Backgrounds**: black or white — no gray intermediates as primary bg
- **Hero sections**: alternate light and dark sections as you scroll — high contrast rhythm
- **`#C5FF02` usage on web**: sparingly — CTA buttons, hover states, active indicators, key metric callouts. Never as a background color for large areas
- **Text on `#C5FF02`**: always `#000000`
- **Link color**: `#000000` (light bg) / `#FFFFFF` (dark bg) — underline on hover only
- **Hover states**: `#C5FF02` highlight or opacity shift (0.7) — no color change on text

### Motion & Interaction
- **Entrance animation**: fade + translateY(24px) → translateY(0), duration 400ms, ease-out-expo
- **Hover on cards**: subtle scale(1.02) or border-color shift to `#C5FF02`, 200ms ease
- **Button hover**: opacity 0.85 on filled · background `rgba(197,255,2,0.1)` on outline, 150ms
- **Page transitions**: fade, 300ms — no slide animations
- **Never**: bounce, elastic, or decorative spin animations — brand is precise, not playful

### Hero sections (web)
Following globant.com pattern:
- Full-viewport height or ~80vh
- Large display typography (display-xl or display-lg), left-aligned or centered
- Background: dark (`#000000`) with video/image overlay OR light (`#FFFFFF`) clean
- Single primary CTA button (pill, `#C5FF02`)
- Subtle background visual: mesh orb, dot pattern, or abstract gradient — never photographic unless intentional editorial shot
- Logo always top-left in web nav (unlike slides where it's top-right)

### Navigation (web)
- Top nav: `#FFFFFF` bg with border-bottom `rgba(0,0,0,0.08)` · sticky on scroll
- Nav logo: top-left (Globant logotipo, light version on white bg)
- Nav links: Heebo/Plus Jakarta Sans SemiBold 14px, `#000000`
- Primary CTA in nav: pill button, `#000000` fill + `#FFFFFF` text (or `#C5FF02` on dark nav)
- Mobile: hamburger menu, full-screen overlay dark bg

### Cards — web
```css
.card-web {
  background: var(--bg);
  border: 1px solid rgba(0,0,0,0.08); /* light mode */
  border-radius: 0; /* sharp — brand signature */
  padding: 32px;
  transition: border-color 0.2s ease;
}
.card-web:hover { border-color: #C5FF02; }
/* Dark mode: border: 1px solid rgba(255,255,255,0.1) */
```

### Accessibility minimums
- Text contrast: ≥ 4.5:1 body · ≥ 3:1 large text (WCAG AA)
- Focus rings: `outline: 2px solid #C5FF02; outline-offset: 2px`
- Font size: body ≥ 16px, labels ≥ 12px
- Interactive targets: ≥ 44×44px
- Never convey information through color alone

### What globant.com does that adapts to artifacts
- **Sharp edges everywhere** — no rounded cards, no soft UI. Precision is the visual voice
- **High contrast alternation** — dark/light sections in rhythm, never 3 same-mode sections in a row
- **Generous whitespace** — content breathes, never dense or cluttered
- **Type does the heavy lifting** — large, bold headlines carry the visual weight, not decoration
- **`#C5FF02` is punctuation, not wallpaper** — it appears in moments: one CTA, one highlight, one active state. Overuse destroys its impact
- **No decorative gradients** on solid surfaces — gradients only in the mesh orb or background overlays
- **Photography is editorial** — humans in context, never stock-generic, never smiling at cameras in suits
