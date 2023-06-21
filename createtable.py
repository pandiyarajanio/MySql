import mysql.connector
mysdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ndiyarajan2002",
    database="db1")
mycursor=mysdb.cursor()
mycursor.execute("create table Employee(id int auto_increment primary key, name varchar(10),salary int(50))")
