import sqlite3

db = sqlite3.connect('db.sqlite3')
sql = db.cursor()

sql.execute("   DROP TABLE authentication;")

db.commit()
db.close()
