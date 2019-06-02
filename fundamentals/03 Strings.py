
''' strings in Python are arrays of bytes
 representing unicode characters.
 However, Python does not have a character data type, 
 a single character is simply a string
 with a length of 1.
 Square brackets can be used to access elements
 of the string.
 '''
 
 
a = "Hello, World!"
print(a[1])

'''Substring. Get the characters
 from position 2 to position 5 (not included):
 note: index starts with 0
 '''
 
b = "Hello, World!"
print(b[2:5])

# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']

# Command-line String Input
print("Enter your name:")
x = input()
print("Hello, " + x)


