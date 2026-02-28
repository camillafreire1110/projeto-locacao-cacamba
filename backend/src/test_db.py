from db import get_connection

try:
    conn = get_connection()
    print("✅ Conectou no MySQL com sucesso!")
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar:", e)
