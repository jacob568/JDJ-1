
# Importing Modules
import pandas as pd
import numpy as np

#NAME OF EXCEL FILE, Set to a variable, Eventually this needs to cycle through a given directory for multiple files.
excel_file_copy = 'TESTCOPY.xlsx'
copy_sheet = pd.read_excel(excel_file_copy)

def copy_range():
    #Returns the entire dataset.
    #print(copy_sheet.head())

    index = copy_sheet.index
    col = copy_sheet.columns
    values = copy_sheet.values


    copy_sheet_cols = pd.DataFrame(copy_sheet, ['ID', 'Parent', 'Subject', 'Page Label', 'Page Index',
                          'Lock', 'Status', 'Tick Mark','Author',
                          'Date', 'Colour', 'Comments'])

    split_names = copy_sheet['Comments'].str.split()
    subject = copy_sheet['Subject']

    print(split_names)
    joined_names = split_names.str.get(0) + " " + split_names.str.get(1)
    measurements = split_names.str.get(2)
    print(joined_names)
    print(measurements)

    # Results almost works, displays names twice though, for example (55  Unit 601   Unit 601   Floor Area     426.54)

    results = pd.merge(pd.merge(joined_names, subject, left_index=True,
                       right_index=True, how='outer', on=joined_names),
                       measurements, how='outer', on= joined_names,
                       left_index=True)

    print(results)

copy_range()