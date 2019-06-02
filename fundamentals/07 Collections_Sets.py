
#  unordered and unindexed

thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
  print(x)
 
#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset.add("orange") #Add an item to a set

thisset.update(["orange", "mango", "grapes"]) # Add multiple items to a set

print(len(thisset))

thisset.remove("banana")

# Note: If the item to remove does not exist, remove() will raise an error.

thisset.discard("banana")

#Note: If the item to remove does not exist, discard() will NOT raise an error.

x = thisset.pop()
print(x)
print(thisset)

'''use the pop(), method to remove an item,
 but this method will remove the last item.
 Remember that sets are unordered, 
 so you will not know what item that gets removed.
'''
thisset.clear()
del thisset

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

'''
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes the specified element
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
'''

