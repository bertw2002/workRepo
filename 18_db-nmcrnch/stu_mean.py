#Albert Wan, Kenneth Chin
#SoftDev1 pd9
#K18 -- Average
#2019-10-11

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="school.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
