import re

word = 'Python'
text = ' The training is all about Python'
match = re.search(word,text)

if match:
    print('true')
else:
    print('false')
