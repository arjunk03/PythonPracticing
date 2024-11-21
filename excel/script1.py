import openpyxl

work_book = openpyxl.load_workbook("dataset/company_revenue.xlsx")
print(work_book.sheetnames)

sheet_obj = work_book["revenue"]
print(sheet_obj.title)

print(sheet_obj["A1"].value)
cell = sheet_obj["B2"]

print(cell.row)
print(cell.column)
print(cell.number_format)
print(cell.coordinate)
print(cell.data_type)
