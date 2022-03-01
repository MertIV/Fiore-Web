import os
from decouple import config

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():

    CSRF_ENABLED = os.truncate
	
    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    LANGUAGES = ['en', 'fr']

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'fioreclinique@gmail.com'
    MAIL_PASSWORD = 'Troyes.AUBE10'

    ADMINS = ['fioreclinique@gmail.com','mrtkrt96@gmail.com']

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
