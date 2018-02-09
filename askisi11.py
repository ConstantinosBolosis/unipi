import random
import sys
if len(sys.argv) != 2:
    print("This script requires only one given argument")
else:
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print("Can't open file", sys.argv[1])
    else:
        words = [x.strip() for x in f.readlines()]
        print(words)
        square = [[None] * 100] * 100
        strings = [""] * 200
        for i in range (100):
            for j in range (100):
                square[i][j] = chr(random.randrange(65,90))
                strings[i] += square[i][j]
                strings[100 + j] += square[i][j]
                print(square[i][j], end="")
            print("\n", end="")
        print(strings)


        
        f.close()