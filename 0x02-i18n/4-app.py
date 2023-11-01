#!/usr/bin/env python3
"""3. Parameterize templates - outputs Hello World.
This module parametises the title and header to different
locales"""

from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Optional

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''Cnfig class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Optional[str]:
    '''select a language translation to use for the request
    either from url or using best fit from client settings
    '''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def main():
    '''index route to display title and header
    with translations workflow'''
    home_title = 'Welcome to Holberton'
    home_header = 'Hello world!'
    return render_template('4-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
