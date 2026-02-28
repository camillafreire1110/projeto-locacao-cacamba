from flask import request
from models.cacamba_model import (
    listar_cacambas,
    atualizar_status_cacamba
)


def get_cacambas():
    return listar_cacambas()


def put_status_cacamba(id):
    dados = request.get_json()
    novo_status = dados.get("status")

    atualizar_status_cacamba(id, novo_status)

    return {"message": "Status atualizado com sucesso"}, 200
