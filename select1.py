# import mysql.connector
# mysdb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="demo")
# mycursor=mysdb.cursor()
# mycursor.execute("select name from employee;")
# mylist=mycursor.fetchone()
# for i in mylist:
#     print(i)


# import mysql.connector
# mysdb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="demo")
# mycursor=mysdb.cursor()
# mycursor.execute("select salary from employee;")
# mylist=mycursor.fetchall()
# for i in mylist:
#     print(i)


# import mysql.connector
# mysdb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="demo")
# mycursor=mysdb.cursor()
# mycursor.execute("select * from employee;")
# mylist=mycursor.fetchall()
# for i in mylist:
#     print(i)

# import mysql.connector
# mysdb=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     database="demo")
# mycursor=mysdb.cursor()
# mycursor.execute("select * from employee order by name;")
# mylist=mycursor.fetchall()
# for i in mylist:
#     print(i)



import mysql.connector
mysdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="demo")
mycursor=mysdb.cursor()
mycursor.execute("select * from employee order by name desc;")
mylist=mycursor.fetchall()
for i in mylist:
    print(i)