import random

def randPerson(arr):
    weirdNamesint = random.randint(0, 2)
    arr1 = list()
    for wdName in arr:
        arr1.append(wdName)
    #print(arr1)
    weirdName = arr1[weirdNamesint]
    #print(weirdName)
    arrNames = arr[weirdName]
    #print(arrNames)
    nameLength = len(arrNames)
    print(arrNames[random.randint(0, nameLength)])

KREWES = {
    'orpheus': ['Emily', 'Kevin', 'Vishwaa', 'Eric', 'ray', 'Jesse', 'Tiffany',
        'Amanda', 'Junhee', 'Jackie', 'Tyler', 'Emory', 'Ivan', 'Elizabeth',
        'Pratham', 'Shaw', 'Eric', 'Yaru', 'Kelvin', 'Hong Wei', 'Michael',
        'Kiran', 'Amanda', 'Joseph', 'Tanzim', 'David', 'Yevgeniy'],
    'rex': ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo',
            'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham',
            'Michael', 'Matthew', 'Jionghao', 'Devin', 'David', 'Jacob', 'Will',
            'Hannah', 'Alex'],
    'endymion': ['Grace', 'Nahi', 'Derek', 'Jun Tao', 'Connor', 'Jason',
            'Tammy', 'Albert', 'Kazi', 'Derek', 'Brandon', 'Kenneth', 'Lauren',
            'Biraj', 'Jeff', 'Jackson', 'Taejoon', 'Kevin', 'Jude', 'Sophie', 'Henry',
            'Coby', 'Manfred', 'Leia', 'Ahmed', 'Winston']
            }
randPerson(KREWES)
