#!/usr/bin/env python3
"""
First task module
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_page():
    """
    renders the 0-index.html template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
