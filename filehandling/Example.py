
sample_file =''
try:
    sample_file = open("/home/dharani/SampleFile2",'x')
except FileExistsError:
    print("The file is already available, so overwriting")
    sample_file = open("/home/dharani/SampleFile2", 'a')

# print(sample_file.read())
'''
for x in sample_file:
  print(x)
'''
# print(sample_file.read(5))

sample_file.write("\n")
sample_file.write("this is new line -1 ")
sample_file.close()





