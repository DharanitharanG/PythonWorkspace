import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [2,3,4,5,6,7]
y1 = [3,4,5,6,7,9]

# plt.plot(x,y)
# plt.show()

'''
plt.scatter(x,y,edgecolors="b", marker="*",label="Y")
plt.legend()
plt.scatter(x,y1,edgecolors="g",marker = "^", label = "Y1")
plt.legend()
plt.xlabel("X variable")
plt.ylabel("Y Variable")
plt.title(" X vs Y")
plt.xlim(0,10)
plt.ylim(0,15)
plt.show()
'''


'''import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [2,3,4,5,6,7]
y1 = [3,4,5,6,7,9]

plt.plot(x,y, color="b", linewidth=1)
plt.legend()
plt.plot(x,y1,color="g",linewidth=1)
plt.legend()
plt.xlabel("X variable")
plt.ylabel("Y Variable")
plt.title(" X vs Y")
plt.xlim(0,10)
plt.ylim(0,15)
plt.show()
'''


fig = plt.figure()
s1 = fig.add_subplot(221)
s1.scatter(x,y)


#
s2 = fig.add_subplot(222)
s2.scatter(x,y1)
plt.show()
# s2.set_xlim(0,8)
#
# plt.show()
#
# plt.bar(x,y)
# plt.show()
# plt.barh(x,y)
# plt.show()
# plt.pie(x,y)
# plt.show()




#-----------------------------------------

# plt.plot(x,y, label='linear')
# plt.legend()
# plt.show()

#---------------------------------------

# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(221) # nrows, ncolumns, position --> 2 rows, 2 cols, 1st position
# ax2 = fig.add_subplot(224)
#
# ax.plot(x,y, color='lightblue', linewidth=3)
# ax2.scatter(x,y, color='darkgreen', marker='*')
# ax.set_xlim(0,7)
# ax2.set_xlim(0,7)
# plt.show()

#-------------------------------------------

# import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(10,30))
# ax = fig.add_subplot(221)
# ax2 = fig.add_subplot(224)
#
# ax.plot(x,y, color='lightblue', linewidth=1)
# ax2.scatter(x,y, color='darkgreen', marker='*')
# ax.set_xlim(0,7)
# ax2.set_xlim(0,7)
# plt.show()

#-------------------------------------------




















