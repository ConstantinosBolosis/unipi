while True:
    user_input = input("Feel free to write something: ")
    for i in range (len(list(user_input))):
        check = ord(list(user_input)[i])
        if check > 126 or check < 32 :                    
            print("Can't process what you typed")
            break
        