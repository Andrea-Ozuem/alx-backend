#!/usr/bin/env python3
'Flask app'

from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''Cnfig class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''select a language translation to use for that request'''
    if request.locale and request.locale in app.config['LANGUAGES']:
        return request.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def main():
    '''index'''
    message = {'home_title': _('Welcome to Holberton'),
               'home_header': _('Hello world!')}
    return render_template('3-index.html', message=message)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)