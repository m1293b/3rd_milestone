import os
from server import app, db, base
from server.models import Users
from flask import render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
def index_page():
    return render_template("index.html", page_title = 'Main page')

## route for Recipes page, no login required

@app.route('/recipes')
def recipes_page():
    if session['logged_in'] == True: # does this work??
        return render_template("recipes_home.html", page_title = 'Recipes page')
    else:
        return render_template("recipes.html", page_title = 'Recipes page')

## route for About page, no login required

@app.route('/about')
def about_page():
    return render_template("about.html", page_title = 'About page')

## route for Sign in page, no login required

@app.route('/sign_in')
def sign_in_page():
    return render_template("sign_in.html", page_title = 'Sign in page')

## route for Sign up page, no login required

@app.route('/sign_up')
def sign_up_page():
    return render_template("sign_up.html", page_title = 'Sign up page')

## route for Home page, login required

@app.route('/home')
def home_page():
    return render_template("home.html", page_title = 'Home page')

@app.route('/events')
def events_page():
    return render_template("events.html", page_title = 'Events page')

## route to log user in, data to be verified is pulled from input fields

@app.route('/login', methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    user = Users.query.filter_by(username = username).first()
    if user and user.check_password(password):
        session['username'] = username
        return redirect(url_for('home_page'))
    else:
        return render_template('sign_in.html')

## route to log user out from session

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop('username')
    return redirect(url_for('index_page'))


## route to register an account, data is pulled from input fields

@app.route('/register', methods=["POST"])
def register():    
    username = request.form['username']
    password = request.form['password']
    email_address = request.form['email_address']
    user = Users.query.filter_by(username = username).first()
    if user:
        return render_template('sign_up.html', error="User already exists")
        flash("User already exists")
    else:
        new_user = Users()
        new_user.username = username
        new_user.set_password(password)
        new_user.email_address = email_address
        new_user.points = 0
        new_user.liked_recipes = []
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username    
        return redirect(url_for('home_page'))