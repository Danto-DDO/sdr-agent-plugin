# Slide Patterns Reference
## Globant Adobe Studio — Presentation Templates

Load this file when creating PPTX, Google Slides, or HTML slide decks.
Always load alongside `adobe-studio-brand.md`.

---

## Slide Types

### 1. Cover Slide (Dark mode)
**Purpose**: Opening slide of any proposal or presentation.

**Structure**:
- Background: `#021325` full bleed
- Decorative orb: bottom-left, 40% slide height, teal wireframe mesh
- Client name: center, Plus Jakarta Sans 800, 72pt, white
- Subtitle (engagement type): center below, 800, 48pt, white
- "Globant Proposal" or context label: center, 400, 32pt, white 70% opacity
- Top-left: Globant logo white
- Top-right: Month + Year, 400, 18pt, white 70%
- Bottom footer: standard (see footer pattern)

### 2. Section Divider Slide (Dark mode)
**Purpose**: Transition between major sections.

**Structure**:
- Background: `#021325`
- Section number: large, faint, top-right, white 8% opacity (decorative)
- Section title: center-left, 800, 56pt, white
- Brief descriptor: below title, 300, 24pt, white 60%
- Teal accent line: 4px horizontal, below title, width 80px

### 3. Content Slide — Standard (Light mode)
**Purpose**: Main content delivery — frameworks, process, analysis.

**Structure**:
- Background: `#FFFFFF`
- Navigation tabs: top-right, pill buttons (see brand reference)
- Slide title: top-left, 800, 36pt, `#0A1628`
- Subtitle: below title, 400, 16pt, `#3D5166`
- Content area: flexible — cards, columns, diagrams
- Right edge: subtle dot grid or gradient accent
- Footer: standard

### 4. Content Slide — Tiered Cards (Light mode)
**Purpose**: Showing 2-3 levels, complexity tiers, maturity models.

**Card structure** (3 levels):
```
[●1] [Card content ─────────────────────]    [Side callout box]
     Title: SemiBold 16pt                     ┌ - - - - - - - ┐
     Bullets: Regular 13pt                    │ Bold label:   │
                                              │ Body text 13pt│
[●2] [Card content ─────────────────────]    └ - - - - - - - ┘
     (medium blue background)

[●3] [Card content ─────────────────────]
     (teal background)
```

**Number circle colors**:
- Level 1: `#A8C0FC` background, white text
- Level 2: `#5490E4` background, white text  
- Level 3: `#0CCC90` background, white text

**Card backgrounds** (match level):
- Level 1: `rgba(168,192,252,0.15)` with `#A8C0FC` left border
- Level 2: `rgba(84,144,228,0.15)` with `#5490E4` left border
- Level 3: `rgba(12,204,144,0.15)` with `#0CCC90` left border

**Side callout box**: dashed border `#0A1628`, white background, right-floated

### 5. Content Slide — Two Columns (Light mode)
**Purpose**: Before/after, comparison, problem/solution.

**Structure**:
- Left column (60%): main argument or content
- Right column (40%): supporting data, callout, or visual
- Vertical separator: 1px `#E2EAF0`

### 6. Team / People Slide (Light mode)
**Purpose**: Introduce delivery team, org structure.

**Structure**:
- Role cards: photo circle + name (Bold) + title (Regular) + Adobe certifications
- Grid: 4-6 per row
- Certification badges: small pill labels in `#5490E4` or `#0CCC90`

### 7. Timeline / Roadmap Slide (Light mode)
**Purpose**: Implementation phases, project milestones.

**Structure**:
- Horizontal timeline with phase markers
- Phase blocks: alternating `#A8C0FC` and `#5490E4`
- Milestone diamonds: `#0CCC90`
- Phase label: Bold 14pt above line
- Duration: Regular 12pt below line

---

## Footer Pattern (all slides)
```
[Globant Proprietary | Confidential information]    [N | Globant logo]
└── Regular 11pt, color: #6B8599 (dark) / #7A90A4 (light)
                                          └── Slide number + white logo
```

---

## Navigation Tab Pattern (content slides)
Tabs represent the deck's main sections. Active tab = current section.

Common tab sets:
- `Blueprint · Drivers · Use Cases · Execution · Scalability`
- `Overview · Architecture · Roadmap · Investment · Team`
- `Discovery · Design · Build · Launch · Scale`

Style: see nav-tab component in `adobe-studio-brand.md`

---

## PPTX-specific notes (when using python-pptx)
- Slide dimensions: 13.33" × 7.5" (widescreen 16:9)
- Always embed Plus Jakarta Sans or substitute Calibri as fallback (document this substitution)
- Use `RGBColor` for all brand colors — never rely on theme colors
- Images: insert logo PNG from `/mnt/skills/user/globant-brand/assets/` when available
- Text frames: set `word_wrap = True`, explicit font assignment per run
- Backgrounds: use `prs.slides[i].background.fill.solid()` with exact RGB

---

## Common mistakes to avoid
- ❌ Using blue on blue (accent-blue on blue background = unreadable)
- ❌ Mixing dark and light mode in same deck without intentional contrast logic
- ❌ Centering everything — Globant decks are left-anchored with deliberate white space
- ❌ Omitting the footer — every slide needs it
- ❌ Using placeholder gray icons instead of real content
- ❌ Forgetting navigation tabs on content slides in multi-section decks
