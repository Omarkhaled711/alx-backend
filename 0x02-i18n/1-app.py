#!/usr/bin/env python3
"""
First task module
"""
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    Configuration class for babel application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def home_page():
    """
    renders the 1-index.html template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
