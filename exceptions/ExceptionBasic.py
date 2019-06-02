
a = 3
b = 6

try:
 c = a/b
 print (c)
 x = [1, 2, 3]
 print(x[6])
except IndexError:
 print("index out of bound")
except ZeroDivisionError:
 print("you are trying to divide a number by zero")
 raise ValueError
