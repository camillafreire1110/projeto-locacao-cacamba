from db import get_connection


def listar_cacambas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM cacambas")
    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados


def atualizar_status_cacamba(id, status):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE cacambas
    SET status = %s
    WHERE id = %s
    """

    cursor.execute(sql, (status, id))
    conn.commit()

    cursor.close()
    conn.close()
