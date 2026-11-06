#!/usr/bin/env python3
"""Genera il sito statico di voltalacarta.it in dist/.

    python3 strumenti/build.py            # staging (noindex)
    python3 strumenti/build.py --produzione

Pagine in src/pages/*.html (template Jinja che estendono src/templates/base.html),
una scheda per ogni libro in dist/libri/<isbn>.html,
dati in src/data/ (libri.csv, collane.json, bottega.json, negozio.json), file statici in src/assets/.
"""

from __future__ import annotations

import argparse
import base64
import csv
import json
import shutil
from pathlib import Path
from urllib.parse import quote

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup, escape

RADICE = Path(__file__).resolve().parent.parent
SRC = RADICE / "src"
DIST = RADICE / "dist"
ESCLUSI = ("non acquistabile",)  # note del catalogo che tolgono il libro dal sito


def euro(valore: float) -> str:
    """12 -> '12 €', 12.5 -> '12,50 €'."""
    if float(valore).is_integer():
        return f"{int(valore)} €"
    return f"{valore:.2f}".replace(".", ",") + " €"


def offusca(testo: str) -> str:
    """Rovescia e codifica in base64: chi legge l'HTML senza eseguire il codice non vede il recapito."""
    return base64.b64encode(testo[::-1].encode("utf-8")).decode("ascii")


def rivela(bottega: dict, tipo: str, etichetta: str = "", oggetto: str = "", testo: str = "", classe: str = "rivela") -> Markup:
    """Telefono o email nascosti ai robot: un pulsante li mostra al clic (assets/js/contatti.js).
    Con `oggetto` il clic apre direttamente l'email già compilata."""
    if tipo == "tel":
        valore, scritta = bottega["telefono"], etichetta or "mostra il numero"
    else:
        valore, scritta = bottega["email"], etichetta or "mostra l'email"
    extra = ""
    if oggetto:
        extra += f' data-oggetto="{escape(oggetto)}"'
    if testo:
        extra += f' data-testo="{escape(testo)}"'
    return Markup(
        f'<button type="button" class="{classe}" data-tipo="{tipo}" data-v="{offusca(valore)}"{extra}>{escape(scritta)}</button>'
    )


def carica_libri(collane: list[dict]) -> list[dict]:
    per_nome = {c["nome"]: c for c in collane}
    libri = []
    with open(SRC / "data" / "libri.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            isbn = r["isbn"].strip()
            if not isbn or any(e in r["note"] for e in ESCLUSI):
                continue
            collana = per_nome.get(r["collana"].strip())
            libri.append({
                "isbn": isbn,
                "titolo": r["titolo"].strip(),
                "autori": "" if r["autori"].strip() in ("", "n.d.") else r["autori"].strip(),
                "anno": "" if r["anno"].strip() in ("", "n.d.") else r["anno"].strip(),
                "prezzo": float(r["prezzo_eur"]) if r["prezzo_eur"].strip() else None,
                "collana": collana,
                "gratuito": "download gratuito" in r["note"],
            })
    libri.sort(key=lambda b: (b["anno"] or "0000", b["titolo"]), reverse=True)
    return libri


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--produzione", action="store_true")
    a = ap.parse_args()

    leggi = lambda n: json.loads((SRC / "data" / n).read_text(encoding="utf-8"))  # noqa: E731
    bottega, collane, negozio = leggi("bottega.json"), leggi("collane.json"), leggi("negozio.json")
    for i, c in enumerate(collane):  # una tinta per collana, per le copertine disegnate
        c["tinta"] = [165, 15, 215, 35, 340, 275, 190, 95, 0, 45][i % 10]
    libri = carica_libri(collane)
    for c in collane:
        c["libri"] = [b for b in libri if b["collana"] is c]
    dati = {"bottega": bottega, "collane": collane, "negozio": negozio, "libri": libri,
            "anni": sorted({b["anno"] for b in libri if b["anno"]})}

    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(SRC / "assets", DIST / "assets")

    env = Environment(
        loader=FileSystemLoader([SRC / "templates", SRC / "pages"]),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["euro"] = euro
    env.filters["url"] = lambda s: quote(s, safe="")
    env.globals["rivela"] = lambda tipo, etichetta="", oggetto="", testo="", classe="rivela": rivela(bottega, tipo, etichetta, oggetto, testo, classe)
    contesto = {"dati": dati, "staging": not a.produzione}

    n = 0
    for pagina in sorted((SRC / "pages").glob("*.html")):
        html = env.get_template(pagina.name).render(pagina=pagina.stem, radice="", **contesto)
        (DIST / pagina.name).write_text(html, encoding="utf-8")
        n += 1
    (DIST / "libri").mkdir()
    scheda = env.get_template("libro.html")
    for b in libri:
        html = scheda.render(pagina="libro", radice="../", libro=b, **contesto)
        (DIST / "libri" / f"{b['isbn']}.html").write_text(html, encoding="utf-8")

    robots = "User-agent: *\nDisallow: /\n" if contesto["staging"] else "User-agent: *\nAllow: /\n"
    (DIST / "robots.txt").write_text(robots, encoding="utf-8")
    (DIST / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Sito generato in {DIST} ({n} pagine e {len(libri)} schede di libri)")


if __name__ == "__main__":
    main()
