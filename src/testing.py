import base64
import io
from PIL import Image
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from config import IMAGE_PATH

def load_image_as_base64(path: str) -> str:
    with Image.open(path) as img:
        img = img.convert("RGB")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")

image_data = load_image_as_base64(IMAGE_PATH)

llm = ChatOllama(
    model="medgemma:4b",   
    temperature=0,
)

SYSTEM_PROMPT = """Sei un analista esperto di disegni infantili in ambito sanitario.
Il tuo compito è analizzare disegni fatti da bambini che hanno ricevuto educazione su:
- alimentazione sana (cibi sani vs batteri/cibi non sani)
- igiene orale (denti, spazzolino, carie)
- attività fisica vs sedentarietà

Devi rispondere ESCLUSIVAMENTE con un oggetto JSON valido, senza testo aggiuntivo, 
senza markdown, senza backtick. Solo JSON puro."""

USER_PROMPT = """Analizza questo disegno infantile e restituisci un oggetto JSON con esattamente questi campi:

{
  "tipologia": uno tra ["+", "-", "+-"],
  "dimensione": uno tra ["L", "S", "N", "SL"],
  "colore": uno tra ["R-D", "R-L", "NR-D", "NR-L"],
  "posizione": uno tra ["C", "P-L", "P-LT", "P-LB", "P-R", "P-RT", "P-RB"],
  "orientamento": uno tra ["S", "U", "D"],
  "accuratezza": uno tra ["A-D", "NA-D", "A-ND", "NA-ND"],
  "alim": true o false,
  "io": true o false,
  "sport": true o false,
  "assoc": uno tra ["++", "--", "=="],
}

Legenda valori:
- tipologia: + elementi positivi (cibo sano, dente sano), - elementi negativi (batteri, cibo cattivo), +- misti
- dimensione: L grande, S piccola, N normale, SL sproporzione tra elementi
- colore: R-D realistico scuro, R-L realistico chiaro, NR-D non realistico scuro, NR-L non realistico chiaro
- posizione: posizione prevalente degli elementi nel foglio (C centro, P-L sinistra, P-LT sinistra alto, P-LB sinistra basso, P-R destra, P-RT destra alto, P-RB destra basso)
- orientamento: S dritto, U sottosopra, D distorto
- accuratezza: A-D accurato e dettagliato, NA-D non accurato ma dettagliato, A-ND accurato non dettagliato, NA-ND non accurato non dettagliato
- alim: true se ci sono alimenti nel disegno
- io: true se ci sono denti o strumenti per igiene orale
- sport: true se c'è attività fisica o televisione/sedentarietà
- assoc: ++ se associazione corretta ed evidente (cibi sani e denti felici), -- se non corretta o non evidente (cibo sano ma denti cariati), == se assoc è false"""

msg = HumanMessage(content=[
    {"type": "text",      "text": USER_PROMPT},
    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}
])

response = llm.invoke([SystemMessage(content=SYSTEM_PROMPT),msg])
print((response.content))
