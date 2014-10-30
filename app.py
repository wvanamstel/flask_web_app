from flask import Flask, request, render_template
import cPickle as pickle
#from model import getdata, myModel

app = Flask(__name__)

@app.route('/')
def index():
    test_dict = {'predictions': 0,
                'approx_payout_date': 1279267200,
                'body_length': 204,
                'channels': 6,
                'delivery_method': 0.0,
                'event_created': 1278365733,
                'event_end': 1278835200,
                'event_published': 1278475736.0,
                'event_start': 1278817200,
                'fb_published': 0,
                'gts': 515.0,
                'has_analytics': 0,
                'has_logo': 0,
                'name_length': 21,
                'num_order': 13,
                'num_payouts': 0,
                'org_facebook': 0.0,
                'org_twitter': 0.0,
                'sale_duration': 4.0,
                'sale_duration2': 5,
                'show_map': 1,
                'user_age': 217,
                'user_created': 1259613950} 
    return render_template('index.html', entries=test_dict)

# @app.route('/score', methods=['POST'])
# def score():
#     data = request.json

# @app.route('/dashboard')
# def dashboard():
#     pass

if __name__ == '__main__':
    app.run(debug=True)