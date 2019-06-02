print("Welcome to the program")

a = 6; b = 0;

try:
 names = ['Sushma','Mythri','Supriya']
 print(" the name in 4th place is :",names[3])
 c = a/b;
 print("This statement is written before the print -c  ")
 print("The value of c is: ",c)
except (IndexError,ZeroDivisionError):
 print("index or zero div")
# except ZeroDivisionError:
#  print("index or zero div")
except:
 print("something happended")

print("This statement is written after the print -c  ")
print("End of the program... Thanks for using the script")