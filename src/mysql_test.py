import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="skin_cancer_detection"
)

print('Mysql connected')

mycursor = mydb.cursor()

sql = "INSERT INTO tbl_user (name, username, email, password, mobile) VALUES (%s, %s, %s, %s, %s)"
value = ('Dr.nihal', 'ram123', 'ram@gmail.com', 'welcome','1234567890')

mycursor.execute(sql, value)

mydb.commit()


print(mycursor.rowcount, "was inserted.")