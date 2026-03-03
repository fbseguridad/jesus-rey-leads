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

# Lista expandida de palabras clave
OFICIOS = ["Albañil", "Flete", "Pintor", "Electricista", "Plomero", "Gasista", "Herrero", "Techista", "Durlock"]
ZONAS = ["Laferrere", "Casanova", "Castillo", "Gonzales Catan", "Isidro Casanova"]

def extraer_telefono(texto):
    # Busca números que parezcan celulares de Argentina
    patron = r'\b(?:\+?54\s?)?(?:9\s?)?(?:11|[23]\d{2,3})\s?\d{6,8}\b'
    resultado = re.findall(patron, texto)
    return resultado[0] if resultado else None

def caza_profunda(oficio, zona):
    print(f"🛰️ Satélite sobre {zona} buscando {oficio}...")
    
    # Búsqueda optimizada para redes y clasificados
    query = f'"{oficio}" "{zona}" (busco OR necesito OR urgente OR presupuesto)'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        # Simulamos la entrada a Google/Bing/DuckDuckGo
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraemos los fragmentos de texto (Snippets) que Google muestra
        resultados = soup.find_all('div', class_='VwiC3b') # Clase común en Google
        
        for res in resultados:
            texto = res.get_text()
            tel = extraer_telefono(texto)
            
            # Si encontramos algo interesante, lo guardamos
            data = {
                'zona': zona,
                'rubro': oficio,
                'descripcion': texto[:200] + "...",
                'contacto': f"wa.me/{tel}" if tel else url,
                'fecha': datetime.datetime.now(),
                'es_directo': True if tel else False
            }
            
            # Guardar con ID único basado en el texto para no repetir
            doc_id = f"{zona}_{oficio}_{hash(texto[:50])}"
            db.collection('leads').document(doc_id).set(data)
            
        print(f"✅ Escaneo completado para {oficio}")
        
    except Exception as e:
        print(f"⚠️ Error en rastreo: {e}")

if __name__ == "__main__":
    while True:
        for zona in ZONAS:
            for oficio in OFICIOS:
                caza_profunda(oficio, zona)
                time.sleep(10) # Pausa de seguridad
        print("😴 Ciclo terminado. Durmiendo 20 min...")
        time.sleep(1200)
