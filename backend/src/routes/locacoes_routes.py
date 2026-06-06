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
        cursor.execute(
            "SELECT id FROM clientes WHERE id = %s", (cliente_id,))
        if not cursor.fetchone():
            return jsonify({"erro": "Cliente não existe"}), 400

        # Verifica caçamba
        cursor.execute(
            "SELECT id FROM cacambas WHERE id = %s", (cacamba_id,))
        if not cursor.fetchone():
            return jsonify({"erro": "Caçamba não existe"}), 400

        # Insere locação
        cursor.execute("""
            INSERT INTO locacoes (
                cliente_id,
                cacamba_id,
                data_entrega,
                data_retirada
            )
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

    cursor.close()
    conn.close()

    return jsonify(locacoes)


# 🔥 PUT - Atualizar locação
@locacoes_bp.route('/locacoes/<int:id>', methods=['PUT'])
def atualizar_locacao(id):
    try:
        data = request.get_json()

        status_locacao = data.get('status_locacao')
        status_pagamento = data.get('status_pagamento')

        conn = get_connection()
        cursor = conn.cursor()

        # Entrega
        if status_locacao == "entregue":

            cursor.execute("""
                UPDATE locacoes
                SET status_locacao = %s,
                    status_pagamento = %s,
                    data_entrega_real = NOW()
                WHERE id = %s
            """, (status_locacao, status_pagamento, id))

        # Finalização
        elif status_locacao == "finalizada":

            cursor.execute("""
                UPDATE locacoes
                SET status_locacao = %s,
                    status_pagamento = %s,
                    data_retirada_real = NOW()
                WHERE id = %s
            """, (status_locacao, status_pagamento, id))

        else:

            cursor.execute("""
                UPDATE locacoes
                SET status_locacao = %s,
                    status_pagamento = %s
                WHERE id = %s
            """, (status_locacao, status_pagamento, id))

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({
            "mensagem": "Locação atualizada com sucesso!"
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
