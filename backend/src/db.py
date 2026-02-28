import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Faculdade@2026",
        database="locadora_cacambas"
    )
