from 统计报表数据库连接函数 import update
from 统计报表数据库连接函数 import select

sql = "insert into all_count value(%s,%s,%s,%s,%s,%s,%s) "

param = ['100.45','40','20.00','40.00','牛仔裤','风衣','T恤']

update(sql,param)


import pymysql
import xlwt

# 建立一个MySQL连接
conn = pymysql.connect(host='localhost', user='root', passwd='', database='t_jarvis')

# 获得游标
cursor = conn.cursor()

# 查询表中全部数据,赋值给xxx
sql = 'select * from xlsx'
cursor.execute(sql)
ddd = cursor.fetchall()
# 写入表格
wb = xlwt.Workbook()
st = wb.add_sheet("薪资管理")
# 大工程
for i in range(0, len(ddd)):
    for j in range(0, len(ddd[i])):
        st.write(i, j, str(ddd[i][j]))
# 保存，该开开，该关关
wb.save("薪资管理1.xls")
cursor.close()
conn.close()