import enchant
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


testWord = "Baseball"
pe = PunEngine(testWord)
print(str(pe))
