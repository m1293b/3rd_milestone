from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData, Sequence
)

#executing the instruction from our localhost "no39_recipes" db
db = create_engine("postgresql+psycopg2:///no39_recipes")

meta = MetaData()

# create variable for "users" table

users_userid_seq = Sequence('users_userid_seq')

users_table = Table("users", meta,
                    Column("userid", users_userid_seq, primary_key=True, server_default=users_userid_seq.next_value()),
                    Column("username", String, nullable=False),
                    Column("password", String, nullable=False),
                    Column("email_address", String, nullable=False),
                    Column("recipes", String),
                    Column("points", Integer),
                    Column("liked_recipes", Integer))

# making the connection
with db.connect() as connection:
    
    select_query = users_table.select()
    
    results = connection.execute(select_query)
    
    for result in results:
        print(result)