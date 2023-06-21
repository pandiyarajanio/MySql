import mysql.connector
mysdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ndiyarajan2002",
    database="db1")
mycursor=mysdb.cursor()
rm=input('enter name :')
mycursor.execute('delete from employee where name=%s',(rm,))
mylist=mycursor.fetchall()
for i in mylist:
    print(i)
mysdb.commit()
print(mycursor.rowcount,'record delete')