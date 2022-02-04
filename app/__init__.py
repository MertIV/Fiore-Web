
import os
from logging.handlers import SMTPHandler

from flask            import Flask,request, g, redirect, url_for,session,current_app,abort
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


@app.before_request
def before_request():
    if request.view_args==None:
        if not 'lang_code' in session.keys():
            return redirect('/en' + request.full_path)
        else:
            return redirect('/'+session['lang_code']+request.full_path)

    # if g.lang_code not in current_app.config['LANGUAGES']:
    #     adapter = app.url_map.bind('')
    #     try:
    #         endpoint, args = adapter.match('/en' + request.full_path.rstrip('/ ?'))
    #         return redirect(url_for(endpoint, **args), 301)
    #     except:
    #         print('Burda cortladın')
    #         abort(404)

    # dfl = request.url_rule.defaults
    # if 'lang_code' in dfl:
    #     if dfl['lang_code'] != request.full_path.split('/')[1]:
    #         print('Hayır Burda cortladın')
    #         abort(404)

@app.context_processor
def inject_lang():
    return dict(sess_lang=session['lang_code'])

@babel.localeselector
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES']) or app.config['LANGUAGES'][0]
    return g.lang_code

# Import routing, models and Start the App
from app import models,email,views