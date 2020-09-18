import sqlite3
#from sqlite3 import *

conn = sqlite3.connect('TwelfthGrade.sqlite') #connection to DB

connect_to_db = conn.cursor() # set the point to the start of DB

connect_to_db.execute(""" INSERT INTO classnames VALUES (
                            'SHALOM',
                            'VANUNU',
                            'SHALOMV@gmail.com' ) """) #this INSRERT the table

conn.commit() #do the state

conn.close()



