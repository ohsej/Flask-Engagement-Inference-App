#!/usr/bin/env python3

#use this to send to react app, receive data, then downsample,
#forward through another function to send to react server
#replace with code from doc to connect to specific host and port that corresponds to react host and port
#convert to socketio client, [serve up socket, allow others to connect]

import socketio

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Make sure 5000 corresponds to the React server socketio port number

sio = socketio.Client()                 # creates a standard Python client instance

sio.connect('http://localhost:5000', namespaces=['/react server', '/flask app'])  # establishes connection to server at PORT = 5000
session_identifier = sio.sid

data_queue = {}

@sio.event(namespace='/react server')
def receive_data(data):
    data.append(data)
    print('Received data', data)

@sio.event(namespace='/react server')
def send_for_downsampling(data):
    sio.emit('downsample data', {'input data': data}, namespace='/flask app') # send to downsampler
    print('Sent data to Flask App to downsample data')

@sio.event(namespace='/react server')
def send_data():
    sio.emit('react receives', {'data': data_queue})
    print('Sent data to React App')

@sio.event
def connect():
    print("Connected")

@sio.event
def connect_error():
    print("Connect error: connection failed")

@sio.event
def disconnect():
    print("Disconnected!")