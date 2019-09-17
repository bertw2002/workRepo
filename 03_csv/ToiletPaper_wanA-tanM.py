#Albert Wan
#SoftDev1 pd9
#K06 -- Divine your Destiny!
#2019-09-17


import random
import csv

def createDict(csvFile):
    newDict = {}
    with open(filename) as oldcsv:
        counter = 0 # counter to skip first row, because it's just the heading
        csvRead = csv.reader(oldcsv, delimiter = ',')
        for row in csvRead:
            if counter > 0:
                newDict[row[0]] = float(row[1]) #i dont know if i need float, but there is a decimal so probably....
            counter += 1
    del newDict['Total']
    return newDict


def createArray(newDict):
    
