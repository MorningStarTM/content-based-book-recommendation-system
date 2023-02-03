from flask import Flask, render_template, url_for, Response
import cv2
import requests
import pandas as pd
import io
import numpy as np

app = Flask(__name__)

#function for get image using url
def get_image():
    image_list = []
    df = pd.read_csv('./books')
    url = df['thumbnail'][1:10]
    for i in range(10):
        #get the image by url
        response = requests.get(url[i])
        if response.status_code == 200:
        # Read the image data and convert it to a NumPy array
            content = np.asarray(bytearray(response.content), dtype=np.uint8)
            img = content.tobytes()
            image_list.append(img)
    return image_list





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/image')
def image():
    return Response(get_image(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)