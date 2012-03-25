import csv

def writeTemplateFile(outputFile, data):
    filePath = 'output/'
    fileHandle = filePath + outputFile
    f = open(fileHandle, 'w')
    f.write(data)
    return True
    
def parseTextFile(inFile):
    # Generates list of items from a text file
    items = []
    reader = csv.reader(open(inFile, "rb"))
    for row in reader:
        items.append(row)
    return items

def loadCodeFromFile(inFile):
    # Generates list of items from a text file
    data = []
    dataStructure = open(inFile, "rb")
    data = dataStructure
    return data

    