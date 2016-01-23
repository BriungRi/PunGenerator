import requests
# from bs4 import BeautifulSoup

url = "http://goo.gl/c29Mjs"
page = requests.get(url).text

def pageParser(page):
    str = ""
    indexBeg = 0
    indexEnd = 0
    x = page.find("<p class=\"story-body")
    while(x > 0):
        print(x)
        indexBeg = page.find(">", x) + 1
        indexEnd = page.find("</p>", indexBeg)
        str += page[indexBeg:indexEnd] + "\n"
        x = page.find("<p class=\"story-body", indexEnd)
        print(x)
    return str

print(pageParser(page))
