#Python 3.6 -- Constantinos Bolosis -- P17085 -- ROT13 ;)

while True:
    user_input = list(input("Input: "))
    for i in range (len(user_input)):
        num = ord(user_input[i])
        if num > 126 or num < 32 :
            ok = 0
            break
        else:
            ok = 1
            if (num >= 65 and num <= 90):
                num += 13
                if num > 90:
                    num -= 26
            if (num >= 97 and num <= 122):
                num += 13
                if num > 122:
                    num -= 26
        user_input[i] = chr(num)
    if ok == 1:
        print("ROT13: " + "".join(user_input) + "\n")
    else:
        print("Can't process what you typed\n")
