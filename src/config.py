# src/config.py
from pathlib import Path
# Root del progetto (funziona su qualsiasi macchina)
PROJECT_ROOT = Path(__file__).parent.parent

# Cartelle standard
DATA_DIR     = PROJECT_ROOT / "data"
OUTPUT_DIR   = PROJECT_ROOT / "output"

# Path configurabili via .env (per file fuori dal progetto)
IMAGE_PATH = Path("directorySingolaImmagine")
CARTELLA_IMMAGINI = Path("DirectoryCartellaImmagini")
FILE_EXCEL        = Path("directoryFileExcel")