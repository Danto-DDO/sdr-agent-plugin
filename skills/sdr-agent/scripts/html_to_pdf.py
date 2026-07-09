#!/usr/bin/env python3
"""
html_to_pdf.py — Convierte un SDR en HTML a PDF preservando el branding.

El PDF se genera a partir del HTML ya branddeado, asi que hereda todos los
lineamientos visuales (colores, logo, tablas, badges) sin reimplementarlos.
El template incluye reglas @page / @media print para saltos de pagina limpios.

Uso:
    python3 html_to_pdf.py <sdr.html> [salida.pdf]

Si no se indica salida, usa el mismo nombre con extension .pdf.

Motores (en orden de preferencia):
  1. WeasyPrint  (recomendado)  ->  pip install weasyprint
  2. Chrome/Chromium/Edge headless (--print-to-pdf) si esta instalado

Exit code 0 si genero el PDF, 1 si fallo.
"""

import os
import shutil
import subprocess
import sys


def out_path(html_path, given):
    if given:
        return given
    base, _ = os.path.splitext(html_path)
    return base + ".pdf"


def try_weasyprint(html_path, pdf_path):
    try:
        from weasyprint import HTML
    except Exception as e:  # noqa: BLE001 — puede fallar por ImportError o por
        # librerias nativas ausentes (GTK/Pango/Cairo), muy comun en Windows.
        # En cualquier caso, no debe tumbar el script: hay que caer a Chrome.
        return False, "weasyprint no disponible: %s" % e
    try:
        HTML(filename=html_path).write_pdf(pdf_path)
        return True, "weasyprint"
    except Exception as e:  # noqa: BLE001
        return False, "weasyprint fallo: %s" % e


def find_chrome():
    for name in ("google-chrome", "google-chrome-stable", "chromium",
                 "chromium-browser", "chrome", "microsoft-edge"):
        p = shutil.which(name)
        if p:
            return p
    # rutas comunes (macOS / Windows)
    for p in (
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ):
        if os.path.exists(p):
            return p
    return None


def try_chrome(html_path, pdf_path):
    chrome = find_chrome()
    if not chrome:
        return False, "no se encontro Chrome/Chromium/Edge"
    url = "file://" + os.path.abspath(html_path)
    cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           "--print-to-pdf=" + os.path.abspath(pdf_path), url]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=120)
    except Exception:
        cmd[1] = "--headless"  # navegadores mas viejos
        try:
            r = subprocess.run(cmd, capture_output=True, timeout=120)
        except Exception as e:  # noqa: BLE001
            return False, "chrome fallo: %s" % e
    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
        return True, "chrome headless"
    return False, "chrome no genero PDF (%s)" % (r.stderr.decode(errors="ignore")[:200])


def main(argv):
    if len(argv) < 2:
        print("Uso: python3 html_to_pdf.py <sdr.html> [salida.pdf]")
        return 2
    html_path = argv[1]
    if not os.path.exists(html_path):
        print("No existe el HTML: %s" % html_path)
        return 1
    pdf_path = out_path(html_path, argv[2] if len(argv) > 2 else None)

    errors = []
    for backend in (try_weasyprint, try_chrome):
        ok, info = backend(html_path, pdf_path)
        if ok:
            print("PDF generado con %s: %s (%d bytes)"
                  % (info, pdf_path, os.path.getsize(pdf_path)))
            return 0
        errors.append(info)

    print("No se pudo generar el PDF. Detalles:")
    for e in errors:
        print("  - %s" % e)
    print("\nInstala un motor:  pip install weasyprint   "
          "(o instala Google Chrome / Chromium).")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
