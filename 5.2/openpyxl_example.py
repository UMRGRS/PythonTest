#5.2
'''
En este ejemplo hago uso de la librería openpyxl para crear un archivo xlsx que contiene
la información recabada sobre mis asistencias proveniente del portal de mi universidad
'''
import openpyxl

#Importamos la función GetData desde el ejemplo de selenium
from sa import GetData

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