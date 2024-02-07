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


def get_locale() -> str:
    """
    responsible for determining the best-matching
    locale based on the user's preferences from the
    Accept-Language header in the HTTP request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def home_page() -> str:
    """
    renders the 1-index.html template
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
