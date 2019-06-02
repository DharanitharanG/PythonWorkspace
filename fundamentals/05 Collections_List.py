'''
There are four collection data types in the Python programming language:

List is a collection which is ordered(insertion order) and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
thislist[1] = "blackcurrant"
print(thislist)

for x in thislist:  # Loop Through a List
  print(x)
  
if "apple" in thislist:  # Check if Item Exists
  print("Yes, 'apple' is in the fruits list")

print(len(thislist))

#To add an item to the end of the list, use the append()
thislist.append("orange") # Add Items
print(thislist)

#To add an item at the specified index, use the insert()
thislist.insert(1, "orange")
print(thislist)

##remove Items
#The remove() method removes the specified item:
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)

#The del keyword removes the specified index:
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely:
del thislist

#The clear() method empties the list:
thislist.clear()


'''
The list() Constructor
It is also possible to use the list() constructor to make a list.
'''
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

