import pymysql
import xlrd
host="localhost"
user="root"
password=""
database = "衣服商城"

# 针对于增，删，改
# def update(sql,param):
#     con = pymysql.connect(host=host,user=user,password=password,database=database)
#     cursor = con.cursor()
#     cursor.execute(sql,param)
#
#     con.commit()
#     cursor.close()
#     con.close()
#
#
# def select(sql,param,mode="all",size=1):
#     con = pymysql.connect(host=host, user=user, password=password, database=database)
#     cursor = con.cursor()
#     cursor.execute(sql, param)
#
#     if mode == "all":
#         return cursor.fetchall()
#     elif mode == "one":
#         return cursor.fetchone()
#     elif mode == "many":
#         return cursor.fetchmany(size)
#     con.commit()
#     cursor.close()
#     con.close()


def create(sql,param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    con.commit()
    cursor.close()
    con.close()
wb =  xlrd.open_workbook(filename=r"D:\a_py培训\py自动化测试\PY\数据库\day09【xlrd】\任务\2020年每个月的销售情况.xlsx",encoding_override=True)

for i in range(12):
    st=wb.sheet_by_index(i)
    row=st.nrows
    col=st.ncols
    sql='create table %s月(日期 char(10),服装名称 char(10),价格件 double(8,2),本月库存数量 int,销售量每日 int)'
    param=[i+1]
    create(sql,param)
    for j in range(1,row):
        sal='insert into %s月 values(%s,%s,%s,%s,%s)'

        param=[i+1,st.row_values(j)[0],st.row_values(j)[1],st.row_values(j)[2],st.row_values(j)[3],st.row_values(j)[4]]

        update(sal,param)