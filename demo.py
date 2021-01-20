from mysql import connector

mydb = connector.connect(host='localhost', user='root', password='1234', database='sql_hr')
mycursor = mydb.cursor()
mycursor.execute('select *from employees')
result = mycursor.fetchall()
for i in result:

 print(i)
 print(i)
