import os
from app import app, db
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (
    create_engine, Column, ForeignKey, Integer, String
)
from werkzeug.security import generate_password_hash, check_password_hash

# create a class-based model for the "users" table
class Users(base):
    __tablename__ = "users"
    Column("user_id", Integer, primary_key=True),
    Column("username", String, unique=True, nullable=False),
    Column("password_hash", String, nullable=False),
    Column("email_address", String, nullable=False),
    Column("points", Integer),
    Column("liked_recipes", ARRAY(Integer))
    Relationship("recipes", backref="users", cascade="all, delete", lazy=True)
    
    def __repr__(self):
        return "#{0} is your username, {1} is you email address and these are your favorite recipes: {2}".format(
            self.username, self.email_address, self.liked_recipes
        )
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# create a class-based model for the "recipes" table
class Recipes(base):
    __tablename__ = "recipes"
    Column("recipe_id", Integer, primary_key=True),
    Column("recipe_name", String, nullable=False),
    Column("user_id", Integer, foreign_key=True, nullable=False),
    Column("ingredients", ARRAY(String), nullable=False),
    Column("instructions", String, nullable=False),
    Column("vegetarian", Boolean, nullable=False),
    Column("gluten_free", Boolean, nullable=False)
    Column("nut_free", Boolean, nullable=False)
    Column("shellfish_free", Boolean, nullable=False)
    
# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
session = Session()

# create tables if they don't exist

base.metadata.create_all(db,base.metadata.tables.values(),checkfirst=True)