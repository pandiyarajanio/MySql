import mysql.connector
mysdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ndiyarajan2002",
    database="db1")
mycursor=mysdb.cursor()
nm=input("Enter Name:")
sal=int(input("Enter salary:"))
mycursor.execute("UPDATE employee set name=%s,salary=%s where id=2;",(nm,sal))
mysdb.commit()
mylist=mycursor.fetchall()
for i in mylist:
    print(i)



# import mysql.connector
# mysdb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="demo")
# mycursor=mysdb.cursor()
# nm=input("Enter Name:")
# sal=int(input("Enter salary:"))
# mycursor.execute("UPDATE employee set name=%s,sal=%swhere id=1;",(nm,sal))
# mysdb.commit()
# mylist=mycursor.fetchall()
# for i in mylist:
#     print(i)