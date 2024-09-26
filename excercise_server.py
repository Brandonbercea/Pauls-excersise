# Write a server that will take in a request for a random exercise and return a random exercise from the diastasis recti exercise list in excercise_picker_cli.py

import flask
from flask import request, jsonify
import os

from exercise_picker_cli import diastasis_recti_exercises, pick_random_exercise


app = flask.Flask(__name__)



def send_from_directory(directory, filename):
    print(directory)
    print(filename)
    return flask.send_from_directory(directory, filename)

@app.route('/info', methods=['GET'])
def info():
    return "Welcome to the Diastasis Recti Exercise Picker API"

# serve an index.html page
@app.route('/', methods=['GET'])
def index():
    # get current working directory
    cwd = os.getcwd()
    return send_from_directory(cwd, 'index.html')

def serve_static_file(filename):
    cwd = os.getcwd()
    return send_from_directory(cwd, filename)

@app.route('/styles/<path:filename>', methods=['GET'])
def serve_styles(filename):
    return send_from_directory('styles', filename)

@app.route('/js/<path:filename>', methods=['GET'])
def serve_js(filename):
    return send_from_directory('js', filename)


@app.route('/api/v1/exercise', methods=['GET'])
def get_exercise():
    l1 = request.args.get('l1', 'Level 1')
    l2 = request.args.get('l2', 'Level 2')
    l3 = request.args.get('l3', 'Level 3')


    # pick_random_exercise(diastasis_recti_exercises, args.L1, args.L2, args.L3)
    exercise = pick_random_exercise(diastasis_recti_exercises, l1, l2, l3)
    return jsonify(exercise)


# Run the server
if __name__ == '__main__':
    app.run(debug=True)
    

