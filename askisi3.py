while True:
    user_input = list(input("Feel free to write something: "))
    for i in range (len(user_input)):
        num = ord(user_input[i])
        if num > 126 or num < 32 :                    
            print("Can't process what you typed")
            break
        else:
            if (num >= 65 and num <= 90) or (num >= 97 and num <= 122):
                num += 13
                user_input[i] = chr(num)
    print("".join(user_input))

