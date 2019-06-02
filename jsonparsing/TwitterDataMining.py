import json;
import pandas as pd
import matplotlib.pyplot as plt
import jsonparsing.ResuableRegex as rs

path = '/home/dharani/PycharmProjects/PythonSession/InputFiles/twittertweets_new.txt'
data = open(path,'r')
jsonList = []

for x in data:
    try:
      line = json.loads(x); jsonList.append(line);
    except:
      continue

screenName = list(map(lambda x : x['user']['screen_name'],jsonList))
text = list(map(lambda x : x['text'],jsonList))
lang = list(map(lambda x : x['lang'],jsonList))
country = list(map(lambda x : x['user']['location'],jsonList))
tweets = pd.DataFrame()
tweets['ScreenName'] = screenName;
tweets['Text']=text ; tweets['lang']=lang; tweets['country']=country ;

tweets['JavaScript'] = list(map(lambda x:
                                 rs.wordPresentOrNot("JavaScript",x),
                                 tweets['Text']))
tweets['Python'] = list(map(lambda x:
                                 rs.wordPresentOrNot("Python",x),
                                 tweets['Text']))

course_counts = [tweets['JavaScript'].value_counts()['True'],
             tweets['Python'].value_counts()['True']]
x_pos = list(range(len(course_counts)))
fig, ax = plt.subplots()
plt.bar(x_pos, course_counts, 0.5,color='g')
ax.set_ylabel('Number of Occurane', fontsize=15)
ax.set_title('JavaScript vs Python Occurance', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * 0.8 for p in x_pos])
ax.set_xticklabels(['JavaScript','Python'])
plt.grid()
# plt.show()
plt.savefig("/home/dharani/Desktop/courseCounts.png")


