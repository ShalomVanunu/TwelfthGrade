import requests
from bs4 import BeautifulSoup


# Step1 - Get the HTML
get_html_page = requests.get("https://corona.mako.co.il/?partner=NewsNavBar")
html_content = get_html_page.content

# Step2 - Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")
print(soup)
#print(soup.prettify())
