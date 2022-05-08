import sqlite3

database = sqlite3.connect('databases\\voting.db')
sql = database.cursor()

with open('App.sql') as file:
    code = file.read().split(';')

for i in code:
    sql.execute(i)
    for i in sql.fetchall():
        for y in i:
            print(y, end=' ')
        print()


database.commit()
database.close()
