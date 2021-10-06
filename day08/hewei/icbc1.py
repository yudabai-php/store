# 导包
import pymysql
'''
    1.联网安装pymysql
        python  -m pip  install  pymysql
    2.导入pymysql包
    3.连接数据库
    4.创建控制台
    5.准备一条sql
    6.控制台执行sql语句

    6.1增，删，改
        提交数据
        6.2查询：
            提取数据：
            fetchall()
            fetchone()
            fetchmany(size)
    7.提交到数据库
    8.关闭资源
'''
# # 连接数据库
# con =pymysql.connect(host="localhost",user="root",password="123456",database="华夏全球银行")
# # 创建控制台
# curses=con.cursor()
# # 准备sql语句
# # sql=""
# # param=[]
# # 控制台执行sql语句
# curses.execute(sql,param)
# # 提交到数据库
# con.commit()
# # 关闭资源
# curses.close()
# con.close()
host="localhost",
user="root",
password="123456"
database="华夏全球银行"
def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = con.cursor()

    cursor.execute(sql,param)

    con.commit()
    cursor.close()
    con.close()


def select(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()

    cursor.execute(sql, param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    con.commit()
    cursor.close()
    con.close()










