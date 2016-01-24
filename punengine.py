# import nltk
import enchant
# import wordprocessing
# import requests
# import random
# import time
from nltk.stem import PorterStemmer
import dictionary
class PunEngine(object):

    def __init__(self, w):
        self.word = w
        self.generateSentences()
        self.finalize()

    def __str__(self):
        output = ""
        i = 0
        while(i < len(self.originalSentences)):
            output += "Number " + str(i + 1) + "\n"
            output += "Original: " + self.originalSentences[i] + "\n\n"
            output += "Punnified: " + self.newSentences[i] + "\n\n"
            i += 1
        return output

    def generateSimilars(self):
        similars = set()
        ps = PorterStemmer()
        for w in dictionary.getSyllables(self.word):
            enchanter = enchant.Dict("en_US")
            for w in enchanter.suggest(w):
                if(len(w) > 2): #Deletes strings that are too short
                    similars.add(w.lower())
        return similars

    def generateSentences(self):
        self.originalSentences = []
        listSimilars = self.generateSimilars()
        for sim in listSimilars:
            listTemp = dictionary.getExampleSentences(sim)
            for sent in listTemp:
                self.originalSentences.append(sent)

    def finalize(self):
        self.newSentences = []
        for i in self.originalSentences:
            beg = i.find("<em>")
            end = i.find("</em>")
            self.newSentences.append(i[0:beg] + self.word.upper() + i[end + 5:])


testWord = "pun"
pe = PunEngine(testWord)
print(str(pe))




































#
# def clean(list, word):
#     cleaned = []
#     for i in list:
#         if len(i) > 1 and i in word.lower():
#             cleaned.append(i)
#     return(cleaned)
#
# def generateSent(list, word):
#     origsentence = ""
#     newList = []
#     for i in list:
#         newList.append(i)
#     # # newsentence = ""
#     newWord = ""
#     while(origsentence == ""):
#         i = random.randint(0, len(newList) - 1)
#         newWord = newList[i]
#         origsentence += wordprocessing.getSentence(newWord) #TODO fix this line
#         time.sleep(5) #delayed for time to process
#         print(newWord)
#     # # indexOf = origsentence.find(newWord) - 1
#     # # newsentence = origsentence[0:indexOf] + word + origsentence[indexOf + len(newWord):]
#     # # return(origsentence + "\n" + newsentence)
#     return origsentence
#
# def generate(word):
#     # print(clean(similars(truncate(word)), word))
#     return(generateSent(clean(similars(truncate(word)), word), word))
