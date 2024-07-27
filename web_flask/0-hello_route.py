#!/usr/bin/python3
"""
This script run flask web application and
listening on 0.0.0.0 port 5000
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Return string"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)