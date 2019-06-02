# unordered, changeable and indexed

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

x = thisdict["model"]
x = thisdict.get("model") 
# above both will give same result

#Change the "year" to 2018:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# To Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
 
# Print all values in the dictionary, one by one: 
for x in thisdict:
  print(thisdict[x])

# values() function to return values of a dictionary:
for x in thisdict.values():
  print(x)
  
# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)
  
print(len(thisdict))

thisdict["color"] = "red"
print(thisdict)

#The del keyword removes the item with the specified key name:
del thisdict["model"]
print(thisdict)
#The del keyword can also delete the dictionary completely:
del thisdict


#The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)


thisdict.clear()

#The dict() Constructor
thisdict =	dict(brand="Ford", model="Mustang", year=1964)

'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing the a tuple for each key value pair
keys()	Returns a list contianing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''


