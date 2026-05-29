# TIrocinio

Repository per il progetto di tirocinio presso l'università degli studi di Milano

# Requirements:

- Ollama (installato e in esecuzione)
- Python 3.11

# Installazione e setup

1) Clona il repository
2) Installa Ollama da https://ollama.com/download
3) esegui lo script di setup: esso crea un ambiente virtuale, lo attiva e installa tutte le dipendenze da requirements.txt

# Configurazione:
modifica config.py per impostare i percorsi corretti sulla tua macchina:
IMAGE_PATH = Path di una singola immagine (testing)
CARTELLA_IMMAGINI = Path della cartella con le immagini da analizzare
FILE_EXCEL        = Path di output di analisiDisegni.py (lo crea automaticamente se non esiste, dare nome appopriato)
TABELLA_PSICOLOGA = Path della tabella della psicologa (../TabellaPsicologi/tabellaPsicologa.xlsx)
TABELLA_CONFRONTO = Path della tabella da analizzare 
MATRICE_CONFUSIONE = Path di output di confusionMatrix.py (lo crea automaticamente se non esiste, dare nome appropriato)

modifica analisiDisegni.py per scegliere il modello di analisi:
MODELLO : "nome del modello preso da Ollama"
ricordare sempre di fare Ollama pull nomeModello su terminale

# Utilizzo:
python analisiDisegni.py:

il programma legge tutti i file .tif della cartella CARTELLA_IMMAGINE
invia ogni immagine al modello scelto
classifica il disegno secondo i criteri definiti
salva i risultati riga per riga su file excel
riprende automaticamente da dove si è interrotto in caso di crash

python confusionMatrix.py:

il programma legge le due tabelle su cui fare il confronto
genera una matrice di confusione e le metriche per ogni colonna
evidenzia i dati mancanti nel foglio finale
salva i risultati su file excel