
import json
path = '/home/dharani/PycharmProjects/PythonSession/InputFiles/Person2.json'
data = open(path,'r')
with data as l:
    persons = json.load(l)
print(persons)
print(persons['firstName'])
print(persons['address']['street'])





