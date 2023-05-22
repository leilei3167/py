# python内置sqlite和驱动
# import sqlite3
#
# conn = sqlite3.connect("test.db")
#
# # 创建一个cursor
# cursor = conn.cursor()
# # 使用cursor来执行sql语句
# cursor.execute(r"create table user (id varchar(20) primary key,name varchar(20))")
# cursor.execute(r"insert into user (id, name) values ('1', 'Michael')")
# print(cursor.rowcount)
# conn.commit()
# cursor.close()
# conn.close()

import mysql.connector

conn = mysql.connector.connect(user="root", password="123456", database="test")
