
"""
this functions deals with the corona data

"""
import requests
from bs4 import BeautifulSoup
import datetime

def Get_Corona_Details(URL):
    corona_data =[]
    #Step1 - Get HTML CODE
    get_html_page = requests.get(URL)
    html_content = get_html_page.content
    #print(html_content)

    # Step2 - Parse the HTML page
    soup = BeautifulSoup(html_content, "html.parser")
    #print(soup.prettify())

    # Get Title of Page

    title = soup.title
    corona_data.append(title.get_text())
    #print(title.get_text())

    p_sick = soup.find_all('p',class_="stat-total")
    man_sick = p_sick[0].get_text()
    bad_sick_man =  p_sick[1].get_text()
    corona_data.append(man_sick)
    corona_data.append(bad_sick_man)
 #   print(man_sick)
 #   print(bad_sick_man)

    death = soup.find_all('strong')
    man_death = death[1].get_text()
    corona_data.append(man_death)
  #  print(man_death)

    date = datetime.datetime.now().strftime("%x")
    corona_data.append(date)
    return corona_data