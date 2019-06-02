# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(thistuple[1])

thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)
#Once a tuple is created, you cannot change its values. Tuples are unchangeable.


## cant add, remove items

# The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''