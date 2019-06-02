'''
def addition():
    a=5
    b=10
    c=a+b
    print(c)

addition()
'''

'''
def addition(a,b):
    c=a+b
    print(c)

addition(4,5)
'''
z = 10
def addition(a,b,c):
    d=a+b+c
    return d

'''def addition(a,b):
    d=a+b
    return d
'''

d=addition(2,3,4)
print(d)
'''
def addition(a=5,b=4):
  a+b 

c=addition()

print(c)
'''

def mul(c,*a) :
    print(len(a))
    sum=1*c
    for x in a :
        sum=sum*x

    return sum

d=mul(5,5,5)
print(d)








