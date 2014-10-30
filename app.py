from flask import Flask, request, render_template
import cPickle as pickle
#from model import getdata, myModel

app = Flask(__name__)

@app.route('/')
def index():
    lst = range(10)
    return render_template('index.html', entries=lst)

# @app.route('/score', methods=['POST'])
# def score():
#     data = request.json

# @app.route('/dashboard')
# def dashboard():
#     pass

if __name__ == '__main__':
    app.run(debug=True)