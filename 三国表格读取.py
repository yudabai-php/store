import pymysql
import xlwt

# 建立一个MySQL连接
conn = pymysql.connect(host='localhost', user='root', passwd='', database='company')

# 获得游标
cursor = conn.cursor()

# 查询表中全部数据,赋值给xxx
sql = 'select * from t_employees'
cursor.execute(sql)
ddd = cursor.fetchall()
# 写入表格
wb = xlwt.Workbook()
st = wb.add_sheet("用户管理")
# 大工程
for i in range(0, len(ddd)):
    for j in range(0, len(ddd[i])):
        st.write(i, j, str(ddd[i][j]))
# 保存，该开开，该关关
wb.save("三国集团.xls")
cursor.close()
conn.close()