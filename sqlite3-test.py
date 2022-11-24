import sqlite3, os

db_file = os.path.join(os.path.dirname(__file__), 'lecture.db')
# if os.path.isfile(db_file):
#     os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# write
# try:
#     cursor.execute('create table test (id varchar(20) primary key, name varchar(20))')
#     cursor.execute("insert into test (id, name) values ('3','john')")
#     print(cursor.rowcount)
#     cursor.close()
#     conn.commit()
#     conn.close()
# except:
#     print('error')


# read
cursor.execute("create table if not exists lecture1 (time varchar(20),place varchar(20),theme varchar(20),department varchar(20),url varchar(20))")  #speaker varchar(20),
# cursor.execute("insert into tb1 (id,time,place) values ('1','12:30','科技楼')")
# data = cursor.execute("select * from tb1 where id = ?",('1',))
# cursor.execute('create table tb2 (id varchar(20),name varchar(20))')
# cursor.execute("insert into tb2 (id,name) values ('3','name')")
# cursor.execute("delete from tb2")

# data=cursor.execute('select * from tb2')
# values = cursor.fetchall()
# print(type(data))
data = []
# cursor.execute("insert into lecture1 (time,place,theme,department,url) values ('12:39','嫩嫩','大司农','此风暴','的嘲弄')")
select = cursor.execute("select * from lecture1")
for row in select:
    if row:
        data.append(row)

print(data)

# for row in data:
#     print(row)
# print(type(values[0][1]))

cursor.close()
conn.commit()
conn.close()