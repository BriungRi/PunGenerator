from flask import Flask, request
import punengine
import random
import csvrecord

app = Flask(__name__)
@app.route('/punengine/api/v1.0/')
def default_sentence():
    pe = punengine.PunEngine("Pun")
    sentences = pe.makeArray()
    return str(sentences[random.randint(0, len(sentences))])

@app.route('/punengine/api/v1.0/<string:word>')
def generate_sentence(word):
    pe = punengine.PunEngine(word)
    sentences = pe.makeArray()
    return str(sentences[random.randint(0, len(sentences))])

#test with: curl -i -H "Content-Type: application/json" -X POST -d '{"orig":"hi", "new":"hello", "sentence":"this is a sentence"}' http://0.0.0.0:5000/punengine/api/v1.0/data
@app.route('/punengine/api/v1.0/data', methods=['POST'])
def add_data():
    if not request.json:
        abort(400)
    data = {
        'orig' : request.json['orig'],
        'new' : request.json['new'],
        'sentence' : request.json['sentence']
    }
    # csvrecord.test()
    csvrecord.record(data)
    return str(data)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
