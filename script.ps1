Write-Host "Creazione ambiente virtuale..."
python -m venv venv

Write-Host "Attivazione venv..."
.\venv\Scripts\Activate.ps1

Write-Host "Installazione dipendenze..."
pip install -r requirements.txt

Write-Host "Setup completato!"