import os
WTF_CSRF_ENABLED = True # activates the cross-site request forgery prevention and it is enabled by default flask-WTF
SECRET_KEY = 'you-will-never-guess' # only needed when CSRF is enabled , used to create cryptographic token that is used to validate forms

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #database path
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') #is the folder where we will store the SQLAlchemy-migrate data files.


