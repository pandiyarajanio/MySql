import mysql.connector
mysdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ndiyarajan2002",
    database="db1")
mycursor=mysdb.cursor()
nm=input('Enter Your Name :')
sal=int(input("Enter Your salary :"))
mycursor.execute('insert into employee(name,salary)values(%s,%s)',(nm,sal))
mysdb.commit()
print(mycursor.rowcount,'Record Interted')