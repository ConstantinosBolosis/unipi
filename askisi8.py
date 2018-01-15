#Python 3.6 -- Constantinos Bolosis -- P17085 -- Combinations :/

import random
while True:
    numlist = random.sample(range(-30, 30), 30)
    print(numlist, "\n", sep="")
    combo = [None] * 3
    i = 0
    for x in range (28):
        combo[0] = numlist[x]
        for y in range (28 - x):
            combo[1] = numlist[1 + x + y]
            for z in range (28 - x - y):
                combo[2] = numlist[2 + x + y + z]
                if (combo[0] + combo[1] + combo[2] == 0):
                   i += 1
                   print(combo)
    if i == 0:
        print("There are no combinations of 3 elements from the main list that add up to 0")
    meh = input("\nRun again? (y/n): ")
    if meh == "n" or meh == "N":
        break