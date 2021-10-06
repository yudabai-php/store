from mysql import update
from mysql import select
from mysql import insert

sql = "insert into parson value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

param = [1200001,'ych',123456,'中s国','北s京','沙阳s路','0201',5000,'2021-01-11 17:50:45','中国银行']

insert(sql,param)