import os
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

leads_db = [
    {"id": 1, "zona": "laferrere", "rubro": "albañileria", "detalle": "Pared 15m", "contacto": "wa.me/5491135101508"},
    {"id": 2, "zona": "catan", "rubro": "ventas", "detalle": "Vendedor materiales", "contacto": "fb.com/456"},
    {"id": 3, "zona": "san-justo", "rubro": "seguridad", "detalle": "Camaras obra", "contacto": "fb.com/789"}
]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/buscar')
def buscar():
    z = request.args.get('zona', '').lower()
    r = request.args.get('rubro', '').lower()
    res = [l for l in leads_db if l['zona'] == z and l['rubro'] == r]
    return jsonify(res)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
