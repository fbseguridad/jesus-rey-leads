import json
import requests
import time
from googlesearch import search
from google.oauth2 import service_account
import google.auth.transport.requests

# CONFIGURACIÓN
PROJECT_ID = "loveplay-7b8cc"
KEY_FILE = "firebase-key.json"

def obtener_token():
    creds = service_account.Credentials.from_service_account_file(
        KEY_FILE, scopes=["https://www.googleapis.com/auth/datastore"]
    )
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    return creds.token

def guardar_en_firestore(zona, rubro, detalle, contacto):
    token = obtener_token()
    url = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/leads"
    
    data = {
        "fields": {
            "zona": {"stringValue": zona},
            "rubro": {"stringValue": rubro},
            "detalle": {"stringValue": detalle},
            "contacto": {"stringValue": contacto}
        }
    }
    
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post(url, json=data, headers=headers)
    if res.status_code == 200:
        print(f"✅ Guardado en la nube: {rubro} en {zona}")
    else:
        print(f"❌ Error al guardar: {res.text}")

def buscar_clientes():
    print("🚀 Robot rastreando pedidos...")
    queries = [
        'site:facebook.com "busco albañil" "laferrere"',
        'site:facebook.com "necesito flete" "matanza"'
    ]
    
    for q in queries:
        for link in search(q, num_results=2, lang="es"):
            rubro = "albanileria" if "albañil" in q else "fletes"
            guardar_en_firestore("laferrere", rubro, "Pedido encontrado en redes", link)

if __name__ == "__main__":
    while True:
        try:
            buscar_clientes()
        except Exception as e:
            print(f"⚠️ Error: {e}")
        print("Dormido 1 hora...")
        time.sleep(3600)
