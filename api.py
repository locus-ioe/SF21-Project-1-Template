"""
This file contains the code to setup your own REST API server for use in the
project. The custom REST API server fetches data from the original One API
and only provides the first 20 characters for use in the actual app. The
comments throughout the file will guide you to fully setup your own API server.
The required utility functions are also provided in the file itself.
"""

import requests  # noqa

from flask import Flask, jsonify, request  # noqa

app = Flask(__name__)

# The following variable is a global variable that stores only the required
# data from The One API that is to be sent to your web app.
characters = []

# Import the config file which contains your API key. Head over to config.py
# and set up your API key there. If you don't have it yet, follow the URL and
# create one.
app.config.from_pyfile("config.py")
API_KEY = app.config["API_KEY"]
URL = "https://the-one-api.dev/v2/"

# These entities are the only ones that you will be needing in your app.
# You will be extracting them from the fetched data before making it
# available to your app.
required_keys = {"_id", "name", "race", "gender", "wikiUrl"}


# This is the utility function that will extract the required entities
# mentioned above. This function accepts the list of characters obtained
# from The One API and returns the list of characters with only the required
# five fields
def filter_character_fields(raw_characters):
    filtered_characters = []
    for character in raw_characters:
        filtered_characters.append(
            {key: value for key, value in character.items() if key in required_keys}
        )
    return filtered_characters


# This is your own character retrieving API endpoint. You will be hitting this
# endpoint to get the characters with only the required fields in your app.
@app.route("/character", methods=["GET"])
def get_characters():
    headers = {"Authorization": f"Bearer {API_KEY}"}  # noqa

    # Send out a request to The One API including the headers above to retrieve
    # the characters. You have to fetch only 20 characters, so you need to set
    # a limit while fetching. The limit to retrieve characters can be set as
    # "URL_TO_RETRIEVE_CHARACTER?limit=20". For further information, you can
    # consult the documentation of The One API by following this URL,
    # https://the-one-api.dev/documentation

    # The following two variables are placeholders to store the received
    # response from the API and for the list of characters after converting
    # that into JSON format. Edit these lines to obtain the required behaviour.
    response = None  # noqa
    raw_characters = []  # noqa

    # This variable stores the filtered character list that only contains the
    # fields required in yoyur web app. You can call the utility function that
    # we have provided above to extract the required fields. Edit the following
    # line to include the funciton call for extraction.
    characters = []

    return jsonify(characters)


# This is your own character adding API endpoint. You will be hitting this
# endpoint with the POST method to add new characters to your API data.
@app.route("/character", methods=["POST"])
def create_character():
    # Get a JSON of the POST request to this endpoint and store it in the
    # following variable.
    character = None  # noqa

    # Edit the following lines to store the values obtained from the POST
    # request. Store the values of field names in the corresponding field name
    # variables provided below. Extract the values from the character variable.
    _id = None
    name = None
    race = None
    gender = None
    wikiUrl = None

    # This line inserts the character details obtained from the POST request to
    # the global data variable. You need not change anything in the following
    # line but you are highly encouraged to understand the code and search for
    # similar related list manipulation functions.
    characters.insert(
        0,
        {"_id": _id, "name": name, "race": race, "gender": gender, "wikiUrl": wikiUrl},
    )

    return jsonify(message="Character Created!", status="200")


# This is your own character deleting API endpoint. You will be hitting this
# endpoint with the DELETE method to delete characters from your API data.
@app.route("/character/<id>", methods=["DELETE"])
def delete_character(id):
    # Using a for loop to go through all the characters to find the character
    # with the matching ID for deletion
    for character in characters:
        if character["_id"] == id:
            # Write down the character removal logic here. Removing the
            # characters means deleting its entry from the global character
            # list in this file.
            pass
    return jsonify()


# API Runs on port 5001
if __name__ == "__main__":
    app.run(port=5001, debug=True)
