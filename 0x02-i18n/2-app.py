#!/usr/bin/env python3
'Flask app'

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config(object):
    LANGUAGES = ['en', 'fr']

babel.BABEL_DEFAULT_LOCALE = Config.LANGUAGES[0]
babel.BABEL_DEFAULT_TIMEZONE = 'UTC'
app.config = Config

@babel.localeselector
def get_locale():
    '''determine the best match with our supported languages'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
