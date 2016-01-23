import nytparser
import nytapi
import time

articlestring = []
topics = ["Obama", "Industry", "Technology", "Eco"]
# links = []
# for i in topics:
#     items = nytapi.getURLS(i)
#     for j in items:
#         links.append(items)
#     # time.sleep(1) //creates a delay in case API calls too quickly
# for i in links:
#     articlestring += nytparser.pageParser(str(i))
# print(articlestring)
for i in topics:
    urls = nytapi.getURLS(i)
    for i in urls:
        articlestring.append(nytparser.pageParser(i))
saveFile = open('articles.txt','w')
for i in articlestring:
    saveFile.write(i + "\n\n\n\n\n\n")
