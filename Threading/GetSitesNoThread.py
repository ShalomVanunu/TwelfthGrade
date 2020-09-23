"""
עליכם קריאה של 10 אתרים ולכתוב :
א.	להציג את שם האתר
ב.	להציג את תוכן קוד האתר בPrint
ג.	לכתוב לתוך קובץ את תוכן האתר
ד.	להציג זמן כולל של הפעולות (import time)

1.	שלב ראשון בצע ללא Thread ReadSitesNoThread.py
2.	שלב שני בצע Thread      ReadSiteThread.py

"""

import requests
from bs4 import BeautifulSoup
import time

url_site =["https://www.ynet.co.il/home/0,7340,L-8,00.html",
         "https://corona.mako.co.il/",
         "https://13tv.co.il/",
         "https://edition.cnn.com/",
         "https://www.youtube.com/?gl=IL",
         "https://www.calcalist.co.il/home/0,7340,L-8,00.html",
         "https://www.one.co.il/",
         "https://www.google.co.il/?hl=iw",
         "https://www.maariv.co.il/news",
            "https://www.apple.com/"
           ]


def Deal_with_site(url):
    get_html_page = requests.get(url).content # get html code of site
    soup = BeautifulSoup(get_html_page, "html.parser")
    title = soup.title # get title of site
    print("\033[1;35m"+title.get_text()+"\033[1;37m")
    print(soup.prettify())

    with open('Sitedata.txt', "wb") as writer: # create file with content of site
        writer.write(soup.prettify().encode("utf-8"))
    writer.close()


start_time = time.perf_counter()

for site in url_site:
    Deal_with_site(site)

end_time = time.perf_counter()
print("Toatl Time is :", end_time-start_time, "sec")
