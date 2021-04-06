from flask import Flask, request
from flask_cors import CORS
import json
import time
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

import cv2
from deepface import DeepFace


app = Flask(__name__)
CORS(app)

@app.route('/getScore', methods=['POST'])
def getScore():
    data = request.data # width = 320, height = 240, rgba values, reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray
    data = np.array(json.loads(data))
    data = data.reshape((240, 320, 4)).astype('uint8')

    # print(data)
    # print("\n\n\n\n")
    # plt.imshow(data, interpolation='nearest')
    # plt.show()
    
    img = Image.fromarray(data, 'RGBA')
    # img.save('face.png')
    # img.show()
    pred = DeepFace.analyze(img, actions=['emotion'])
    print(pred)
    score = np.random.rand()
    return json.dumps({"score":score, "timestamp": time.time()})

def getEmotions(img):
    return

if __name__ == "__main__":
    app.run(debug=True)