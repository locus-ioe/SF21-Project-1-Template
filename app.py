"""
This file contains the code to setup the Flask server for your app. This file
issues API requests to your proxy API server setup in api.py and renders the
templates using the retrieved data. The comments throughout the file will guide 
you to setup your app server and display a basic website without styling.
"""

import requests

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# The URL to request for the character data is your own API server instead of the
# One API over the internet.
URL = "http://localhost:5001/"


# This is your endpoint to render the form and the characters table. You will be
# hitting this endpoint to render your application with data.
@app.route("/character", methods=["GET", "POST"])
def get_or_update_character():

    # Check if the form in the page was submitted with character data. Submitting data
    # would mean a POST request being sent.
    if request.method == "POST":
        # This line retrieves the data submitted in the form as a dictionary and stores
        # it to POST into the API.
        character = dict(request.form)

        # This line sends a POST request to the API server you created in api.py with the
        # data retrieved from the form. Update the empty string in the line to include the
        # endpoint for adding the characters.
        requests.post("", json=character)

    # This part retrieves the data from your own API to update the table in the app. Send a
    # GET request to the endpoint for getting the characters and store the response in the
    # corresponding variable. Converrt it into JSON format and store it in the characters
    # list which will sent to your template.
    response = None  # noqa
    characters = None

    return render_template("table.html", characters=characters)


# This is your endpoint for deleting a character. You will be hitting this endpoint with a
# GET request when you click the delete button provided in the template. After that you need
# to send a DELETE request to your API for character deletion.
@app.route("/character/<id>", methods=["GET"])
def delete_character(id):
    # Update the empty string in the following line to include your endpoint for character
    # deletion.
    requests.delete("")

    # Render the same form and table after deleting a character.
    return redirect(url_for("get_or_update_character"))


# App runs on port 5000
if __name__ == "__main__":
    app.run(port=5000, debug=True)
