def digit2roman(cur, one, five, ten):
    if cur <= 3:
        return cur * one
    elif cur == 4:
        return one + five
    elif cur >= 5 and cur <= 8:
        return five + (cur - 5) * one
    else:
        return one + ten
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
        digits = list(user_input)
        if len(digits) != 4:
            for i in range (4 - len(digits)):
                digits.insert(0, 0)
        thousands = int(digits[0]) * "M"
        hundreds = digit2roman(int(digits[1]), "C", "D", "M")
        tens = digit2roman(int(digits[2]), "X", "L", "C")
        ones = digit2roman(int(digits[3]), "I", "V", "X")
        print (thousands + hundreds + tens + ones + "\n")
        continue
