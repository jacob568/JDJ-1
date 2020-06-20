'''
from openpyxl import load_workbook
wb2 = load_workbook("TEST.xlsx")
print (wb2.sheetnames)

Data = wb2.get_sheet_by_name("Data")
#Individual Grabs
Type = Data.cell(row=2 ,column=2).value
Floor_Area = Data.cell(row=2, column=9).value
HLF = Data.cell(row=2, column=13).value
'''
"""
#For loop that loops through ALL
for Titles in range(9, 28):
    print(Data.cell(row=2, column=Titles).value)

print(Type + ("|"), Floor_Area +("|"), HLF + ("|"))

"""

import openpyxl

# COPY
wb = openpyxl.load_workbook("TESTCOPY.xlsx")  # Add file name
sheet = wb["TESTCOPY"]  # Add Sheet name

"""
# PASTE
template = openpyxl.load_workbook("TESTPASTE.xlsx")  # Add file name
temp_sheet = template["DATA"]  # Add Sheet name

"""

def copyRange(startCol, startRow, endCol, endRow, sheet):
	rangeSelected = []
	for i in range(startRow, endRow + 1, 1):
		rowSelected = []
		for j in range(startCol, endCol + 1, 1):
			rowSelected.append(sheet.cell(row=i, column=j).value)
			print(sheet.cell(row = i,column = j).value)
			#if sheet.cell(row = i, column = j).value == "None":

		rangeSelected.append(rowSelected)
        #FFS HOW DO I PRINT LISTS

#Building and measurement are stored in the same cell.
#This function separate the two values into their own variables
def splitBuildingAndMeasurement(inputValue):
	words = inputValue.split()
	buildingName = words[0] + " " +  words[1]
	measurement = words[2] + " " + words[3] + " " + words[4]

	print("The building is called: " + buildingName)
	print("The measurements are: " + measurement)


def is_number(s):
    if s.isdigit():
    	return False
    else:
    	return True


splitBuildingAndMeasurement("Unit 002 884.27 sq m")
#copyRange(1, 2, 1, 57, sheet)

#startcol = 3
#startRow = 2
#endCol = 3
#end_Row = 10