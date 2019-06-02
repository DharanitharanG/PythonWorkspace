import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="hadoop",
  passwd="hadoop",
  database="training"
)

mycursor = mydb.cursor()

sql = "create table employee (id int, name string)"

mycursor.execute(sql)

mydb.commit()
