from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "ok": True,
        "rota": "/",
        "mensagem": "Servidor ativo na porta 3005"
    })

@app.route("/agendador", methods=["GET"])
def rota1():
    
    """ definir servicos """
    return jsonify({
        "ok": True,
        "rota": "/rota1",
        "mensagem": "Teste da rota 1"
    })

@app.route("/rota2", methods=["GET"])
def rota2():
    return jsonify({
        "ok": True,
        "rota": "/rota2",
        "mensagem": "Teste da rota 2"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3005, debug=True)