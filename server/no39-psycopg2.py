import psycopg2
import app.py

# connect to database

connection = psycopg2.connect(dbname="no39_recipes")

# build a cursor object of the database

cursor = connection.cursor()

# fetch the restults (multiple)

results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection

connection.close()

# print restults

for result in results:
    print(result)