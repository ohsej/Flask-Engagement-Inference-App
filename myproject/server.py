#!/usr/bin/env python3
from flask import Flask
import socket, threading
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def launchServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                #TODO: Create threads to handle each device in parallel
                #TODO: Do downsampling
                #TODO: Send to React server
                #print
                conn.sendall(data)