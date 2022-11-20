
import csv, os

class csvParser():
    
    def __init__(self):
        self.reader = None
        self.writer = None
    
    
    def open_file(self, file_name: str):
        file = open(file_name)
        # General method to parse
        self.reader = csv.reader(file)
        self.writer = csv.writer('FileToWriteTo')
        data = list(self.reader)
        print(f'Data{data}')

        # loop through the files
        for file in os.listdir('.'):
            if not file.endsWith('.csv'):
                continue

    def write_to_file(self, file):
        csvRow = []
        csvFile = open(file)
        readerObj = csv.reader(csvFile)
        # TODO: Refactor to use context manager
        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csvRow.append(row)
        csvFile.close()

