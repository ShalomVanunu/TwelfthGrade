"""
this program deal the CORONA DB

"""

import sqlite3
from sqlite3 import Error # module Error of SQlite
#from sqlite3 import *

## DB Connection

def Create_Connection(path):
    try:
        connection = sqlite3.connect(path)
        print('Connection to DB file is OK')
    except Error as e:
        print(f'The Error {e} occurred')
    return connection

def Execute_On_DB(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(" The Query Executed Succesfully")
    except Error as e:
        print(f'The Error {e} occurred')

def Close_Connection(connection):
    try:

        connection.close()
        print("the Connection DB closed")
    except Error as e:
        print(f'The Error {e} occurred')

