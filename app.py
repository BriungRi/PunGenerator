from flask import Flask, request
import punengine
import random

app = Flask(__name__)
@app.route('/')
def default_sentence():
    pe = punengine.PunEngine("Pun")
    sentences = pe.makeArray()
    return str(sentences[random.randint(0, len(sentences))])
@app.route('/<string:word>')
def generate_sentence(word):
    pe = punengine.PunEngine(word)
    sentences = pe.makeArray()
    return str(sentences[random.randint(0, len(sentences))])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
