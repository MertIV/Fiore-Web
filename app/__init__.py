
import os
from logging.handlers import SMTPHandler

from flask            import Flask,request, g, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt     import Bcrypt
from flask_babel      import Babel
from flask_mail       import Mail
from flask            import request

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object('app.config.Config')

from app.main import bp
app.register_blueprint(bp)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

db = SQLAlchemy  (app) # flask-sqlalchemy
bc = Bcrypt      (app) # flask-bcrypt
babel = Babel    (app) # flask-babel
mail = Mail      (app) # flask-mail



@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES']) or app.config['LANGUAGES'][0]
    return g.lang_code

# Import routing, models and Start the App
from app import models,email,views