import mysql.connector

host = "sql11.freemysqlhosting.net"
user = "sql11494945"
pasword = "KHKhri1XFc"
database = "sql11494945"

db = mysql.connector.connect(
    host=host,
    user=user,
    passwd=password,
    database=database
)
