from flask import Flask, render_template, url_for, Response, request
from PIL import Image
import requests
import pandas as pd
from io import BytesIO
import numpy as np

app = Flask(__name__)

# Read image URLs from DataFrame
df = pd.read_csv('./books.csv')

#similarity data
similarity_df = pd.read_csv("./similarity_books.csv")

#find the index of title
def get_index(title):
  return df[df.title == title].index.values[0] 

@app.route('/', methods=('POST', 'GET'))
def index():
    thumb = []
    #get filtered row and sorting by rating
    if request.method == "POST":
        text = request.form['text']
        book_id = get_index(text)
        #find the similar value 
        similar_books = list(enumerate(similarity_df[str(book_id)]))
        sorted_books = sorted(similar_books,key=lambda x:x[1],reverse=True)
        #append similarity books
        for i in range(20):
            thumb.append(df[df.index == sorted_books[i][0]]["thumbnail"].values[0])
        """category = request.form['name']
        df_filtered = df[df['categories'] == category]
        df_filtered = df_filtered.sort_values('average_rating', ascending=False)
        urls = df_filtered['thumbnail'][0:10].tolist()
        titles = df_filtered['title'][0:10].tolist()"""
    
    return render_template('index.html', thumb=thumb)#, categories=categories, titles=titles)


@app.route('/image', methods=('POST', 'GET'))
def image():
    text = ''
    if request.method == "POST":
        text = request.form['text']
        print(text)
    return render_template('sample.html', h1=text)


if __name__ == "__main__":
    app.run(debug=True)