import sys

sys.path.append('../db_fixture')

from mysql_db import DB

# create data
datas = {
    'sign_event': [
        {'id': 1, 'name': '红米 Pro 发布会', 'maximum': 2000, 'status': 1, 'address': '北京会展中心',
         'start_time': '2023-08-20 14:00:00'},
        {'id': 2, 'name': '可参加人数为 0', 'maximum': 0, 'status': 1, 'address': '北京会展中心',
         'start_time': '2023-08-20 14:00:00'},
        {'id': 3, 'name': '当前状态为关闭', 'maximum': 2000, 'status': 0, 'address': '北京会展中心',
         'start_time': '2023-08-20 14:00:00'},
        {'id': 4, 'name': '发布会已结束', 'maximum': 2000, 'status': 1, 'address': '北京会展中心',
         'start_time': '2020-08-20 14:00:00'},
        {'id': 5, 'name': '小米 5 发布会', 'maximum': 2000, 'status': 1, 'address': '北京国家会议中心',
         'start_time': '2023-08-20 14:00:00'},
    ],
    'sign_guest': [
        {'id': 1, 'realname': 'alen', 'phone': '13511001100', 'email': 'alen@mail.con', 'sign': 0, 'event_id': 1},
        {'id': 2, 'realname': 'has sign', 'phone': '13511001101', 'email': 'tom@mail.con', 'sign': 1, 'event_id': 1},
        {'id': 3, 'realname': 'tom', 'phone': '13511001102', 'email': 'tom@mail.con', 'sign': 0, 'event_id': 5},
    ],
}


# 遇到错误
# 1. pymysql.err.OperationalError: (1364, "Field 'create_time' doesn't have a default value")
#   插入数据时没有填入 create_time 字段，解决方法：
#       1. 在插入数据时增加 create_time 字段
#       2. 将数据库表 create_time 字段设置为添加记录时自动添加时间，执行语句：
#       ALTER TABLE guest_test.sign_guest MODIFY COLUMN create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP  NOT NULL;


# Insert Table datas
def init_data():
    db = DB()
    for table, data in datas.items():
        # print(type(table))
        # print(table)
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()
