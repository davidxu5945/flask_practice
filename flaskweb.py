from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
toolbar = DebugToolbarExtension(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
