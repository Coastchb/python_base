#coding=utf-8
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",password="Mysql1991",
    database="Toutiao")
cursor = conn.cursor()

### fetch from database
sql = """
select * from blogs
"""
# 执行SQL语句
ret = cursor.execute(sql)
if (ret > 0) :
    for item in cursor.fetchall():
        print(item)

# 关闭光标对象
cursor.close()
# 关闭数据库连接
#conn.close()


### insert to database
sql = '''
insert into blogs(id, title, abstract, tag, link, score, published_date) values(%s, %s, %s, %s, %s, %s, %s) 
'''
cursor = conn.cursor()
ret = cursor.execute(sql, ["11", "aaa", "AAA", "html", "aaa.com", "3", "2019-12-20"])
print(ret)
conn.commit()
cursor.close()
conn.close()