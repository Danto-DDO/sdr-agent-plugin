#!/usr/bin/env python3
"""
validate_sdr.py — QA del HTML generado por sdr-agent.

Valida un SDR (HTML) contra las reglas de calidad de SKILL.md y reporta
ERRORES (bloquean la entrega) y AVISOS (revisar antes de entregar).

Uso:
    python3 validate_sdr.py <ruta-al-sdr.html>

Salida: reporte legible + exit code 0 (sin errores) / 1 (con errores).
No tiene dependencias externas (solo stdlib).
"""

import re
import sys
import html

ALLOWED_TYPES = {"String", "Integer", "Double", "Boolean", "Array", "Object", "Date"}
SNAKE_RE = re.compile(r"^[a-z0-9]+(_[a-z0-9]+)*$")
GA4_STANDARD = {
    "view_item", "view_item_list", "select_item", "add_to_cart",
    "remove_from_cart", "view_cart", "begin_checkout", "add_payment_info",
    "add_shipping_info", "purchase", "refund", "add_to_wishlist",
    "view_promotion", "select_promotion", "search", "login", "sign_up",
}


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def main(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            doc = f.read()
    except OSError as e:
        print("No se pudo leer el archivo: %s" % e)
        return 1

    errors, warnings, info = [], [], []

    # 0. Ignorar comentarios HTML (scaffolding de ejemplo del template)
    doc = re.sub(r"<!--.*?-->", "", doc, flags=re.S)

    # 1. Placeholders sin reemplazar
    for ph in sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", doc))):
        errors.append("Placeholder sin reemplazar: %s" % ph)

    # 2. Tipos de dato
    types_found = re.findall(r'type-tag\s+type-([A-Za-z]+)', doc)
    for t in sorted({t for t in types_found if t.capitalize() not in ALLOWED_TYPES}):
        errors.append("Tipo de dato no permitido: '%s' (permitidos: %s)"
                      % (t, ", ".join(sorted(ALLOWED_TYPES))))

    # 3. Eventos
    name_iter = list(re.finditer(r'<span class="event-name">(.*?)</span>', doc, re.S))
    info.append("Eventos detectados: %d" % len(name_iter))
    info.append("Tipos de dato usados: %s" % (", ".join(sorted(set(types_found))) or "ninguno"))

    for i, m in enumerate(name_iter):
        raw_name = strip_tags(m.group(1))
        start = m.end()
        end = name_iter[i + 1].start() if i + 1 < len(name_iter) else len(doc)
        block = doc[start:end]
        label = raw_name or "(sin nombre)"
        if not raw_name:
            errors.append("Evento #%d sin nombre." % (i + 1))
        if not re.search(r'ev-(new|updated|existing)', block):
            errors.append("Evento '%s': falta badge de estado (Nuevo/Actualizado/Existente)." % label)
        trig = re.search(r'class="event-trigger".*?</strong>(.*?)</p>', block, re.S)
        if not trig or not strip_tags(trig.group(1)):
            errors.append("Evento '%s': trigger ausente o vacio." % label)
        if raw_name and not SNAKE_RE.match(raw_name):
            warnings.append("Evento '%s': nombre no esta en snake_case "
                            "(ok si es un evento EXISTENTE con su nombre real)." % label)

    # 4. GA4
    names = {strip_tags(m.group(1)) for m in name_iter}
    lowered = {n.lower(): n for n in names}
    for std in GA4_STANDARD:
        alt = std.replace("_", "")
        for ln, original in lowered.items():
            if ln.replace("_", "") == alt and original != std:
                warnings.append("Evento '%s' parece el estandar GA4 '%s' — considera renombrarlo." % (original, std))

    info.append("Checks manuales (no automatizables): defaults por atributo, "
                "atributos de funcionalidades especiales marcados, exactitud de los triggers.")

    print("=" * 60)
    print("QA SDR — %s" % path)
    print("=" * 60)
    for line in info:
        print("  · %s" % line)
    print()
    if errors:
        print("ERRORES (%d) — corregir antes de entregar:" % len(errors))
        for e in errors:
            print("  x %s" % e)
    else:
        print("ERRORES: 0 OK")
    print()
    if warnings:
        print("AVISOS (%d) — revisar:" % len(warnings))
        for w in warnings:
            print("  ! %s" % w)
    else:
        print("AVISOS: 0 OK")
    print()
    print("Veredicto: %s" % ("FAIL (hay errores)" if errors else "PASS"))
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 validate_sdr.py <ruta-al-sdr.html>")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
