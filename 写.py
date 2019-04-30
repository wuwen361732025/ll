from openpyxl import Workbook
wb = Workbook()
wb1=wb.create_sheet("biao1",0)
# wb1.title="test"
#添加数据的第一种方式
#添加数据
wb1["A3"]=4
wb1["A4"]=6
# 添加函数
wb1["A5"]='=sum(A3:A4)'





wb.save('1.xlsx')