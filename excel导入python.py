import xlrd
def excel(path):
  excel=xlrd.open_workbook(path)
  table=excel.sheets()[0]
  a=[]
  for i in range(0,table.nrows):
    a.append(table.row_values(i))
  return a
