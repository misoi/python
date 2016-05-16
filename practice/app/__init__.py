from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

from app import views
