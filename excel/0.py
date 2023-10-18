import xlwings as xw

app=xw.App(visible=True,add_book=False)
wb=app.books.open(r'.\0.xlsx')

# wb就是新建的工作簿(workbook)，下面则对wb的sheet1的A1单元格赋值
print('sheets:{0}'.format(wb.sheets))

initial_sheet = wb.sheets['9月初数据']
initial_sheet_rows = initial_sheet.used_range.last_cell.row
names = []
for idx in range(2, initial_sheet_rows+1):
    names.append(initial_sheet.range('B{0}'.format(idx)).value)
print('initial_sheet_rows:{0}'.format(initial_sheet_rows))
print('names:{0}'.format(names))


add_sheet = wb.sheets['采购数据']
add_sheet_rows = add_sheet.used_range.last_cell.row
add_maps = {}
for idx in range(2, add_sheet_rows+1):
    name = add_sheet.range('A{0}'.format(idx)).value
    value = add_sheet.range('C{0}'.format(idx)).value
    add_maps[name] = value

print('add_maps:{0}'.format(add_maps))

initial_sheet.range('E1').value = '采购数量'
for idx in range(2, initial_sheet_rows+1):
    print('name:{0}, val:{1}'.format(initial_sheet.range('B{0}'.format(idx)).value,
                                     add_maps.get(initial_sheet.range('B{0}'.format(idx)).value, 0.0)))
    initial_sheet.range('E{0}'.format(idx)).value = add_maps.get(initial_sheet.range('B{0}'.format(idx)).value, 0.0)

wb.save(r'.\1.xlsx')
wb.close()
app.quit()