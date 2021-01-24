
import csv, os

class csvParser():
    # which csv to open
    file = open('')
    # General method to parse
    reader = csv.reader(file)
    writer = csv.writer('FileToWriteTo')
    data = list(reader)
    print(data)

    # loop through the files
    for file in os.listdir('.'):
        if not file.endsWith('.csv'):
            continue

    #parse out rows in a csv file
    csvRow = []
    csvFile = open(file)
    readerObj = csv.reader(csvFile)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRow.append(row)
    csvFile.close()

