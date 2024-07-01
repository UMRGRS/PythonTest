#5.2
import openpyxl
from selenium_attendance import GetData

data = GetData()

book = openpyxl.Workbook()

sheet = book.active

for row in data:
    sheet.append(row)

for column in sheet.columns:
    max_length = 0
    column_letter = column[0].column_letter
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 3)
    sheet.column_dimensions[column_letter].width = adjusted_width

book.save('test_files/asistencias.xlsx')