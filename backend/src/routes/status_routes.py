from flask import Blueprint, jsonify

# Blueprint responsável pelas rotas de status da API
status_bp = Blueprint('status_bp', __name__)

# Rota usada para verificar se a API está ativa
@status_bp.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "API funcionando",
        "sistema": "Sistema de Locação de Caçambas",
        "versao": "1.0",
        "mensagem": "Backend ativo e respondendo corretamente"
    })
