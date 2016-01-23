import requests
import json
import time
# import random
import values

def search(name):
    todaysDate = time.strftime("%Y%m%d")
    data = {'q' : name,
          'begin_date' : '20000101',
          'end_date' : todaysDate,
          'api-key' : values.nytapikey}

    resp = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json?', params = data)
    jsondict = str(resp.json())
    return(jsondict)


def jsonparser(jsondata, toFind):           #jsondata - string of json to parse  #toFind - parameter to find
    urls = []
    while(jsondata.find(toFind) > 0):
        spacing = len(toFind) + 4
        x = jsondata.find(toFind)
        jsondata = jsondata[x + spacing:len(jsondata)]  #length fix?
        indexEnd = jsondata.find("\'")
        strurl = jsondata[0:indexEnd]
        urls.append(strurl)
    return urls

def getURLS(topic):
    return(jsonparser(search(topic), "web_url"))
