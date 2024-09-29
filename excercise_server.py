# Write a server that will take in a request for a random exercise and return a random exercise from the diastasis recti exercise list in excercise_picker_cli.py

import flask
from flask import request, jsonify
from bs4 import BeautifulSoup

import os
import json

import requests
import urllib.parse

from exercise_picker_cli import diastasis_recti_exercises, pick_random_exercise

# make a constant for the youtube api key that is pulled from the environment or falls back to a default value
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', 'AIzaSyD-9tSr1k1vq1ZgK0CJhj6qKf6Qp4i4KdI')
YOUTUBE_EMBED_URL = "https://www.youtube.com/embed?listType=search&list="


app = flask.Flask(__name__)


def send_from_directory(directory, filename):
    print(directory)
    print(filename)
    return flask.send_from_directory(directory, filename)

# Query youtube for a video about the excercise.name and add the video embed link to the excercise object
def decorate_exercises(exercises):
    # print(f"excercises to decorate: {json.dumps(exercises, indent=4)}")

    for exercise_level in exercises:
        # print(f"excercise name: {json.dumps(exercises[exercise_level], indent=4)}")
        # print(f"exercise name: {exercises[exercise_level]}")

        for exercise in exercises[exercise_level]:
            exercise_name = exercise['name']
            print(f"excercise name: {exercise_name}")

            # query the youtube api embed URL for a video about the exercise
            query = exercise['name'] + " exercise"
            query = urllib.parse.quote(exercise_name)
            print(f"query: {query}")
            response = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={query}&key={YOUTUBE_API_KEY}")
            print(f"response: {response}")

            # parse the response to get the video link
            video_link = None
            if response.status_code == 200:
                response_json = response.json()
                video_id = response_json['items'][0]['id']['videoId']
                video_link = f"{YOUTUBE_EMBED_URL}{video_id}"
                print(f"video link: {video_link}")
            else:
                print(f"Error: {response.status_code}")

        
        
        # add the video link to the exercise object
        exercise['video'] = video_link



    return exercises

        # Example request:

        



        


        # https://www.youtube.com/embed?listType=search&list=diastasis+recti+exercise
        
    return

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


@app.route('/node_modules/<path:filename>', methods=['GET'])
def serve_node_modules(filename):
    return send_from_directory('node_modules', filename)

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


    # resolveExcerciseList()
    exercises = pick_random_exercise(diastasis_recti_exercises, l1, l2, l3)

    decorated_excercises = decorate_exercises(exercises)

    #pretty print the exercises in json format
    print(json.dumps(decorated_excercises, indent=4))

    return jsonify(decorated_excercises)


# Run the server
if __name__ == '__main__':
    app.run(debug=True)
    print("Server is running on http://127.0.0.1:5000")
    

