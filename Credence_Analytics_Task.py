import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="sonam",password="1234",database="employee")

mycursor=mydb.cursor()


mycursor.execute("select * from employee")

result = mycursor.fetchall() 


for i in mycursor:
	print(i)
