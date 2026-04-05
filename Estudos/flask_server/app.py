from flask import Flask # pip install flask

app = Flask(__name__)

@app.route('/')
def status():
    return {"status": "running", "message": "Service is up and running!"}


@app.route('/status')
def healthcheck():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Escolha a porta que desejar
