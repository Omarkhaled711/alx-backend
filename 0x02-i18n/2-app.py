#!/usr/bin/env python3
"""
First task module
"""
from flask import Flask, render_template, request
from flask_babel import Babel

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
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    responsible for determining the best-matching
    locale based on the user's preferences from the
    Accept-Language header in the HTTP request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
