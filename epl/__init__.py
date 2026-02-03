from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.sqlite'
app.secret_key = b'Oat'

db = SQLAlchemy(app)  
migarte = Migrate(app, db)

from epl import models, routes