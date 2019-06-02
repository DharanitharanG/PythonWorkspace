'''

open(filename,modeOfHandling) - key function to handle the file

  arguments to open() - >
  filename : filepath with extension
  mode: r, a, w , x (create)

  optional params : t --> should handle the file in text way
                    b --> in binary way

this is sample in python
next line
next line 2
next line 3
last line
'''

#samplefile = open("C:\\Users\\Dharani\\Desktop\\samplefile1.txt")

#print(samplefile.read())
# print(samplefile.readline())
# print(samplefile.read(4))

'''
for a in samplefile:
    print(a)
'''

samplefile = open("/home/dharani/Desktop/f1","r")

# samplefile.write("anotherline-----ppp")
# samplefile.close()

print(samplefile.readlines())
