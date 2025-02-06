import mysql.connector


def connect_mysql():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="skin_cancer_detection"
    )
    return db


def save_user(form_data):
    print('Saving user data')

    name = form_data['name']
    phone = form_data['phone']
    email = form_data['email']
    password = form_data['password']

    print('Request data ------------------')
    print(name)
    print(phone)
    print(email)
    print(password)

    mydb = connect_mysql()
    mycursor = mydb.cursor()
    mycursor.execute('SELECT COUNT(*) FROM tbl_user WHERE email = %s', (email,))

    count = mycursor.fetchone()[0]

    print('Record count', count)

    if count > 0:
        return {
            'hasError': True,
            'error': 'User already exist'
        }

    sql = "INSERT INTO tbl_user (name, email, password, mobile) VALUES (%s, %s, %s, %s)"
    value = (name, email, password, phone)
    mycursor.execute(sql, value)
    mydb.commit()
    print('Data inserted')
    return {
        'hasError': False
    }
