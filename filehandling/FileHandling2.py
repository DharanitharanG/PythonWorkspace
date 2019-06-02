import os

# os.mkdir("C:\\Users\\Dharani\\Desktop\\f1")

if (os.path.exists("/home/dharani/test")):
    print("exists")
else:
    print("not exists")
    os.mkdir("/home/dharani/test")
