import requests
import random
import dictionary

#TODO is it possible if a word is small, to find it within a bigger word?
#TODO subject that a word covers and the words within it
class PunEngine(object):

    def __init__(self, w, mode):
        self.word = w
        self.run(mode)

    def __str__(self):
        return self.get_sentence()

    def run(self, mode): #mode = 0 similars mode = 1 synonyms
        self.original_sentences = []
        if mode == 0:
            list_words = dictionary.get_similars(self.word)
        elif mode == 1:
            list_words = dictionary.get_synonyms(self.word)
        new_word = self.get_random_word(list_words)
        list_temp = dictionary.get_example_sentences(new_word)
        for s in list_temp:
            self.original_sentences.append(s)
        self.finalize()

    def get_random_word(self, list):
        new_list = []
        for i in list:
            new_list.append(i)
        return new_list[random.randint(0, len(new_list) - 1)]

    def finalize(self):
        self.new_sentences = []
        for i in self.original_sentences:
            beg = i.find("<em>")
            end = i.find("</em>")
            self.new_sentences.append(i[0:beg] + self.word.upper() + i[end + 5:])

    def get_JSON(self):
        self.jsonoutput = []
        i = 0
        while(i < len(self.original_sentences)):
            data = {'id' : i,
                  'original' : self.original_sentences[i],
                  'new' : self.new_sentences[i],}
            self.jsonoutput.append(data)
            i += 1

        return self.jsonoutput

    def get_array(self):
        arrayoutput = []
        i = 0
        while(i < len(self.original_sentences)):
            data = "ORIGINAL: " + self.original_sentences[i] + "\n" + "PUNNIFIED: " + self.new_sentences[i] + "\n"
            arrayoutput.append(data)
            i += 1
        return arrayoutput

    def get_sentence(self):
        sentences = self.get_array()
        return str(sentences[random.randint(0, len(sentences) - 1)])
