print("Welcome to the program")

a = 6; b = 0;

try:
 names = ['Sushma','Mythri','Supriya']
 # print(" the name in 4th place is :",names[3])
 c = a/b;
 print("This statement is written before the print -c  ")
 print("The value of c is: ",c)
except (IndexError):
 print("index issue")
 c = 5/0;
except ZeroDivisionError as a:
 print("dont divide a num by 0 : ",repr(a))
except:
 print("something happended")
finally:
 print("End of the program... Thanks for using the script")
