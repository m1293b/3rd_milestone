from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import (
    Column, ForeignKey, Integer, String, ARRAY, Boolean
)
from server import db, app

# create a class-based model for the "users" table

class Users(db.Model):
    '''
    Model to build users table in the database
    '''
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False)
    points = db.Column(db.Integer)
    liked_recipes = db.Column(db.ARRAY(Integer))
    admin = db.Column(db.Boolean)
    recipes = db.relationship("Recipes", backref='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# create a class-based model for the "recipes" table

class Recipes(db.Model):
    '''
    Model to build recipes table in the database
    '''
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(20), unique=True, nullable=False)
    course = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    ingredients = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)
    vegetarian = db.Column(db.String, default='no')
    gluten_free = db.Column(db.String, default='no')
    nut_free = db.Column(db.String, default='no')
    shellfish_free = db.Column(db.String, default='no')

# create tables if they don't exist

with app.app_context():
    db.create_all()
