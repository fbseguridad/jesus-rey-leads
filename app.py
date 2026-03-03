from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
import os

app = Flask(__name__)

# Conexión simple
if not firebase_admin._apps:
    cred = credentials.Certificate('firebase-key.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    if request.method == 'POST':
        zona = request.form.get('zona', '').lower()
        rubro = request.form.get('rubro', '').lower()
        
        try:
            # Traemos solo los últimos 10 para ahorrar memoria
            leads_ref = db.collection('leads')
            docs = leads_ref.order_by('fecha', direction=firestore.Query.DESCENDING).limit(10).stream()
            
            for doc in docs:
                item = doc.to_dict()
                if zona in item.get('zona', '').lower() and rubro in item.get('rubro', '').lower():
                    resultados.append(item)
        except Exception as e:
            print(f"Error: {e}")
            
    return render_template('index.html', resultados=resultados)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
