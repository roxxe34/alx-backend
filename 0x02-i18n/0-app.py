<<<<<<< HEAD
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("1-index.html")
=======
#!/usr/bin/env python3
"""
Basic Flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    hello world
    """
    return render_template('0-index.html')
>>>>>>> 6db9e63516616551678817ffaa0ccc7231b5c5bd
