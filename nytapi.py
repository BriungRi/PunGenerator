import requests
import json
def search(name):
    data = {'q' : name,
          'begin_date' : '20150101',
          'end_date' : '20160101',
          'api-key' : '74eba9e75a744dc34a90c6dbae0b37af:2:74093787'}

    resp = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json?', params = data)
    jsondict = str(resp.json())
    return(jsondict)


def jsonparser(jsondata, toFind):           #jsondata - string of json to parse  #toFind - parameter to find
    urls = []
    while(jsondata.find(toFind) > 0):
        spacing = len(toFind) + 4
        x = jsondata.find(toFind)
        jsondata = jsondata[x + spacing:len(jsondata)]
        indexEnd = jsondata.find("\'")
        strurl = jsondata[0:indexEnd]
        urls.append(strurl)
    return urls

def getURLS(topic):
    return(jsonparser(search(topic), "web_url"))
