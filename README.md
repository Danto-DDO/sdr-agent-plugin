# sdr-agent — plugin de Claude Code

Genera documentos **SDR (Solution Design Reference)** de analytics en **HTML y PDF**, con branding Globant Adobe Studio, y los valida automáticamente. Migrado desde la skill de Cowork.

## Estructura

```
sdr-agent-plugin/                 ← raíz del repo (plugin + marketplace de 1 plugin)
├── .claude-plugin/
│   ├── plugin.json               ← manifiesto del plugin
│   └── marketplace.json          ← manifiesto del marketplace
├── skills/
│   └── sdr-agent/                ← la skill (auto-descubierta desde skills/)
│       ├── SKILL.md
│       ├── assets/               ← template HTML + logos
│       ├── references/           ← guías de marca y UI
│       └── scripts/              ← validate_sdr.py (QA) + html_to_pdf.py (HTML→PDF)
└── README.md
```

Las skills se **auto-descubren** desde `skills/`; no hay que declararlas en `plugin.json`.

## Instalación (equipo)

1. Sube esta carpeta (`sdr-agent-plugin/`) a un repo Git (GitHub/GitLab).
2. Cada persona del equipo, dentro de Claude Code:

   ```
   /plugin marketplace add <owner>/<repo>
   /plugin install sdr-agent@omni-analytics
   ```

   (`<owner>/<repo>` también admite la URL completa o una ruta local `./ruta/al/repo`.)

3. La skill queda disponible con namespace: `sdr-agent:sdr-agent`.

## Uso local (sin repo)

Para probarla sin publicar, copia `skills/sdr-agent/` a `~/.claude/skills/sdr-agent/`
(nivel usuario) o a `.claude/skills/` dentro de un proyecto.

## Notas de migración desde Cowork

- El **Modo 2** (lectura del dataLayer en vivo) requiere un MCP de navegador
  (p. ej. Playwright) conectado en Claude Code. Sin él, usa Modo 1 o Modo 3.
- El validador `scripts/validate_sdr.py` es Python stdlib puro; corre con
  `python3 scripts/validate_sdr.py <archivo.html>`.
- El PDF se genera desde el HTML con `python3 scripts/html_to_pdf.py <archivo.html>`.
  Requiere **WeasyPrint** (`pip install weasyprint`); si no está, usa Chrome/Chromium
  headless. El entregable final son ambos archivos: `.html` (fuente) y `.pdf` (para compartir).
- Los Modos 1 (entrevista) y 3 (actualización de un SDR previo) funcionan sin
  herramientas extra.

## Instalar el motor de PDF (WeasyPrint)

WeasyPrint necesita las librerías de sistema de Pango. Comandos por SO
(verificados con WeasyPrint 69):

**Ubuntu ≥ 20.04**
```bash
sudo apt install python3-pip libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 libharfbuzz-subset0
pip install weasyprint
```

**Debian ≥ 11**
```bash
sudo apt install python3-pip libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0
pip install weasyprint
```

**Fedora ≥ 39**
```bash
sudo dnf install python3-pip pango
pip install weasyprint
```

**macOS** (Homebrew)
```bash
brew install weasyprint
```

**Windows** — la vía más simple es **no instalar WeasyPrint** y dejar que
`html_to_pdf.py` use Google Chrome / Edge (ya lo detecta automáticamente).
Si aun así quieres WeasyPrint: instala [MSYS2](https://www.msys2.org/), ejecuta
`pacman -S mingw-w64-x86_64-pango` y luego `python -m pip install weasyprint`.

Verifica la instalación con `weasyprint --info`. Si aparece "cannot load
library", falta alguna lib de Pango del listado de arriba.

