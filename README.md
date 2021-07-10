# Software Fellowship 2021 | Project 1

## Instructions

1. Clone this repo using [git](https://git-scm.com/), or download it and later upload it through GitHub GUI itself. The previous one is the recommended way.
2. Create a vitrual environment and activate it. [Detailed Instructions Here](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
3. Enter following in the terminal to install required dependencies.
  ```sh
    pip install -r requirements.txt
  ```
4. The repo contains code for mainly two servers.
    1. `api.py` for creating an API
    2. `app.py` for displaying them using `jinja` in HTML
5. The functions in the provided files should be updated as instructed there to make a fully functioning, beautiful web app.
6. This repo should contain the code with the deadline.

## Project Components

### REST API

- Use the `api.py`, provided in this repo, for creating an REST API server run in post 5001.
- The server should request the characters API from the [The One API](https://the-one-api.dev/documentation/#4) using the token provided by the website itself.
- The file is a complete REST API server where the useful [HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) are implemented viz. GET, POST, and DELETE.
    - _NOTE: We do not require PUT request to be implemented for grading._
- Read the comments in the file to make a fully functioning REST API yourself.
- It acts like a proxy server to a small portion of the [The One API](https://the-one-api.dev/).

### FLASK SERVER

- Use the `app.py`, provided in this repo, for creating an server run in post 5000.
- The server should request the characters API from the other server described above.
- The server should return only HTML pages populating the data requested.
- Read the comments in the file to make a fully functioning web server.

### HTML Templates

- The templates for the flask server are inside `templates` directory.
- Jinja reads the template and converts it into pure HTML before the server sends a response.
- The templates provided are just minimal working version. **You need to add styles to them either by writing the CSS yourself or using its frameworks like [Bootstrap](https://getbootstrap.com/).**
- Since the styling part is done by you, it will be highly unlikely if your HTML pages appear the same as the other participants. If we find that one project is a copy of another, then both of the projects will not be graded.
