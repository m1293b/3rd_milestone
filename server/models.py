from server import db, base

from sqlalchemy import (
    Column, ForeignKey, Integer, String, ARRAY, Boolean
)
from werkzeug.security import generate_password_hash, check_password_hash

# create a class-based model for the "users" table
class Users(db.Model):
    __tablename__ = "users"
    user_id = Column("user_id", Integer, primary_key=True)
    username = Column("username", String, unique=True, nullable=False)
    password_hash = Column("password_hash", String, nullable=False)
    email_address = Column("email_address", String, nullable=False)
    points = Column("points", Integer)
    liked_recipes = Column("liked_recipes", ARRAY(Integer))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# create a class-based model for the "recipes" table
class Recipes(db.Model):
    __tablename__ = "recipes"
    recipes_id = Column("recipe_id", Integer, primary_key=True)
    recipes_name = Column("recipe_name", String, nullable=False)
    user_id = Column("user_id", Integer, ForeignKey('users.user_id'), nullable=False)
    ingredients = Column("ingredients", ARRAY(String), nullable=False)
    instructions = Column("instructions", String, nullable=False)
    vegetarian = Column("vegetarian", Boolean, nullable=False)
    gluten_free = Column("gluten_free", Boolean, nullable=False)
    nut_free = Column("nut_free", Boolean, nullable=False)
    shellfish_free = Column("shellfish_free", Boolean, nullable=False)

# create tables if they don't exist

#base.metadata.create_all(db,base.metadata.tables.values(),checkfirst=True)