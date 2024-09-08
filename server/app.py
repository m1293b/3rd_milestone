import os
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')

@app.route('/')
def index_page():
    return render_template("index.html", page_title = 'Main page')

@app.route('/recipes')
def recipes_page():
    return render_template("recipes.html", page_title = 'Recipes page')

@app.route('/about')
def about_page():
    return render_template("about.html", page_title = 'About page')

@app.route('/login')
def login_page():
    return render_template("login.html", page_title = 'Login page')

def login_check():
    print('hello')

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")), #don't forget to change the port to 5000 for the live site
        debug = True #delete this line before submiting project
    )