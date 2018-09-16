import pymysql.cursors

# connect to the database
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='YUke1030',
    db='prac',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        sql = "SELECT mark FROM mark"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

    connection.commit()

    # with connection.cursor() as cursor:
    #     sql = "SELECT id, password FROM users WHERE email=%s"
    #     cursor.execute(sql, ('jg@mail', 10))
    #     result = cursor.fetchone()
    #     print(result)

finally:
    connection.close()
