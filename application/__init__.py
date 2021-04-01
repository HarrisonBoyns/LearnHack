from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import config
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.urandom(32)

application = Flask(__name__)

application.config.from_object(config.Config)

mail = Mail(application)

db = SQLAlchemy(application)
migrate = Migrate(application, db)

gunicorn_logger = logging.getLogger('gunicorn.error')
application.logger.handlers = gunicorn_logger.handlers
application.logger.setLevel(gunicorn_logger.level)

from application import routes, models
