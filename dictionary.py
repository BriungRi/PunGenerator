import requests

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

def get_synonyms(word):
    list_synonyms = []
    urlname = "http://www.thesaurus.com/browse/" + word
    page = requests.get(urlname).text
    first = page.find("<a href=\"http://www.thesaurus.com/browse/")
    last = page.find("\"", first + 20)
    while(first > 0):
        list_synonyms.append(page[first + 41:last])
        first = page.find("<a href=\"http://www.thesaurus.com/browse/", last)
        last = page.find("\"", first + 20)
    # for s in list_synonyms:
    #     while(s.find("%") > 0):
    #         print(s)
    #         s = s[0:s.find("%")] + " " + s[s.find("%") + 1:]
    return list_synonyms

print(get_synonyms("good"))
