import mysql.connector

def insert_record():
    print('Inserting record')

def update_record():
    print('Updating record')


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="skin_cancer_detection"
)

mycursor = mydb.cursor()

mycursor.execute('SELECT COUNT(*) FROM tbl_user WHERE username = %s',('nihal',))

count = mycursor.fetchone()

if count == 0:
   insert_record()
else:
   update_record()

mydb.close()

