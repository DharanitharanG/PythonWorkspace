import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="hadoop",
  passwd="hadoop",
  database="TrainingInstitute"
)

mycursor = mydb.cursor()

sql = "create table courseDetails(courseid int primary key,coursename varchar(20))"
sql2 = "create table studentsEnquiry(studentid int primary key,studname varchar(20),phonenum int,courseInterested int)"
sql3 = "create table studentsEnrollment(enrollid int primary key,studid int,courseenrolled int)"

selectQ = "select * from Table"
mycursor.execute(sql)
mycursor.execute(sql2)
result = mycursor.execute(selectQ)

records =[]
for x in result:
 records.append(x.tolist())

mydb.commit()
