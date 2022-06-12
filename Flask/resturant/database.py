import sqlite3

db = sqlite3.connect('static/db/resturant.db')
sql = db.cursor()

with open("database.sql") as file:
    code = file.read()
    
for i in code.split(';'):
    try:
        sql.execute(i)
    except Exception as e:
        print(e)
    db.commit()
    for y in sql.fetchall():
        print(y)

db.close()
