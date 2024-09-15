from sqalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql+psycopg2:///no39_recipes")
base = declerative_base()

class Users(base):
    __tablename__ = "users"
    Column("userid", users_userid_seq, primary_key=True, server_default=users_userid_seq.next_value()),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("email_address", String, nullable=False),
    Column("recipes", ),
    Column("points", Integer),
    Column("liked_recipes", Integer)

Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

