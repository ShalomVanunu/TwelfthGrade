﻿import requestsfrom bs4 import BeautifulSoupimport timedef main():    start_time = time.perf_counter()  # Start The Timer    urls_list = ["https://www.epicgames.com/store/en-US/", "https://store.steampowered.com/",             "https://13news.co.il/writer/tentv_writer_1569374523/",             "https://www.ynet.co.il/home/0,7340,L-8,00.html",             "https://www.rishonlezion.muni.il/Pages/default.aspx",             "https://www.bmw.co.il/he/index.html",             "https://www.apple.com/",             "https://stackoverflow.com/",             "https://www.maserati.com/il/he",             "https://www.ferrari.com/en-IL"]    get_html_page_list = []    for url in urls_list:        get_html_page_list.append(requests.get(url))    html_contents = []    for page in get_html_page_list:        html_contents.append(page.content)    print(html_contents)    soups_content = []    for content in html_contents:        c = BeautifulSoup(content, "html.parser")        soups_content.append(c)        print(c)    print ("It was the Content of the 10 sites, now the titles: ")    titles = []    file = open("file.txt", "wb")    for content in soups_content:        titles.append(content.title.get_text())        file.write(content.encode('utf-8'))    file.close()    for title in titles:        print(title)    end_time = time.perf_counter()  # Stop The Timer    print (f"It takes {end_time-start_time} seconds!")if __name__ == '__main__':    main()