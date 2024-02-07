#!/usr/bin/env python3
"""
First task module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import exceptions, timezone
from typing import Union

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """
    Configuration class for babel application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    responsible for determining the best-matching
    locale based on the user's preferences from the
    Accept-Language header in the HTTP request.
    """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    elif g.user and g.user.get('locale')\
            and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ get timezone """
    if request.args.get('timezone'):
        time = request.args.get('timezone')
    elif g.user and g.user.get('timezone'):
        time = g.user.get('timezone')
    try:
        return timezone(time)
    except exceptions.UnknownTimeZoneError:
        return timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


def get_user() -> Union[dict, None]:
    """
    get the logged in user
    """
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """
    find a user if any, and set it as a global on flask.g.user.
    """
    g.user = get_user()


@app.route('/', strict_slashes=False)
def home_page() -> str:
    """
    renders the 1-index.html template
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
