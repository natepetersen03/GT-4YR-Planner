from flask import Flask
api = Flask(__name__)

@api.route('/schedule')

def my_schedule():
    data = {
        'name': 'Nate',
        'about': 'Building app'
    }
    return data
