from flask import Flask, request, render_template
from cPickle import pickle
from model import getdata, myModel

app = Flask(__name__)

@app.route('/')
def index():
    return

@app.route('/score', methods=['POST'])
def score():
    data = request.json

@app.route('/dashboard')
def dashboard():
    return html

requests.post('http://10.0.1.23.5000/register',)

if __name__ == '__main__':
    app.run()
