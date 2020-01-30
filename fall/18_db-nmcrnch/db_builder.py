# Albert Wan & Kenneth Chin
# SoftDev1 pd9
# K#17 - No Trouble
# 2019-10-07

from sqlite3 import connect, Row
from utl.csvrw import insertAll, printTable

# Setup the database
DB_FILE = "data.db"

db = connect(DB_FILE)
db.row_factory = Row
c = db.cursor()

# Add the csv and create a table to store the csv if it does not exist
insertAll("data/courses.csv", "courses", db)
insertAll("data/students.csv", "students", db)

# Print the database
print("courses table")
printTable("courses", c)
print("\nstudents table")
printTable("students", c)
q = """SELECT name, students.id, mark
FROM students, courses
WHERE students.id = courses.id;"""



foo = c.execute(q)
print(foo)
# Save and exit the database
db.commit()
db.close()