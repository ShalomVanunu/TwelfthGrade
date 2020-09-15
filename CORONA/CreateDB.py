"""
this prog Create the DB
its run once a time

"""
import sqlite3

connection  = sqlite3.connect('COVID19.db')
c = connection.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS covid19 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            daily_man_sick TEXT,
            man_bad_sick TEXT,
            man_death TEXT,
            date TEXT )
""")

connection.commit()
connection.close()
