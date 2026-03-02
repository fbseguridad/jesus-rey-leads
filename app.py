from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
import os

app = Flask(__name__)

# Conectar a Firebase usando la llave que acabamos de subir
if not firebase_admin._apps:
    cred = credentials.Certificate('firebase-key.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/', methods=['GET', 'POST'])
def index():
    zona = ""
    rubro = ""
    resultados = []

    if request.method == 'POST':
        zona = request.form.get('zona', '').strip().lower()
        rubro = request.form.get('rubro', '').strip().lower()

        # Buscamos en la colección 'leads' de Firebase
        leads_ref = db.collection('leads')
        docs = leads_ref.stream()

        for doc in docs:
            lead = doc.to_dict()
            l_zona = lead.get('zona', '').lower()
            l_rubro = lead.get('rubro', '').lower()
            
            # Si el usuario busca algo, filtramos; si no, mostramos todo
            if (not zona or zona in l_zona) and (not rubro or rubro in l_rubro):
                resultados.append(lead)

    return render_template('index.html', resultados=resultados, zona=zona, rubro=rubro)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
