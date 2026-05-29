# Tirocinio — Analisi Disegni Infantili

Repository per il progetto di tirocinio presso l'Università degli Studi di Milano.

---

## Requisiti

- [Ollama](https://ollama.com/download) installato e in esecuzione
- Python 3.11

---

## Installazione e setup

1. Clona il repository

2. Installa Ollama da [https://ollama.com/download](https://ollama.com/download)

3. Esegui lo script di setup:
   Lo script crea un ambiente virtuale, lo attiva e installa tutte le dipendenze da `requirements.txt`.

---

## Configurazione

### `config.py`

Modifica `config.py` per impostare i percorsi corretti sulla tua macchina:

| Variabile | Descrizione |
|---|---|
| `IMAGE_PATH` | Path di una singola immagine (per testing) |
| `CARTELLA_IMMAGINI` | Path della cartella con le immagini da analizzare |
| `FILE_EXCEL` | Output di `analisiDisegni.py` — creato automaticamente se non esiste |
| `TABELLA_PSICOLOGA` | Path della tabella della psicologa (es. `../TabellaPsicologi/tabellaPsicologa.xlsx`) |
| `TABELLA_CONFRONTO` | Path della tabella da confrontare |
| `MATRICE_CONFUSIONE` | Output di `confusionMatrix.py` — creato automaticamente se non esiste |

### `analisiDisegni.py`

Modifica la variabile `MODELLO` per scegliere il modello da usare:

```python
MODELLO = "nome_modello"  # nome del modello installato in Ollama
```

Ricordati di scaricare il modello prima di eseguire lo script:

```bash
ollama pull nome_modello
```

---

## Utilizzo

### `analisiDisegni.py`

```bash
python analisiDisegni.py
```

- Legge tutti i file `.tif` dalla cartella `CARTELLA_IMMAGINI`
- Invia ogni immagine al modello scelto
- Classifica il disegno secondo i criteri definiti
- Salva i risultati riga per riga su file Excel
- Riprende automaticamente da dove si era interrotto in caso di crash

### `confusionMatrix.py`

```bash
python confusionMatrix.py
```

- Legge le due tabelle su cui fare il confronto
- Genera una matrice di confusione e le metriche (precision, recall, accuracy) per ogni colonna
- Evidenzia i dati mancanti in un foglio dedicato
- Salva i risultati su file Excel