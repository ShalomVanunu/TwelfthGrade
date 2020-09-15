#import requests
#from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://corona.mako.co.il/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


# Step1 - Get the HTML
get_html_page = requests.get("https://corona.mako.co.il/")
html_content = get_html_page.content


# Step2 - Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")
#print(soup.title)
print(soup.prettify())

p_sick = soup.find_all('p', class_="stat-total")
print(p_sick)