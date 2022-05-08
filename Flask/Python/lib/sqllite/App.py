import sqlite3

database = sqlite3.connect('voting.db')
sql = database.cursor()

with open('App.sql') as file:
    code = file.read()

sql.execute(code)
# sql.execute('SELECT * FROM login_participa]'bzcx)
for i in sql.fetchall():
    print(i)

sql.execute(code)
database.commit()
database.close()
