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
    model="ministral-3:3b",   
    temperature=0,
)

SYSTEM_PROMPT = """Sei un analista esperto di disegni infantili in ambito sanitario.
Il tuo compito è analizzare disegni fatti da bambini che hanno ricevuto educazione su:
- alimentazione sana (cibi sani vs batteri/cibi non sani)
- igiene orale (denti, spazzolino, carie)
- attività fisica vs sedentarietà

REGOLA FONDAMENTALE: per ogni campo devi scegliere SOLO uno dei valori esatti indicati.
Non inventare valori nuovi. Se non sei sicuro, scegli il valore più vicino tra quelli disponibili.
Non usare null, N/A o altri placeholder — scegli sempre un valore valido.

Devi rispondere ESCLUSIVAMENTE con un oggetto JSON valido, senza testo aggiuntivo, 
senza markdown, senza backtick. Solo JSON puro.
Esempio valido:

{
  "tipologia": "+",
  "dimensione": "N",
  "colore": "R-L",
  "posizione": "C",
  "orientamento": "S",
  "accuratezza": "A-ND",
  "alim": true,
  "io": true,
  "sport": false,
  "assoc": "NONE"
}

NOTA:
"NONE" è valido SOLO per assoc.

"""

USER_PROMPT = """
Restituisci SOLO JSON valido.
Regole IMPORTANTI:
- tipologia può essere SOLO "+", "-", "+-"
- assoc può essere SOLO "++", "--", "NONE"
- NON usare mai "NONE" in tipologia
- NON inventare valori

Schema:

{
  "tipologia": "+ | - | +-",
  "dimensione": "L | S | N | SL",
  "colore": "R-D | R-L | NR-D | NR-L",
  "posizione": "C | P-L | P-LT | P-LB | P-R | P-RT | P-RB",
  "orientamento": "S | U | D",
  "accuratezza": "A-D | NA-D | A-ND | NA-ND",
  "alim": true/false,
  "io": true/false,
  "sport": true/false,
  "assoc": "++ | -- | NONE"
}


Legenda valori:
- tipologia: "+" elementi positivi (cibo sano, dente sano), "-" elementi negativi (batteri, cibo cattivo), "+-" misti
- dimensione: L grande, S piccola, N normale, SL sproporzione tra elementi
- colore: R-D uso realistico del colore e colori scuri (es grigio, nero), R-L realistico chiaro, NR-D non realistico scuro, NR-L non realistico chiaro
- posizione: posizione prevalente degli elementi nel foglio (C centro, P–L = periferic left, a sinistra del foglio, P–LT = periferic left top, a sinistra in alto del foglio, P–LB = periferic left bottom, a sinistra in basso del foglio, P–R = periferic right, a destra del foglio, P–RT = periferic right top, a destra in alto del foglio, P–RB = periferic right bottom, a destra in basso del foglio)
- orientamento: S dritto, U sottosopra, D distorto
- accuratezza: A-D accurato e dettagliato, NA-D non accurato ma dettagliato, A-ND accurato non dettagliato, NA-ND non accurato non dettagliato
- alim: true se ci sono alimenti nel disegno
- io: true se ci sono denti o strumenti per igiene orale
- sport: true se c'è attività fisica o televisione/sedentarietà
- assoc: Associazione fra gli elementi presenti nel disegno (es. cibi sani e dente felice; oppure dente cariato e batteri, ecc.); se sì mettere associazione corretta o non forte e non evidente ++, --, NONE se non c'è nessuna associazione"""

msg = HumanMessage(content=[
    {"type": "text",      "text": USER_PROMPT},
    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}
])

response = llm.invoke([SystemMessage(content=SYSTEM_PROMPT),msg])
print((response.content))
