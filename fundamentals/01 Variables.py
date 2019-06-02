# Creating Variables
'''Variables do not need to be declared with any particular type '''
 
x = 4 # x is of type int
x = "Dharani" # x is now of type str
print(x)


x = "Dharani"
print("Trainer is " + x)

# You can also use the + character to add a variable to another variable:

x = "Python is "
y = "awesome"
z =  x + y
print(z)

x = 5
y = 10
print(x + y)

#If you try to combine a string and a number, Python will give you an error:

x = 5
y = "John"
print(x + y)