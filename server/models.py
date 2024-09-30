from server import db, base, app

from sqlalchemy import (
    Column, ForeignKey, Integer, String, ARRAY, Boolean
)
from werkzeug.security import generate_password_hash, check_password_hash

# create a class-based model for the "users" table
class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False)
    points = db.Column(db.Integer)
    liked_recipes = db.Column(db.ARRAY(Integer))
    recipes = db.relationship("Recipes", backref='users')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# create a class-based model for the "recipes" table
class Recipes(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String, unique=True, nullable=False)
    course = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    ingredients = db.Column(db.String, nullable=False)
    instructions = db.Column(db.String, nullable=False)
    vegetarian = db.Column(db.String, default='no')
    gluten_free = db.Column(db.String, default='no')
    nut_free = db.Column(db.String, default='no')
    shellfish_free = db.Column(db.String, default='no')

with app.app_context():
    db.create_all()

# create tables if they don't exist

#base.metadata.create_all(db,base.metadata.tables.values(),checkfirst=True)