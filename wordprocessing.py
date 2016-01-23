import nltk
import nytparser
import nytapi
import random
from nltk.tokenize import sent_tokenize, word_tokenize

def cleanArticle():
    text = open("articles.txt", "r").read()
    while(text.find("<a ") > 0):
        indexBeg = text.find("<a ")
        indexEnd = text.find("</a>", indexBeg) + 4
        text = text[0:indexBeg] + text[indexEnd:len(text)]
    articles = open('articles.txt','w')
    articles.write(text)

def generateArticle(word):
    articlestring = []
    urls = nytapi.getURLS(word)
    for i in urls:
        articlestring.append(nytparser.pageParser(i))
    articles = open('articles.txt','w')
    for i in articlestring:
        articles.write(i)
    cleanArticle()

def findWord(toFind):
    articles = open("articles.txt", "r").read()
    sentences = sent_tokenize(articles)
    list = []
    for s in sentences:
        if toFind in s:
            list.append(s)
    return(list)

def getSentence(word):
    generateArticle(word)
    listSentences = findWord(word)
    return(listSentences[random.randint(0, len(listSentences))])
