#Python 3.6 -- Constantinos Bolosis -- P17085 -- 100x100 Square :D

import random
import sys
if len(sys.argv) != 2:
    print("This script requires only one given argument")
else:
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print("Can't open", sys.argv[1], "or no such file exists")
    else:
        words = [x.strip() for x in f.readlines()]
        strings = [""] * 200
        for i in range (100):
            for j in range (100):
                char = chr(random.randrange(65,90))
                strings[i] += char
                strings[100 + j] += char
            print(strings[i])
        counter = 0
        for i in range (len(words)):
            if words[i] != "" and any(str.upper(words[i]) in square for square in strings):
                counter += 1
                if counter == 1:
                    print("\nWords found:")
                print(words[i])
        if counter == 0:
            print("\nNo words found")
        f.close()