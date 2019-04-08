# encoding=utf-8
'''
数据库连接
'''
import pymysql as pms


# 获取数据结果集
def get_datas(sql):
    # 1.打开数据库链接
    conn = pms.connect(host="192.168.159.39", user="clover", passwd="clover", database="ccjf_data", port=3306,
                       charset="utf8");
    #方法2：
    # db = pymysql.connect("localhost", "root", "root", "my_db")

    # 2.使用cursor方法获取操作游标
    cursor = conn.cursor();

    # 3.使用 cursor.execute方法执行 SQL
    cursor.execute(sql);

    # 4.使用 cursor.fetchall获取所需要的数据
    datas = cursor.fetchall();

    # 5.关闭链接
    cursor.close();
    # 返回数据
    return datas;


# 获取属性名
def get_fields(sql):
    # 1.打开数据库链接
    conn = pms.connect(host="192.168.159.39", user="clover", passwd="clover", database="ccjf_data", port=3306,
                       charset="utf8")
    # 2.获取游标
    cursor = conn.cursor();
    # 3.执行SQL
    cursor.execute(sql);
    # 4. 获取所需要的字段名称
    fields = cursor.description
    # 5.关闭链接
    cursor.close();
    return fields;
