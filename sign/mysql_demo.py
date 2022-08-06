import pymysql.cursors

# description 该表应用的 test 数据库

# 创建表
"""
CREATE TABLE test.sign_guest (
 realname varchar(50),
 phone varchar(16),
 email varchar(30),
 sign boolean,
 event_id int(32) primary key,
 create_time datetime
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
"""

# Connect to the database
connection = pymysql.connect(
    user='root',
    password='admin',
    host='127.0.0.1',
    port=3306,
    db='test',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = 'INSERT INTO sign_guest(realname, phone, email, sign, event_id, create_time) VALUE ("alen", "18800110001", "alen@mail.com", 0, 1, NOW());'
        cursor.execute(sql)
        # connection is not auto commit by default. So you must commit to save your changes.
        connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = 'SELECT realname, phone, email, sign FROM sign_guest WHERE phone=%s'
        cursor.execute(sql, ('18800110001',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
