from flask import Blueprint, jsonify

status_bp = Blueprint('status_bp', __name__)

@status_bp.route('/status', methods=['GET'])
def status():
    return jsonify({
        "status": "API funcionando",
        "mensagem": "Backend do sistema de locação de caçambas ativo"
    })
