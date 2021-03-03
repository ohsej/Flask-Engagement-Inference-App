from flask import Flask
import socket, threading
from .server import launchServer
# from .client import 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
    t = threading.Thread(target=launchServer)
    t.daemon = True
    t.start()