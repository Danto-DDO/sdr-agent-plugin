# UI Components Reference
## Globant Adobe Studio — Web & Application Interfaces

Load this file when building React components, HTML pages, dashboards, or agent UIs.
Always load alongside `adobe-studio-brand.md`.

---

## Base Setup

```html
<!-- Font -->
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<!-- CSS root variables — choose one mode -->
```

### Dark Mode Root
```css
:root {
  --font-primary: 'Plus Jakarta Sans', sans-serif;
  --bg-primary:   #021325;
  --bg-secondary: #0C2430;
  --bg-elevated:  #0C3030;
  --text-primary: #FFFFFF;
  --text-secondary: #B0C4D4;
  --text-muted:   #6B8599;
  --accent-teal:  #0CCC90;
  --accent-blue:  #5490E4;
  --accent-blue-lt: #A8C0FC;
  --border:       rgba(255,255,255,0.08);
  --border-accent: rgba(12,204,144,0.3);
  --shadow:       0 4px 24px rgba(0,0,0,0.4);
}
```

### Light Mode Root
```css
:root {
  --font-primary: 'Plus Jakarta Sans', sans-serif;
  --bg-primary:   #FFFFFF;
  --bg-secondary: #F0F8FF;
  --bg-teal-wash: #E4F0F0;
  --text-primary: #0A1628;
  --text-secondary: #3D5166;
  --text-muted:   #7A90A4;
  --accent-blue:  #1E6FFF;
  --accent-teal:  #0CCC90;
  --accent-blue-lt: #5490E4;
  --accent-lavender: #A8C0FC;
  --border:       #E2EAF0;
  --border-accent: #0CCC90;
  --shadow:       0 2px 16px rgba(10,22,40,0.08);
  --gradient-hero: linear-gradient(135deg, #FFFFFF 0%, #E4F0F0 40%, #CCF0E4 70%, #B4F0F0 100%);
}
```

---

## Component Library

### Header / Nav Bar
```css
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 32px;
  background: var(--bg-primary);
  border-bottom: 1px solid var(--border);
}
.header-logo {
  height: 32px; /* standard logo height */
}
.header-nav {
  display: flex;
  gap: 8px;
}
```

### Pill Navigation Tabs
```css
.tab-group {
  display: flex;
  gap: 6px;
  background: var(--bg-secondary);
  padding: 4px;
  border-radius: 24px;
}
.tab {
  padding: 8px 20px;
  border-radius: 20px;
  font-family: var(--font-primary);
  font-weight: 600;
  font-size: 13px;
  border: none;
  cursor: pointer;
  color: var(--text-secondary);
  background: transparent;
  transition: all 0.2s ease;
}
.tab.active {
  background: var(--accent-blue);
  color: #FFFFFF;
}
.tab:hover:not(.active) {
  background: var(--border);
  color: var(--text-primary);
}
```

### Card — Standard
```css
.card {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 24px;
  font-family: var(--font-primary);
}
.card-title {
  font-weight: 700;
  font-size: 16px;
  color: var(--text-primary);
  margin-bottom: 8px;
}
.card-body {
  font-weight: 400;
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.6;
}
```

### Card — Tiered (Levels 1/2/3)
```css
.tier-card {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 12px;
}
.tier-1 { background: rgba(168,192,252,0.12); border-left: 4px solid #A8C0FC; }
.tier-2 { background: rgba(84,144,228,0.12);  border-left: 4px solid #5490E4; }
.tier-3 { background: rgba(12,204,144,0.12);  border-left: 4px solid #0CCC90; }

.tier-badge {
  width: 36px; height: 36px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: 16px; color: white;
  flex-shrink: 0;
}
.tier-1 .tier-badge { background: #A8C0FC; }
.tier-2 .tier-badge { background: #5490E4; }
.tier-3 .tier-badge { background: #0CCC90; }
```

### Stat / KPI Card
```css
.stat-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 24px;
  text-align: center;
}
.stat-value {
  font-weight: 800;
  font-size: 36px;
  color: var(--accent-teal);
  line-height: 1;
  margin-bottom: 6px;
}
.stat-label {
  font-weight: 500;
  font-size: 13px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
```

### Button — Primary
```css
.btn-primary {
  background: var(--accent-teal);
  color: #021325;
  padding: 12px 28px;
  border-radius: 8px;
  font-family: var(--font-primary);
  font-weight: 700;
  font-size: 14px;
  border: none;
  cursor: pointer;
  transition: opacity 0.2s;
}
.btn-primary:hover { opacity: 0.88; }
```

### Button — Secondary (outline)
```css
.btn-secondary {
  background: transparent;
  color: var(--accent-teal);
  padding: 11px 28px;
  border-radius: 8px;
  border: 1.5px solid var(--accent-teal);
  font-family: var(--font-primary);
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-secondary:hover {
  background: rgba(12,204,144,0.1);
}
```

### Badge / Tag
```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 12px;
  border-radius: 20px;
  font-weight: 600;
  font-size: 12px;
  gap: 6px;
}
.badge-blue  { background: rgba(84,144,228,0.15); color: #5490E4; }
.badge-teal  { background: rgba(12,204,144,0.15); color: #0CCC90; }
.badge-gray  { background: rgba(107,133,153,0.15); color: #6B8599; }
```

### Progress Bar
```css
.progress-track {
  height: 6px;
  background: var(--border);
  border-radius: 3px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-teal));
  border-radius: 3px;
  transition: width 0.4s ease;
}
```

### Table
```css
.data-table { width: 100%; border-collapse: collapse; font-family: var(--font-primary); }
.data-table th {
  font-weight: 600; font-size: 12px;
  color: var(--text-muted);
  text-transform: uppercase; letter-spacing: 0.06em;
  padding: 10px 16px;
  border-bottom: 1px solid var(--border);
  text-align: left;
}
.data-table td {
  padding: 14px 16px;
  font-size: 14px;
  color: var(--text-primary);
  border-bottom: 1px solid var(--border);
}
.data-table tr:hover td { background: var(--bg-secondary); }
```

### Dot Grid Decoration (SVG background)
```css
.dot-grid-bg {
  background-image: radial-gradient(circle, rgba(12,204,144,0.25) 1px, transparent 1px);
  background-size: 24px 24px;
}
/* Dark mode variant */
.dot-grid-bg-dark {
  background-image: radial-gradient(circle, rgba(164,192,252,0.2) 1px, transparent 1px);
  background-size: 20px 20px;
}
```

### Mesh Orb (CSS-only decorative element)
```css
.mesh-orb {
  width: 320px; height: 320px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%,
    rgba(12,204,144,0.4) 0%,
    rgba(84,144,228,0.2) 40%,
    transparent 70%
  );
  box-shadow:
    inset 0 0 60px rgba(12,204,144,0.15),
    0 0 80px rgba(12,204,144,0.1);
  /* Add SVG mesh overlay via ::after for full effect */
}
```

---

## Layout Grids

### Dashboard Grid
```css
.dashboard {
  display: grid;
  grid-template-columns: 240px 1fr;
  grid-template-rows: 64px 1fr;
  min-height: 100vh;
  background: var(--bg-primary);
}
.sidebar { grid-row: 1 / -1; border-right: 1px solid var(--border); }
.topbar  { grid-column: 2; border-bottom: 1px solid var(--border); }
.content { grid-column: 2; padding: 32px; overflow-y: auto; }
```

### Card Grid
```css
.card-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
.card-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}
```

---

## Animation Tokens
```css
--transition-fast:   0.15s ease;
--transition-base:   0.25s ease;
--transition-slow:   0.4s ease;
--ease-out-expo:     cubic-bezier(0.16, 1, 0.3, 1);
```

Standard entrance animation:
```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
.animate-in { animation: fadeUp 0.4s var(--ease-out-expo) both; }
```

---

## Accessibility minimums
- Text contrast: ≥ 4.5:1 for body, ≥ 3:1 for large text
- Focus rings: `outline: 2px solid var(--accent-teal); outline-offset: 2px;`
- Font size: body ≥ 14px, labels ≥ 12px
- Interactive targets: ≥ 44×44px
