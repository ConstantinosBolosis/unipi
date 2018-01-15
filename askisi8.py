import random
numlist = list()
for i in range (30):
    numlist.append(random.randrange(-30, 30))
print(numlist)
#triad = list()
i = 0
for x in range (28):
    for y in range (28 - x):
        for z in range (28 - x - y):
            i += 1
print(i)
            