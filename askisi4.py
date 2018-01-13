#Python 3.6 -- Constantinos Bolosis -- P17085 -- Integer to Roman Numerals Converter :P

def digit2roman(cur, one, five, ten):
    if cur <= 3:
        return cur * one
    elif cur == 4:
        return one + five
    elif cur >= 5 and cur <= 8:
        return five + (cur - 5) * one
    else:
        return one + ten
print("Integer to Roman Numerals Converter (Type 'exit' to quit)")
while True:
    user_input = input("Type in an integer up to 3999: ")
    if user_input == "exit":
        break
    try:
        check = int(user_input)
    except ValueError:
        print("\nInvalid input\n")
        continue
    else:
        if int(user_input) > 3999:
            print("\nInvalid input\n")
            continue
        digits = list(user_input)
        if len(digits) != 4:
            for i in range (4 - len(digits)):
                digits.insert(0, 0)
        thousands = int(digits[0]) * "M"
        hundreds = digit2roman(int(digits[1]), "C", "D", "M")
        tens = digit2roman(int(digits[2]), "X", "L", "C")
        ones = digit2roman(int(digits[3]), "I", "V", "X")
        print ("\n" + thousands + hundreds + tens + ones + "\n")
        continue
