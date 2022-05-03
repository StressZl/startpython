#! /usr/bin/python
# -*- coding: UTF-8 -*-
import re
import pymysql
from zhon import hanzi
'''
进入后显示数据库  SHOW DATABASES;
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| shige              |
| sys                |
+--------------------+
5 rows in set (0.03 sec)
选择数据库  USE 数据库名字;
mysql> use shige;
Database changed
mysql> show tables;
+-----------------+
| Tables_in_shige |
+-----------------+
| runoob_tbl      |
| 诗经            |
+-----------------+
2 rows in set (0.02 sec)
例子 创建用户对TUTORIALS这个数据库有全部权限
mysql> GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP
    -> ON TUTORIALS.*
    -> TO 'zara'@'localhost'
    -> IDENTIFIED BY 'zara123';
展示表的字段属性
mysql> desc 诗经;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int         | NO   | PRI | NULL    |       |
| title | varchar(45) | NO   |     | NULL    |       |
| value | varchar(45) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.01 sec)
MySQL 中修改表字段名的语法规则如下：
ALTER TABLE <表名> CHANGE <旧字段名> <新字段名> <新数据类型>;
修改字段的数据类型就是把字段的数据类型转换成另一种数据类型。在 MySQL 中修改字段数据类型的语法规则如下：
ALTER TABLE <表名> MODIFY <字段名> <数据类型>;
删除字段是将数据表中的某个字段从表中移除，语法格式如下：
ALTER TABLE <表名> DROP <字段名>;
在末尾添加字段
一个完整的字段包括字段名、数据类型和约束条件。MySQL 添加字段的语法格式如下：
ALTER TABLE <表名> ADD <新字段名><数据类型>[约束条件];
在开头添加字段
MySQL 默认在表的最后位置添加新字段，如果希望在开头位置（第一列的前面）添加新字段，那么可以使用 FIRST 关键字，语法格式如下：
ALTER TABLE <表名> ADD <新字段名> <数据类型> [约束条件] FIRST;
在中间位置添加字段
MySQL 除了允许在表的开头位置和末尾位置添加字段外，还允许在中间位置（指定的字段之后）添加字段，此时需要使用 AFTER 关键字，语法格式如下：
ALTER TABLE <表名> ADD <新字段名> <数据类型> [约束条件] AFTER <已经存在的字段名>;
ALTER TABLE <表名> ALTER column <字段名> SET Default 默认值;
ALTER TABLE <表名> ALTER column <字段名> DROP Default;
'''


def get_shijilist(path='诗经.txt', encoding='UTF8'):
    content = ''
    peace = ''
    siji_list = []

    def _add_shiji_dict(l: list, titles: str, contont: str, ipeace: str):
        l.append({'标题': titles,
                  '内容': contont,
                  '篇章': ipeace})

    with open(path, 'r', encoding=encoding) as file:
        contents = file.read()
        contents = contents.split('--------------------------------------------------')[-1]
        contents_list = ([x.strip() for x in contents.split('\n') if x])
        for val in contents_list:
            if val.startswith('∷'):
                if content:
                    _add_shiji_dict(siji_list, title, content, peace)
                content = ''
                title = val.split('∷')[-1]
            elif re.findall(hanzi.sentence, val):
                content += val
            else:
                peace = val
        _add_shiji_dict(siji_list, title, content, peace)
    return siji_list


def insert_info(db, cmd="select * FROM 诗经"):
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(cmd)
        # 提交到数据库执行
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data1 = cursor.fetchall()
        return data1
    except:
        # 发生错误时回滚
        db.rollback()


def exec_mysql_cmd(host='localhost', port=3306, db='shige', user='root', password='Zlsgdsb@123',
                   cmd="select *  from 诗经"):
    with pymysql.connect(host=host,
                         user=user,
                         password=password,
                         database=db, port=port) as db:
        x = insert_info(db, cmd)
        return x
# name = "'Admin'"
# cmd = "select passwd from 用户管理 where name=%s" % name
# info = exec_mysql_cmd(cmd=cmd)
# print(info)
# data_list = get_shijilist()
# cmd_o = 'INSERT INTO 诗经  ' \
#           '(title, value,peace)  ' \
#           'VALUES  '
# for i in data_list:
#     cmd = cmd_o + '("%s","%s","%s")' % (i['标题'], i['内容'], i['篇章'])
#     cmd.encode('utf8')
#     print(cmd)
#     exec_mysql_cmd(cmd=cmd)


