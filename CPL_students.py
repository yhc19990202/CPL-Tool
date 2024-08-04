import json
import openpyxl

def read_students(filename):
	wb = openpyxl.load_workbook(filename)
	sheet = wb.worksheets[0]

	student_id = []
	for cell in sheet['A']:
		if cell.value is not None:
			student_id.append(cell.value)
	return student_id

if __name__ == '__main__':
	x = read_students('./excel/student.xlsx')
	print(x)