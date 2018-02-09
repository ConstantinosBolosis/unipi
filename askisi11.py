import random
import sys
if len(sys.argv) != 2:
    print("Not enough arguments given")
else:
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print("Can't open file", sys.argv[1])
    else:
        square = [[None] * 100] * 100
        for i in range (100):
            for j in range (100):
                square[i][j] = chr(random.randrange(65,90))
                print(square[i][j], end="")
            print("\n", end="")
        f.close()