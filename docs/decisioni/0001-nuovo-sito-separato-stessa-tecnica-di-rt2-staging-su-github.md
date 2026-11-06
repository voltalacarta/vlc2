---
titolo: Nuovo sito separato, stessa tecnica di rt2, staging su GitHub Pages
stato: accettato
creato: 2026-11-06
aggiornato: 2026-11-06
tag: [decisioni, sito, tecnica]
sintesi: voltalacarta.it rifatto a parte con pagine HTML generate da Python, come rilegaretesi.it; prova su GitHub Pages, sito attuale intatto.
---

# 0001 · Nuovo sito separato, stessa tecnica di rt2, staging su GitHub Pages

## Contesto

Il titolare ha scelto siti separati e collegati per le tesi e per Volta la carta (decisione D12 della Mappa delle scelte) e nessun costo fisso al lancio (D15). rilegaretesi.it si sta già rifacendo in `voltalacarta/rt2` con pagine HTML generate da Python.

## Decisione

- voltalacarta.it si rifà in questa repo con la stessa tecnica di rt2: modelli Jinja, dati in file, generatore `strumenti/build.py`.
- Il sito di prova si pubblica su GitHub Pages a ogni push, con `noindex`. Il sito attuale non si tocca fino al passaggio.
- Il catalogo dei libri parte dalla copia del second brain (`info-pubbliche/dati/catalogo.csv`, ottobre 2026).

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Ripulire il WordPress attuale | Scartato per entrambi i siti nella decisione 0009 di documentazione |
| Un unico sito con le tesi | Il titolare vuole siti separati e collegati (D12) |

## Conseguenze

- ✅ Stessi strumenti e stesse regole di rt2: chi conosce uno sa lavorare sull'altro.
- ✅ Una scheda per ogni libro con ISBN, leggibile da Google e dagli assistenti AI.
- ⚠️ Il catalogo va verificato con il titolare: alcuni titoli risultano nei cataloghi online ma non sul sito attuale.
