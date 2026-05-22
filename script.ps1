Write-Host "Creazione ambiente virtuale..."
py -3.11 -m venv venv

Write-Host "Attivazione venv..."
.\venv\Scripts\Activate.ps1

Write-Host "Installazione dipendenze..."
py -m pip install -r requirements.txt

Write-Host "Setup completato!"