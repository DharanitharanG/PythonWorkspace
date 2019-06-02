import random

# random.seed(30)
# print("first - ", random.randint(25, 50))
#
# random.seed(30)
# print("Second - ", random.randint(25, 50))
#
# random.seed(30)
# print("Third - ", random.randint(25, 50))

#-------------------------
# random.seed(30)
# print("first - ", random.randint(25, 50))

# print("Second - ", random.randint(25, 50))
#
# random.seed(30)
# print("Third - ", random.randint(25, 50))
#---------------------------

list = [100, 200, 300, 400, 500, 600]
random.seed(6)
random_item = random.choice(list)

print("First random item from list ", random_item)
random.seed(6)
random_item = random.choice(list)
print("Second random item from list ", random_item)

random.seed(6)
random_item = random.choice(list)
print("Third random item from list ", random_item)



