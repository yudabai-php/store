import xlrd
import xlwt
# 存数据类

class loginData:
    dic = {}
    book = xlrd.open_workbook(r'D:\Python\Pythondaim\autoweb03\HKR.xlsx')
    data_xlsx = book.sheet_by_name('Sheet1')
    for i in range(1, data_xlsx.nrows):
        account = data_xlsx.cell(i, 0).value
        password = data_xlsx.cell(i, 1).value
        value = data_xlsx.cell(i, 2).value
        aa = {'account': account, 'password': password, 'value': value}
        print(aa)
        dic[i] = aa

    successLoginData = {}
    errorLoginData = {}
















