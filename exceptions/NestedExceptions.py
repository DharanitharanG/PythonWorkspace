try:
    print("inside outer try")
    a = 5/0
    print("end of try")
except ZeroDivisionError:
    print("inside zero division error - outer")
    try:
        x = ['a','b','c']
        print("printing 4th element", x[3])
    except Exception:
        print("some issue ")
except IndexError:
    print(" inside index error - outer")
finally:
    print("in finally - outer")
