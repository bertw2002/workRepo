#Albert Wan, Kenneth Chin
#SoftDev1 pd9
#K18 -- Average
#2019-10-11

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
from utl.csvrw import insertAll, printTable
DB_FILE="data.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops


#computes student's average
average = """SELECT name, students.id, SUM(mark) / COUNT(mark)
    FROM students, courses
    WHERE students.id = courses.id
    GROUP BY courses.id;"""

newTable = "CREATE TABLE stu_avg(id INTEGER, average INTEGER)"

# creates table stu_avg
# c.execute(newTable)
c.execute(average)

averages = c.fetchall()
print (averages)

for x in averages:
    print (x[0], ":",  x[1], ":", x[2])
    insert = "INSERT INTO stu_avg VALUES(" + str(x[1]) + "," +  str(x[2]) + ")" + ";"
    c.execute(insert)


db.commit() #save changes
db.close()  #close database
