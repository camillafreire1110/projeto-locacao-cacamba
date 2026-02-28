from flask import Flask, jsonify
from flask_cors import CORS

from routes.status_routes import status_bp
from routes.cacamba_routes import cacamba_bp

app = Flask(__name__)

# 🔥 Habilita CORS (permite front na porta 5500 conversar com backend 5000)
CORS(app)

# Registra os blueprints
app.register_blueprint(status_bp)
app.register_blueprint(cacamba_bp)


@app.route("/")
def home():
    return jsonify({
        "message": "Backend do sistema de locação de caçambas está rodando!"
    })


if __name__ == "__main__":
    app.run(debug=True)
