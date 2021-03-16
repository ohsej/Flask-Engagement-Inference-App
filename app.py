from flask import Flask, request
from flask_cors import CORS
import json
import time

app = Flask(__name__)
CORS(app)

@app.route('/getScore', methods=['POST'])
def getScore():
    data = request.data # width = 320, height = 240, rgba values, referece: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray
    score = 1
    return json.dumps({"score":score, "timestamp": time.time()})

if __name__ == "__main__":
    app.run(debug=True)