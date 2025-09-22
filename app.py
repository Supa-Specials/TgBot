from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return f"<h2>Ваш IP: {ip}</h2>"

if __name__ == "__main__":
    app.run()