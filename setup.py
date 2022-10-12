from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ENV = 'prod'
app = Flask(__name__)

# setting up database credentials
if ENV == 'dev':
    config = open('configlocal.txt', 'r').read()
    app.debug = True
elif ENV == 'prod':
    try:
        config = open('configprod.txt', 'r').read()
    except FileNotFoundError:
        print("Database config not found. Please provide necessary details.\nDatabase url:")
        db_url = input()
        print("Name of database:")
        db_name = input()
        print("Database username:")
        db_username = input()
        print("Database password:")
        db_password = input()
        with open('configprod.txt', 'w') as f:
            f.write('postgresql://{}:{}@{}/{}'.format(
                db_username, db_password, db_url, db_name))
        config = open('configprod.txt', 'r').read()
    app.debug = False
app.config['SQLALCHEMY_DATABASE_URI'] = config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
