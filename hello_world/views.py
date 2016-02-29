__author__ = 'Kibur'

from flask import render_template
from hello_world import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat/')
def chat():
    return render_template('chat.html')

@app.route('/about/')
def about():
    return render_template('about.html')
