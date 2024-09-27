from server import db, base, app

from sqlalchemy import (
    Column, ForeignKey, Integer, String, ARRAY, Boolean
)
from werkzeug.security import generate_password_hash, check_password_hash

# create a class-based model for the "users" table
class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False)
    points = db.Column(db.Integer)
    liked_recipes = db.Column(db.ARRAY(Integer))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# create a class-based model for the "recipes" table
class Recipes(db.Model):
    recipes_id = Column(db.Integer, primary_key=True)
    recipes_name = Column(db.String, nullable=False)
    course = Column(db.String, nullable=False)
    user_id = Column(db.Integer, ForeignKey('users.user_id'), nullable=False)
    ingredients = Column(db.ARRAY(String), nullable=False)
    instructions = Column(db.String, nullable=False)
    vegetarian = Column(db.Boolean, nullable=False)
    gluten_free = Column(db.Boolean, nullable=False)
    nut_free = Column(db.Boolean, nullable=False)
    shellfish_free = Column(db.Boolean, nullable=False)

with app.app_context():
    db.create_all()

# create tables if they don't exist

#base.metadata.create_all(db,base.metadata.tables.values(),checkfirst=True)