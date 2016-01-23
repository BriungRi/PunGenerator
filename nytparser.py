import requests
# from bs4 import BeautifulSoup
def pageParser(urlname):
    page = requests.get(urlname).text
    str = ""
    indexBeg = 0
    indexEnd = 0
    x = page.find("<p class=\"story-body")
    while(x > 0):
        indexBeg = page.find(">", x) + 1
        indexEnd = page.find("</p>", indexBeg)
        str += page[indexBeg:indexEnd] + "\n"
        x = page.find("<p class=\"story-body", indexEnd)
    return str
