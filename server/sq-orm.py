from sqalchemy import (
    create_engine, Column, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "no39_recipes" database
db = create_engine("postgresql+psycopg2:///no39_recipes")
base = declerative_base()

# create a class-based model for the "users" table
class Users(base):
    __tablename__ = "users"
    Column("userid", users_userid_seq, primary_key=True, server_default=users_userid_seq.next_value()),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("email_address", String, nullable=False),
    Column("recipes", ),
    Column("points", Integer),
    Column("liked_recipes", Integer)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

