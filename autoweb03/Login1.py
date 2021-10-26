import xlrd
# from openpyxl import load_workbook
wb = xlrd.open_workbook(r'D:\Python\Pythondaim\autoweb03\HKR.xlsx')
class InitPage:
    Login_Success_data =[]
    sheet = wb.sheet_by_name("login")
    rows = sheet.nrows
    for i in range(1,rows):
        c = sheet.row_values(i)
        print(c)
        username = str(c[0])
        password = str(c[1])
        expect = str(c[2])
        b = {'username':username,'password':password,'expect':expect}
        Login_Success_data.append(b)

    #     write = load_workbook(filename=r'D:\Python\Pythondaim\autoweb03\HKR.xlsx')
    #     print(write.sheetnames)
    #
    #     sheet = write.active
    #
    #     call = sheet['H3']
    #     call.value = '白告子'
    #
    # write.save(filename=r'D:\Python\Pythondaim\autoweb03\HKR.xlsx')

    # Login_error_data = []
    # sheet = wb.sheet_by_name("Error")
    # rows = sheet.nrows
    # for i in range(1, rows):
    #     c = sheet.row_values(i)
    #     print(c)
    #     username = str(c[0])
    #     password = str(c[1])
    #     expect = str(c[2])
    #     a = {'username': username, 'password': password, 'expect': expect}
    #     Login_error_data.append(a)





    # Login_error_data = xlrd
