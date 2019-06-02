import json;
import pandas as pd
import matplotlib.pyplot as plt
import jsonparsing.ResuableRegex as rs

path = '/home/dharani/PycharmProjects/PythonSession/InputFiles/Person2.json'
data = open(path,'r')
jsonList = []

for x in data:
    line = json.loads(x)
    jsonList.append(line)

fname = list(map(lambda x : x['firstName'],jsonList))
lname = list(map(lambda x : x['lastName'],jsonList))
age = list(map(lambda x : x['age'],jsonList))
feedback = list(map(lambda x : x['feedback'],jsonList))
country = list(map(lambda x : x['address']['country'] if(len(x['address']['country']) > 0) else 'India',jsonList))
students = pd.DataFrame()
students['FirstName'] = fname; students['LastName'] = lname
students['age']=age ; students['feedback']=feedback
students['country']=country ; print(students)

students['fd_good'] = list(map(lambda x: rs.wordPresentOrNot("good",x),
                                 students['feedback']))
students['fd_bad'] = list(map(lambda x: rs.wordPresentOrNot("bad",x),
                                 students['feedback']))
# print(students)
# print ("No of good comments : ",students['fd_good'].value_counts()['True'])
# print ("No of bad comments : ",students['fd_bad'].value_counts()['True'])

feedBacks = [students['fd_good'].value_counts()['True'],
             students['fd_bad'].value_counts()['True']]
x_pos = list(range(2))
fig, ax = plt.subplots()
plt.bar(x_pos, feedBacks, 0.2,color='g')
# Setting axis labels and ticks
ax.set_ylabel('Number of feedbacks', fontsize=15)
ax.set_title('Good vs bad feedback', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * 0.8 for p in x_pos])
ax.set_xticklabels(['Good','Bad'])
plt.grid()
plt.show()


