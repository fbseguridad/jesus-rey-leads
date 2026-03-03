import time
import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import requests
from bs4 import BeautifulSoup
import re

# Conexión a Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('firebase-key.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()

OFICIOS = ["Albañil", "Flete", "Pintor", "Electricista", "Plomero", "Gasista", "Herrero"]
ZONAS = ["Laferrere", "Casanova", "Castillo", "Gonzales Catan"]

def extraer_telefono(texto):
    patron = r'\b(?:\+?54\s?)?(?:9\s?)?(?:11|[23]\d{2,3})\s?\d{6,8}\b'
    resultado = re.findall(patron, texto)
    return resultado[0] if resultado else None

def caza_real_duck(oficio, zona):
    print(f"🕵️ Buscando {oficio} en {zona}...")
    
    # Usamos DuckDuckGo que no bloquea tanto como Google
    query = f'busco {oficio} {zona} urgente'
    url = f"https://html.duckduckgo.com/html/?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # DuckDuckGo usa la clase 'result__snippet' para el texto
        resultados = soup.find_all('a', class_='result__snippet')
        
        if not resultados:
            print(f"⚠️ No se encontraron resultados ahora para {oficio}")
            return

        for res in resultados:
            texto = res.get_text()
            tel = extraer_telefono(texto)
            
            data = {
                'zona': zona.capitalize(),
                'rubro': oficio.capitalize(),
                'descripcion': texto[:250],
                'contacto': f"wa.me/{tel}" if tel else "https://duckduckgo.com/?q=" + query.replace(" ", "+"),
                'fecha': datetime.datetime.now()
            }
            
            # Guardamos con ID único para no repetir avisos
            doc_id = f"{zona}_{oficio}_{hash(texto[:30])}"
            db.collection('leads').document(doc_id).set(data)
            print(f"✅ ¡ENCONTRADO! Guardado en la web.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🚀 ROBOT REPARADO INICIADO...")
    while True:
        for zona in ZONAS:
            for oficio in OFICIOS:
                caza_real_duck(oficio, zona)
                time.sleep(10) # Pausa para ser amigable
        print("😴 Ciclo completo. Esperando 15 minutos...")
        time.sleep(900)
