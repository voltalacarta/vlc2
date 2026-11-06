---
titolo: "voltalacarta.it (nuovo sito)"
stato: attivo
creato: 2026-11-06
aggiornato: 2026-11-06
tag: [progetto]
sintesi: "Nuovo sito di Volta la carta: catalogo dei libri, pubblicare con noi, legatoria e negozio, con ordini per email."
---

# voltalacarta.it (nuovo sito)

Nuovo sito di Volta la carta: casa editrice, legatoria e negozio in via Voltapaletto 25 a Ferrara. Separato da [rilegaretesi.it](https://github.com/voltalacarta/rt2) e collegato.

## Dove trovare cosa

| Cosa | Dove |
| --- | --- |
| Documentazione del progetto | [`docs/`](docs/README.md) |
| Decisioni del progetto | [`docs/decisioni/`](docs/decisioni/README.md) |
| Mappa compatta di tutti i file (anche per Claude) | `INDICE.md`, generato da solo |
| Regole generali di Volta la carta | [documentazione](https://github.com/voltalacarta/documentazione) |

## Il sito

| Cosa | Dove |
| --- | --- |
| Pagine | `src/pages/*.html`, modelli Jinja che estendono `src/templates/base.html` |
| Scheda di ogni libro | `src/templates/libro.html`, una pagina per ISBN in `dist/libri/` |
| Catalogo dei libri | `src/data/libri.csv` |
| Collane, negozio, dati della bottega | `src/data/*.json` |
| Generatore | `strumenti/build.py` |

## Come si lavora

- Apri la repo in un Codespace: *Code* → *Codespaces* → *Create codespace on main*.
- Una decisione nuova: `python3 strumenti/nuova-decisione.py "Titolo"`, poi compila il file.
- Ogni push su `main` pubblica il sito di prova su GitHub Pages. Il sito attuale voltalacarta.it non viene toccato.
