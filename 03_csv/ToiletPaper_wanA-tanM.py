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
                newDict[float(row[1])] = float(row[0]) #i dont know if i need float, but there is a decimal so probably....
            counter += 1
    del newDict['Total']
    return newDict


def createArray(newDict):
    newArr = []
    for key in newDict.keys():# extract numbers. (percents)
        for x in range(int(key * 10)):
            newArr.append(newDict[key])
    return newArr

def randomPick(newArr):
    print(random.choice(newArr))


randomPick(createArray(createDict('occupations.csv')))
