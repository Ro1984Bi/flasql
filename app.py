from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "secrey key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFiCATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(contacts)

