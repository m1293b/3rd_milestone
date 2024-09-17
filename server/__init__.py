import os
from flask import Flask
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

if os.path.exists("env.py"):
    import env
    
app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["NO39_RECIPES_DATABASE_URI"] = os.environ.get("DB_URL")

# executing the instructions from the "no39_recipes" database
db = create_engine("postgresql+psycopg2:///no39_recipes")
base = declarative_base()