from flask import Flask, render_template, url_for, Response, request
from PIL import Image
import requests
import pandas as pd
from io import BytesIO
import numpy as np

app = Flask(__name__)



@app.route('/', methods=('POST', 'GET'))
def index():
    # Read image URLs from DataFrame
    df = pd.read_csv('./books.csv')
    sorted_df = df.sort_values('average_rating', ascending=False)
    urls = sorted_df['thumbnail'][0:10].tolist()
    titles = sorted_df['title'][0:10].tolist()
    

    #get categories of books
    categories = df['categories'].unique().tolist()

    #get filtered row and sorting by rating
    if request.method == "POST":
        category = request.form['name']
        df_filtered = df[df['categories'] == category]
        df_filtered = df_filtered.sort_values('average_rating', ascending=False)
        urls = df_filtered['thumbnail'][0:10].tolist()
        titles = df_filtered['title'][0:10].tolist()

    return render_template('index.html', urls=urls, categories=categories, titles=titles)


@app.route('/image', methods=('POST', 'GET'))
def image():
    genre = ''
    if request.method == 'POST':
        genre = request.form['name']
    return render_template('sample.html', h1=genre)


if __name__ == "__main__":
    app.run(debug=True)