from flask import Blueprint, request, jsonify
from db import get_connection

locacoes_bp = Blueprint('locacoes', __name__)

# 🔥 POST - Criar locação


@locacoes_bp.route('/locacoes', methods=['POST'])
def criar_locacao():
    try:
        data = request.get_json()

        cliente_id = data.get('cliente_id')
        cacamba_id = data.get('cacamba_id')
        data_entrega = data.get('data_entrega')
        data_retirada = data.get('data_retirada')

        conn = get_connection()
        cursor = conn.cursor()

        # Verifica cliente
        cursor.execute("SELECT id FROM clientes WHERE id = %s", (cliente_id,))
        if not cursor.fetchone():
            return jsonify({"erro": "Cliente não existe"}), 400

        # Verifica caçamba
        cursor.execute("SELECT id FROM cacambas WHERE id = %s", (cacamba_id,))
        if not cursor.fetchone():
            return jsonify({"erro": "Caçamba não existe"}), 400

        # Insere locação
        cursor.execute("""
            INSERT INTO locacoes (cliente_id, cacamba_id, data_entrega, data_retirada)
            VALUES (%s, %s, %s, %s)
        """, (cliente_id, cacamba_id, data_entrega, data_retirada))

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"mensagem": "Locação cadastrada com sucesso!"})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


# 🔥 GET - Listar locações
@locacoes_bp.route('/locacoes', methods=['GET'])
def listar_locacoes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM locacoes")
    locacoes = cursor.fetchall()

    return jsonify(locacoes)
