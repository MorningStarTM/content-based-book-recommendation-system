from flask import Flask, render_template, url_for, Response, request
from PIL import Image
import requests
import pandas as pd
from io import BytesIO
import numpy as np

app = Flask(__name__)



@app.route('/')
def index():
    # Read image URLs from DataFrame
    df = pd.read_csv('./books.csv')
    sorted_df = df.sort_values('average_rating', ascending=False)
    urls = sorted_df['thumbnail'][0:10].tolist()
    
    return render_template('index.html', urls=urls)


@app.route('/image', methods=('POST', 'GET'))
def image():
    genre = ''
    if request.method == 'POST':
        genre = request.form['name']
    return render_template('sample.html', h1=genre)


if __name__ == "__main__":
    app.run(debug=True)