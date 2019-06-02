'''
Python Loops
Python has two primitive loop commands:

while loops
for loops
'''

i = 1
while i < 6:
  print(i)
  i += 1
  
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#  looping through strings
for x in range(2, 6):
  print(x)for x in "banana":
  print(x)
  
# range() function
for x in range(6):
  print(x)
    
for x in range(2, 6):
  print(x)
  
# range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)
  
#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)
  
# nested loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
	
