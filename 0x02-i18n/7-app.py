#!/usr/bin/env python3
'Flask app'

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional
from pytz import timezone

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''Cnfig class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    '''returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed'''
    try:
        u_id = request.args.get('login_as')
        return users.get(int(u_id))
    except Exception:
        return


@babel.timezoneselector
def get_timezone():
    '''imezone parameter in URL parameters'''
    tz = request.args.get('timezone')
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    u_id = request.args.get('login_as')
    if u_id:
        tz = users.get(int(u_id)).get('timezone')
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    else:
        return 'UTC'


@app.before_request
def before_request():
    '''use get_user to find a user if any, and set it as a global on
    flask.g.user'''
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale() -> Optional[str]:
    '''select a language translation to use for the request'''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    u_id = request.args.get('login_as')
    if u_id:
        locale = users.get(int(u_id)).get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    headers = request.headers.get("locale")
    if headers:
        return headers
    if len(request.accept_languages) > 0:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    else:
        return app.config.BABEL_DEFAULT_LOCALE


@app.route('/', strict_slashes=False)
def main():
    '''index route'''
    home_title = 'Welcome to Holberton'
    home_header = 'Hello world!'
    return render_template('6-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
