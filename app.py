from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def greet():
    hostname = socket.gethostname()
    return f"Hello from Iyanu! Host: {hostname}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
