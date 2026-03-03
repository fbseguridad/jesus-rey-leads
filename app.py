from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
import os

app = Flask(__name__)

# Conexión ultra-segura a Firebase
try:
    if not firebase_admin._apps:
        # Buscamos la llave en la carpeta actual
        cred = credentials.Certificate('firebase-key.json')
        firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print(f"Error iniciando Firebase: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    zona = request.form.get('zona', '')
    rubro = request.form.get('rubro', '')

    try:
        leads_ref = db.collection('leads')
        # Traemos los últimos 20 para no saturar
        docs = leads_ref.order_by('fecha', direction=firestore.Query.DESCENDING).limit(20).stream()
        
        for doc in docs:
            item = doc.to_dict()
            # Filtro simple por texto
            if zona.lower() in item.get('zona', '').lower() and rubro.lower() in item.get('rubro', '').lower():
                resultados.append(item)
    except Exception as e:
        print(f"Error al consultar: {e}")

    return render_template('index.html', resultados=resultados, zona=zona, rubro=rubro)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
