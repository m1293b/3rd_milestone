import os
from server import app, db, base
from flask import render_template, request, flash, redirect, url_for

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

## route for Main page, no login required

@app.route('/login', methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    user = base.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username'] = username
        session['logged_in'] = True
        session['user_id'] = int(user.user_id)
        return redirect(url_for('home_page'))
    else:
        return render_template('sign_in.html')


## route for Main page, no login required

@app.route('/register', methods=["POST"])
def register():    
    username = request.form['username']
    password = request.form['password']
    email_address = request.form['email_address']
    points = 0
    liked_recipes = []
    user = base.query.filter_by(username=username).first()
    
    if user:
        return render_template('sign_up.html', error="User already exists")
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