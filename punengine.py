import nltk
import enchant
import wordprocessing
import requests
from nltk.stem import PorterStemmer

def truncate(word):
    urlname = "http://dictionary.reference.com/browse/" + word
    page = requests.get(urlname).text
    first = page.find("data-syllable=") + 15
    last = page.find("\"", first)
    syllabalizedWord = page[first:last] + "·"
    listSyllables = []
    while(syllabalizedWord.find("·") > 0):
        firstInstanceOf = syllabalizedWord.find("·")
        listSyllables.append(syllabalizedWord[0:firstInstanceOf])
        syllabalizedWord = syllabalizedWord[firstInstanceOf + 1:len(syllabalizedWord)]
    return(listSyllables)

def similars(listSyllables):
    similars = set()
    for word in listSyllables:
        d = enchant.Dict("en_US")
        ps = PorterStemmer()
        for w in d.suggest(ps.stem(word)):
            similars.add(w.lower())
    return(similars)

def clean(list):
    cleaned = []
    for i in list:
        if len(i) > 3:
            cleaned.append(i)
    return(cleaned)

def generateSentence(list):
    sentence = ""
    i = 0
    while(sentence == ""):
        print(list[i])
        sentence += wordprocessing.getSentence(list[i])
        i += 1
    return sentence

# print(clean(similars(truncate("Almighty"))))
print(generateSentence(clean(similars(truncate("Almighty")))))
