import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

if os.path.exists("env.py"):
    import env
    
app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')
app.secret_key = "the_actual_secret_flash_key"
app.config["SECRET_KEY"] = "the_actual_secret_flash_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///no39_recipes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# executing the instructions from the "no39_recipes" database
db = SQLAlchemy(app)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)

base = declarative_base()