import mysql.connector
mysdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ndiyarajan2002"
)
mycursor=mysdb.cursor()
mycursor.execute("create database db1")

































































