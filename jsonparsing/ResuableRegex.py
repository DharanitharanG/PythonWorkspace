import re

def wordPresentOrNot(word,text):
    match = re.search(word.upper(),text.upper())
    if match:
        return 'True'
    else:
        return 'False'
