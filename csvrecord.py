import csv

def record(jsondata):
    data = jsondata.get('orig') + "," + jsondata.get('new') + "," + jsondata.get('sentence') + "," + jsondata.get('binary') + "\n"
    fd = open('data.csv','a')
    fd.write(data)
    fd.close()

# record({'orig' : 'hi', 'new' : 'hello', 'sentence' : 'this is a sentence', 'binary' : '0'}) #test statement
