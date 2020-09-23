import sqlite3
#from sqlite3 import *

conn = sqlite3.connect('Our_data.db') #connection to DB

connect_to_db = conn.cursor() # set the point to the start of DB

#connect_to_db.execute('SELECT * FROM employee_records')
#connect_to_db.execute("""INSERT INTO employee_records  VALUES (4,'Joan','Electronics', 3)""")
connect_to_db.execute(""" DELETE FROM employee_records WHERE STARS=4""")

conn.commit() #do the state

conn.close() #close the connction to db

w ='ttt'
print('dd'.f)

