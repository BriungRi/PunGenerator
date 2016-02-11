from flask import Flask, request
import punengine
import csvrecord

app = Flask(__name__)
@app.route('/punengine/api/v1.0/')
def default_sim_sentence():
    pe = punengine.PunEngine("Pun", 0)
    return str(pe)

@app.route('/punengine/api/v1.1/')
def default_syn_sentence():
    pe = punengine.PunEngine("Pun", 1)
    return str(pe)

@app.route('/punengine/api/v1.0/<string:word>')
def get_similar_sentence(word):
    pe = punengine.PunEngine(word, 0) #mode = 0
    return str(pe)

@app.route('/punengine/api/v1.1/<string:word>')
def get_synonym_sentence(word):
    pe = punengine.PunEngine(word, 1) #mode = 1
    return str(pe)

#test with: curl -i -H "Content-Type: application/json" -X POST -d '{"orig":"hi", "new":"hello", "sentence":"this is a sentence", "binary":"0"}' http://0.0.0.0:5000/punengine/api/v1.0/data
@app.route('/punengine/api/v1.0/data', methods=['POST'])
def add_data():
    if not request.json:
        abort(400)
    data = {
        'orig' : request.json['orig'],
        'new' : request.json['new'],
        'sentence' : request.json['sentence'],
        'binary' : request.json['binary']
    }
    csvrecord.record(data)
    return str(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
