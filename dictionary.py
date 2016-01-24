import requests


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
