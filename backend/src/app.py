from flask import Flask, jsonify, request
from flask_cors import CORS

from routes.status_routes import status_bp
from routes.cacamba_routes import cacamba_bp

from db import get_connection  # conexão com banco

app = Flask(__name__)

# Habilita CORS
CORS(app)

# Registra os blueprints
app.register_blueprint(status_bp)
app.register_blueprint(cacamba_bp)


@app.route("/")
def home():
    return jsonify({
        "message": "Backend do sistema de locação de caçambas está rodando"
    })


# =========================
# 🔥 AC2 - CLIENTES
# =========================

# ✅ POST - Criar cliente
@app.route('/clientes', methods=['POST'])
def criar_cliente():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO clientes (nome, cpf_cnpj, endereco, telefone, email)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        data['nome'],
        data['cpf_cnpj'],
        data['endereco'],
        data['telefone'],
        data['email']
    )

    cursor.execute(sql, valores)
    conn.commit()

    return jsonify({"msg": "Cliente cadastrado com sucesso"})


# ✅ GET - Listar clientes
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    return jsonify(clientes)


if __name__ == "__main__":
    app.run(debug=True)
