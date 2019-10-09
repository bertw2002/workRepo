#Albret Wan
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


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================


with open('courses.csv', newline="") as courseFile:
    courseReader = csv.DictReader(courseFile)
    #reads the file
    command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"
    #create table in mySql
    c.execute(command)
    for x in courseReader:
        exec = "INSERT INTO courses VALUES({{code}}, {{mark}}, {{id}})"
        #now, you populate values into the table
        c.execute(exec)

with open('students.csv', newline="") as studentFile:
    courseReader = csv.DictReader(courseFile)
    #reads the file
    command = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"
    #create table in mySql
    c.execute(command)
    for x in courseReader:
        exec = "INSERT INTO students VALUES({{name}}, {{age}}, {{id}})"
        #now, you insert each value into the table (or populate)
        c.execute(exec)


db.commit() #save changes
db.close()  #close database
