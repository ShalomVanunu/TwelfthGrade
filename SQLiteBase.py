import sqlite3
#from sqlite3 import *

conn = sqlite3.connect('Class12.sqlite') #connection to DB

connect_to_db = conn.cursor() # set the point to the start of DB

connect_to_db.execute(""" CREATE TABLE classnames (
                            fist_name text,
                            last_name text,
                            email text ) """) #this creat the table

conn.commit() #do the state

conn.close()



