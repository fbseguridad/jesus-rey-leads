import os
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

# Base de datos de prueba (El robot la llenará automáticamente)
leads_db = [
    {"id": 1, "zona": "laferrere", "rubro": "albañileria", "detalle": "Busco albañil para pared de 15m", "contacto": "wa.me/5491135101508"},
    {"id": 2, "zona": "catan", "rubro": "ventas", "detalle": "Necesito vendedor de materiales", "contacto": "https://facebook.com/456"},
    {"id": 3, "zona": "san-justo", "rubro": "seguridad", "detalle": "Instalacion de camaras en obra", "contacto": "https://facebook.com/789"}
]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/buscar', methods=['GET'])
def buscar():
    zona = request.args.get('zona', '').lower()
    rubro = request.args.get('rubro', '').lower()
    
    # Filtro inteligente
    resultados = [l for l in leads_db if l['zona'] == zona and l['rubro'] == rubro]
    return jsonify(resultados)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
