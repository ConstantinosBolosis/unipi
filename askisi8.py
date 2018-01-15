import random
numlist = []
for i in range (30):
    numlist.append(random.randrange(-30, 30))
print(numlist)
combo = [None] * 3
for x in range (28):
    combo[0] = numlist[x]
    for y in range (28 - x):
        combo[1] = numlist[1 + x + y]
        for z in range (28 - x - y):
            combo[2] = numlist[2 + x + y + z]
            if (combo[0] + combo[1] + combo[2] == 0):
                print(combo)
print(i)
            