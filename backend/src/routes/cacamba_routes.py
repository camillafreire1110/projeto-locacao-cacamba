from flask import Blueprint, jsonify
from controllers.cacamba_controller import (
    get_cacambas,
    put_status_cacamba
)

cacamba_bp = Blueprint("cacambas", __name__)


@cacamba_bp.route("/cacambas", methods=["GET"])
def listar():
    return jsonify(get_cacambas())


@cacamba_bp.route("/cacambas/<int:id>", methods=["PUT"])
def atualizar(id):
    return put_status_cacamba(id)
