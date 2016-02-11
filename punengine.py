import enchant
import requests
import random #for main method
import dictionary
from nltk.stem import PorterStemmer

#TODO use synonym algorithm

class PunEngine(object):

    def __init__(self, w):
        self.word = w
        self.generate_sentences()
        self.finalize()

    def __str__(self):
        return str(self.make_JSON())

    def generate_similars(self):
        similars = set()
        ps = PorterStemmer()
        for w in dictionary.get_syllables(self.word):
            similars.add(w.lower())
            enchanter = enchant.Dict("en_US")
            for w in enchanter.suggest(w):
                if(len(w) > 2): #Deletes strings that are too short
                    similars.add(w.lower())
        return similars

    def generate_sentences(self):
        self.originalSentences = []
        listSimilars = self.generate_similars()
        for sim in listSimilars:
            listTemp = dictionary.get_example_sentences(sim)
            for sent in listTemp:
                self.originalSentences.append(sent)

    def finalize(self):
        self.newSentences = []
        for i in self.originalSentences:
            beg = i.find("<em>")
            end = i.find("</em>")
            self.newSentences.append(i[0:beg] + self.word.upper() + i[end + 5:])

    def make_JSON(self):
        self.jsonoutput = []
        i = 0
        while(i < len(self.originalSentences)):
            data = {'id' : i,
                  'original' : self.originalSentences[i],
                  'new' : self.newSentences[i],}
            self.jsonoutput.append(data)
            i += 1

        return self.jsonoutput

    def make_array(self):
        arrayoutput = []
        i = 0
        while(i < len(self.originalSentences)):
            data = "ORIGINAL: " + self.originalSentences[i] + "\n" + "PUNNIFIED: " + self.newSentences[i] + "\n"
            arrayoutput.append(data)
            i += 1
        return arrayoutput

word = "cool"
pe = PunEngine(word)
sentences = pe.make_array()
print(str(sentences[random.randint(0, len(sentences))]))
