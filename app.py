import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/recipes')
def recipes_page():
    return render_template("recipes.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/login')
def login_page():
    return render_template("login.html")

def login_check():
    print('hello')

if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")), #don't forget to change the port to 5000 for the live site
        debug = True #delete this line before submiting project
    )