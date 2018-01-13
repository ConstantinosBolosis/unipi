while True:
    user_input = input("Roman Number Converter (Type 'exit' to quit)\nType in an integer up to 3999:\n")
    if user_input == "exit":
        break
    try:
        check = int(user_input)
    except ValueError:
        print("\nPlease, input an integer up to 3999!")
        continue
    else:
        if int(user_input) > 3999:
            print("\nPlease, input an integer up to 3999!")
            continue
        print("well, that's an integer up to 3999, nice")
        digits = list(user_input)
        for i in range (4):
            digits[i] = int(digits[i])
        if len(digits) != 4:
            for i in range (4 - len(digits)):
                digits.insert(0, 0)
        thousands = digits[0] * "M"
        print(0 * ":P")
        break
