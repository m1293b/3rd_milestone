from sqalchemy import (
    create_engine, Column, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

import os
from flask import Flask, render_template, request, flash, redirect, url_for
# if os.path.exists("env.py"):
#     import env

app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')
app.secret_key = os.environ.get("SECRET_KEY")

# executing the instructions from the "no39_recipes" database
db = create_engine("postgresql+psycopg2:///no39_recipes")
base = declarative_base()

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# create a class-based model for the "users" table
class Users(base):
    __tablename__ = "users"
    Column("user_id", Integer, primary_key=True),
    Column("username", String, unique=True, nullable=False),
    Column("password_hash", String, nullable=False),
    Column("email_address", String, nullable=False),
    Column("points", Integer),
    Column("liked_recipes", ARRAY(Integer))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Recipes(base):
    __tablename__ = "recipes"
    Column("recipe_id", Integer, primary_key=True),
    Column("recipe_name", String, nullable=False),
    Column("user_id", Integer, foreign_key=True, nullable=False),
    Column("ingredients", ARRAY(String), nullable=False),
    Column("instructions", String, nullable=False),
    Column("vegeterian", Bolean, nullable=False),
    Column("gluten_free", Bolean, nullable=False)
    Column("nut_free", Bolean, nullable=False)
    Column("shellfish_free", Bolean, nullable=False)

## route for Main page, no login required

@app.route('/')
def index_page():
    return render_template("index.html", page_title = 'Main page')

## route for Recipes page, no login required

@app.route('/recipes')
def recipes_page():
    return render_template("recipes.html", page_title = 'Recipes page')

## route for About page, no login required

@app.route('/about')
def about_page():
    return render_template("about.html", page_title = 'About page')

## route for Login page, no login required

@app.route('/login_page')
def login_page():
    return render_template("login_page.html", page_title = 'Login page')

## route for Sign page, no login required

@app.route('/signup')
def signup_page():
    return render_template("signup.html", page_title = 'Sign up page')

## route for Home page, login required

@app.route('/home')
def home_page():
    return render_template("home.html", page_title = 'Home page')

## route for Main page, no login required

@app.route('/login', methods=["POST"])
def login():
    username = request.form('username')
    password = request.form('password')
    user = base.query.filter_by(username=username).first()
    if user and user.check_password():
        session['username'] = username
        return redirect(url_for('home_page'))
    else:
        return render_template('login_page.html')


## route for Main page, no login required

@app.route('/register', methods=["POST"])
def register():
    username = request.form('username')
    password = request.form('password')
    email_address = request.form('email_address')
    points = 0
    liked_recipes = []
    user = base.query.filter_by(username=username).first()
    
    
    if user and user.check_password():
        return render_template('signup.html', error="User already exists")
    else:
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.email_address = email_address
        new_user.points = points
        new_user.liked_recipes = liked_recipes
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect(url_for('home_page'))
        

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")), #don't forget to change the port to 5000 for the live site
        debug = True #delete this line before submitting project
    )

# create tables if they don't exist

base.metadata.create_all(db,base.metadata.tables.values(),checkfirst=True)