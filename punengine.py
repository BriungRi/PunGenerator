import enchant
import requests
from nltk.stem import PorterStemmer

def isWord(word): #Checks if it is a word
    urlname = "http://dictionary.reference.com/browse/" + word
    page = requests.get(urlname).text
    count = page.lower().count("misspell")
    return(count < 40)

def getSyllables(word): #Returns an array of the syllables
    listSyllables = []
    urlname = "http://dictionary.reference.com/browse/" + word
    page = requests.get(urlname).text
    first = page.find("data-syllable=") + 15
    last = page.find("\"", first)
    syllabalizedWord = page[first:last] + "·"
    while(syllabalizedWord.find("·") > 0):
        firstInstanceOf = syllabalizedWord.find("·")
        listSyllables.append(syllabalizedWord[0:firstInstanceOf])
        syllabalizedWord = syllabalizedWord[firstInstanceOf + 1:len(syllabalizedWord)]
    return(listSyllables)


def getExampleSentences(word): #Returns an array of example sentences
    listSentences = []
    urlname = "http://dictionary.reference.com/browse/" + word
    page = requests.get(urlname).text
    first = page.find("partner-example-text")
    last = page.find("</p>", first)
    while(first > 0):
        listSentences.append(page[first + 23:last])
        first = page.find("partner-example-text", last)
        last = page.find("</p>", first)
    return listSentences

class PunEngine(object):

    def __init__(self, w):
        self.word = w
        self.generateSentences()
        self.finalize()

    def __str__(self):
        return str(self.makeJSON())

    def generateSimilars(self):
        similars = set()
        ps = PorterStemmer()
        for w in getSyllables(self.word):
            similars.add(w.lower())
            enchanter = enchant.Dict("en_US")
            for w in enchanter.suggest(w):
                if(len(w) > 2): #Deletes strings that are too short
                    similars.add(w.lower())
        return similars

    def generateSentences(self):
        self.originalSentences = []
        listSimilars = self.generateSimilars()
        for sim in listSimilars:
            listTemp = getExampleSentences(sim)
            for sent in listTemp:
                self.originalSentences.append(sent)

    def finalize(self):
        self.newSentences = []
        for i in self.originalSentences:
            beg = i.find("<em>")
            end = i.find("</em>")
            self.newSentences.append(i[0:beg] + self.word.upper() + i[end + 5:])

    def makeJSON(self):
        self.jsonoutput = []
        i = 0
        while(i < len(self.originalSentences)):
            data = {'id' : i,
                  'original' : self.originalSentences[i],
                  'new' : self.newSentences[i],}
            self.jsonoutput.append(data)
            i += 1

        return self.jsonoutput

    def makeArray(self):
        arrayoutput = []
        i = 0
        while(i < len(self.originalSentences)):
            data = self.originalSentences[i] + "\n" + self.newSentences[i] + "\n"
            arrayoutput.append(data)
            i += 1
        return arrayoutput
