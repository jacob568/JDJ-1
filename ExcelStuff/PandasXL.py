
import pandas as pd


def splitBuildingAndMeasurement(inputValue):
    words = inputValue.split()
    buildingName = words[0] + " " +  words[1]
    measurement = [2] + " " + words[3] + " " + words[4]
    return [buildingName, measurement]

def copy_range():
    #NAME OF EXCEL FILE, Set to a variable.
    excel_file_copy = 'TESTCOPY.xlsx'
    copy_sheet = pd.read_excel(excel_file_copy)

    #Unit Names & Measurements & Subject.
    area_measurements = pd.DataFrame(copy_sheet, columns= ['Comments'])
    subject = pd.DataFrame(copy_sheet, columns= ['Subject'])

    #Splitting the column into two & formatting
    area_measurements["Comments"] = area_measurements["Comments"].str.split(n=1,expand=False)
    result = pd.merge(area_measurements["Comments"] , subject["Subject"], left_index=True, right_index=True, how='outer')

    print(result)

    # This needs a for loop that iterates through "Comments" and formats the data properly for Output.
    #

    #print(area_measurements["Comments"])
    #print(subject)

copy_range()