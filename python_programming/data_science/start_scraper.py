__author__ = 'null'

from web_scrape import *
from load_urls import *
from createfile import *

def main():
    loadUrls = LoadUrls('input/urls')
    urllist  = loadUrls.get_urls()
    c = 0
    for url1 in urllist:
        print url1
        c = c + 1
        webScraper = WebScrape(url1)
        webScraper.fetch_html()
        webScraper.process_html()
        print webScraper.get_text()

        createFile = CreateFile(webScraper.get_text(),str(c)+'.txt')
        createFile.create_file()

if __name__=='__main__':
    main()

