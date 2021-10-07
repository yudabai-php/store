import pymysql

host = "localhost"
user = "root"
password = ""
database = "衣服商城"


# 针对增、删、改
def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = con.cursor()         #创建操作台
    cursor.execute(sql,param)     #添加数据

    con.commit()       #提交数据
    cursor.close()
    con.close()

def select(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()  # 创建操作台
    cursor.execute(sql, param)  # 添加数据

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)

    con.commit()  # 提交数据
    cursor.close()
    con.close()






