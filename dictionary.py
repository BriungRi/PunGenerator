import requests
import enchant
from nltk.stem import PorterStemmer

def is_word(word): #Checks if it is a word
    urlname = "http://dictionary.reference.com/browse/" + word
    page = requests.get(urlname).text
    count = page.lower().count("misspell")
    return(count < 40)

def get_syllables(word): #Returns an array of the syllables
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

def get_example_sentences(word): #Returns an array of example sentences
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

def get_similars(word): #uses spellchecker and truncation to get similar words
    list_similars = set()
    ps = PorterStemmer()
    for w in get_syllables(word):
        list_similars.add(w.lower())
        enchanter = enchant.Dict("en_US")
        for w in enchanter.suggest(w):
            if(len(w) > 2): #Deletes strings that are too short
                list_similars.add(w.lower())
    return list_similars

#TODO clean special symbols
def get_synonyms(word): #finds synonyms of any word
    list_synonyms = set()
    urlname = "http://www.thesaurus.com/browse/" + word
    page = requests.get(urlname).text
    first = page.find("<a href=\"http://www.thesaurus.com/browse/")
    last = page.find("\"", first + 20)
    while(first > 0):
        list_synonyms.add(page[first + 41:last])
        first = page.find("<a href=\"http://www.thesaurus.com/browse/", last)
        last = page.find("\"", first + 20)
    return list_synonyms
