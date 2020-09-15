"""
this is the main program that import CORONA data
"""

import DB
import WebSite

corona_data = []
corona_data= WebSite.Get_Corona_Details('https://corona.mako.co.il/')
print(corona_data[0])

#DB.Create_Connection('COVID19.db')
query = f"""INSERT INTO covid19 (daily_man_sick,man_bad_sick,man_death,date)
VALUES ('{corona_data[1]}','{corona_data[2]}','{corona_data[3]}','{corona_data[4]}')
"""
DB.Execute_On_DB(DB.Create_Connection('COVID19.db'), query)
DB.Close_Connection(DB.Create_Connection('COVID19.db'))




