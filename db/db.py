import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Palmeiras1!",
    database="sys"
)

def get_database_connection():
    return mydb
