#!/bin/bash
py -3.11 -m venv venv
source venv/bin/activate
py -m pip install -r requirements.txt
echo "Setup completato! Modifica .env con i tuoi path."