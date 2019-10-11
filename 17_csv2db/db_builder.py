#Albert Wan
#SoftDev1 pd9
#K17 - No Trouble
#2019-10-10

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >


command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"
#create table in mySql
c.execute(command)
with open('courses.csv') as courseFile:
    courseReader = csv.DictReader(courseFile)
    #reads the file

    for row in courseReader:
#        exec = "INSERT INTO courses VALUES ('{}', {}, {});".format(x['code'], x['mark'], x['id'])
        command = "INSERT INTO courses VALUES(\"" + row['code'] + "\"" + ", " + row['mark'] + ", " + row['id'] + ");"
        #now, you populate values into the table
        c.execute(command)
command = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"
#create table in mySql
c.execute(command)
with open('students.csv') as studentFile:
    studentReader = csv.DictReader(studentFile)
    #reads the file
    for row in studentReader:
        exec = "INSERT INTO students VALUES(\"" + row['name'] + "\"" + ", " + row['age'] + ", " + row['id'] + ");"
        #now, you insert each value into the table (or populate)
        c.execute(exec)


db.commit() #save changes
db.close()  #close database
