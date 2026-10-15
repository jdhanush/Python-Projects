from openpyxl import Workbook
from win32com.client import Dispatch

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "YouTube" 

workbook.save(filename='hello_youtube.xlsx')

# cell = sheet["A1"]
# print(cell.value)
xl = Dispatch("Excel.Application")
xl.Visible = True

wb = xl.Workbooks.Open(r"E:\Dhanush\Python Concepts\12. Automation Projects\Matador Software-YT Channel\excel automation\hello_youtube.xlsx")

