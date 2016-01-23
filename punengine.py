import nltk
import enchant
import wordprocessing
import requests
import random
import time
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
        # ps = PorterStemmer()
        for w in d.suggest(word):
            similars.add(w.lower())
    return(similars)

def clean(list, word):
    cleaned = []
    for i in list:
        if len(i) > 1 and i in word.lower():
            cleaned.append(i)
    return(cleaned)

def generateSent(list, word):
    origsentence = ""
    newList = []
    for i in list:
        newList.append(i)
    # # newsentence = ""
    newWord = ""
    while(origsentence == ""):
        i = random.randint(0, len(newList) - 1)
        newWord = newList[i]
        origsentence += wordprocessing.getSentence(newWord) #TODO fix this line
        time.sleep(5) #delayed for time to process
        print(newWord)
    # # indexOf = origsentence.find(newWord) - 1
    # # newsentence = origsentence[0:indexOf] + word + origsentence[indexOf + len(newWord):]
    # # return(origsentence + "\n" + newsentence)
    return origsentence

def generate(word):
    # print(clean(similars(truncate(word)), word))
    return(generateSent(clean(similars(truncate(word)), word), word))
