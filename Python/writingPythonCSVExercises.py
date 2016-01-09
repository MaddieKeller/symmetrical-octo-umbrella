import os, csv

#the path to the script
currentPath = os.path.dirname(os.path.abspath("writingPthonCSVExercies.py"))

#the path to the CSV File
outputCsv = currentPath +"\spreadsheet.csv"

'''
wb deletes the current file and writes to it
rb reads the current file
'''

#create and open the file
csvFile = open(outputCsv,'wb')

#create writer object
writer = csv.writer(csvFile,delimiter=",")

#data to go in CSV file
row_1 = [1, 'Row 1',123]
row_2 = [2,'Row 2',456]
row_3 =[3,'Row 3',789]

#write rows to the CSV File
rows=[row_1, row_2, row_3]
for row in rows:
    writer.writerow(row)

exit()

