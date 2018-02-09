import random
square = [[None] * 100] * 100
for i in range (100):
    for j in range (100):
        square[i][j] = chr(random.randrange(65,90))
        print(square[i][j], end="")
    print("\n", end="")
