from flask import Flask, jsonify
from routes.status_routes import status_bp

app = Flask(__name__)
app.register_blueprint(status_bp)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend do sistema de locação de caçambas está rodando 🚀"
    })

if __name__ == "__main__":
    app.run(debug=True)

