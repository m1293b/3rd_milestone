import psycopg2
# import app.py

# connect to database

connection = psycopg2.connect(database="no39_recipes")

# build a cursor object of the database

cursor = connection.cursor()

# fetch the results (multiple)

results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection

connection.close()

# print results

for result in results:
    print(result)