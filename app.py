from flask import Flask, request
import punengine
import random

app = Flask(__name__)

@app.route('/<string:word>')
def send_text_file(word):
    pe = punengine.PunEngine(word)
    sentences = pe.makeArray()
    return str(sentences[random.randint(0, len(sentences))])


if __name__ == '__main__':
    app.run(debug=True)
