import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    MAIL_PORT = 465
    ENV = 'production'
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_PASSWORD = 'LearnHack14!'
    SECRET_KEY = 'SECRET_KEY'
    MAIL_SERVER = 'smtp.gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_USERNAME = 'learnhacktutoring@gmail.com'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
