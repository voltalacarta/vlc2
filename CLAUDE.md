# Claude · regole di questa repo

Nuovo voltalacarta.it: casa editrice, legatoria e negozio. Progetto di voltalacarta; regole generali in `voltalacarta/documentazione`, scelte del titolare nel second brain (`scelte-titolare-2026-11`).

## Spendere pochi token

1. Orientati con `INDICE.md` (una riga per file) o `grep -i "parola" INDICE.md`. Apri solo i file che servono.
2. Non aggiornare a mano indici e tabelle tra i marcatori `<!-- indice:… -->`: lo fa l'Action dopo il push.
3. Clone superficiale: `git clone --depth 1`.

## Regole del sito

- Si dà del **lei** (casa editrice ed enti). Le tesi stanno su rilegaretesi.it, che dà del tu.
- **Niente carrello**: libri e oggetti si ordinano per email (decisione 0002).
- Telefono ed email mai in chiaro: si usa `rivela(...)` nei template.
- Fuori dall'Unione europea dazi e tasse sono a carico di chi riceve: va detto dove si parla di spedizioni.
- Catalogo dei libri in `src/data/libri.csv` (copia dal second brain), collane in `src/data/collane.json`.
- Anteprima: `python3 strumenti/build.py`, poi apri `dist/index.html` con un server locale.

## Regole della repo

- Ciò che si decide in chat → `python3 strumenti/nuova-decisione.py "Titolo" --tag … --sintesi "…"`, poi compila il file.
- Documenti in `docs/`, con frontmatter `titolo`, `stato`, `creato`, `aggiornato`, `tag` (e `sintesi` in una riga).
- Prima del commit: `python3 strumenti/controlla.py`. Messaggi di commit `tipo(ambito): descrizione`.
- Mai segreti o dati sensibili nella repo.
