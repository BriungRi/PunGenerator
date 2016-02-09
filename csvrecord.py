import csv

def record(jsondata):
    data = jsondata.get('orig') + "," + jsondata.get('new') + "," + jsondata.get('sentence') + "\n"
    fd = open('data.csv','a')
    fd.write(data)
    fd.close()
# def test():
#     fd = open('data.csv','a')
#     fd.write("ok")
#     fd.close()

# record({'orig' : 'hi', 'new' : 'hello', 'sentence' : 'this is a sentence'})
