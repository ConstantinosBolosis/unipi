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
def digit2roman2(cur, one, five):
    if cur <= 4:
        return cur * one
    else:
        return five + (cur - 5) * one
print("Integer to Roman Numerals Converter (Type 'exit' to quit)")
while True:
    user_input = input("Type in an integer up to 1.000.000: ")
    if user_input == "exit":
        break
    try:
        check = int(user_input)
    except ValueError:
        print("\nInvalid input\n")
        continue
    else:
        if int(user_input) > 1000000:
            print("\nInvalid input\n")
            continue
        digits = list(user_input)
        if len(digits) != 7:
            for i in range (7 - len(digits)):
                digits.insert(0, 0)
        millions = int(digits[0]) * "M"
        hunthousands = digit2roman(int(digits[1]), "C", "D", "M")
        decthousands = digit2roman(int(digits[2]), "X", "L", "C")
        thousands = digit2roman2(int(digits[3]), "M", "V")
        hundreds = digit2roman(int(digits[4]), "C", "D", "M")
        tens = digit2roman(int(digits[5]), "X", "L", "C")
        ones = digit2roman(int(digits[6]), "I", "V", "X")
        dashmillions = int(digits[0]) * "_"
        dashhunthousands = digit2roman(int(digits[1]), "_", "_", "_")
        dashdecthousands = digit2roman(int(digits[2]), "_", "_", "_")
        dashthousands = digit2roman2(int(digits[3]), " ", "_")
        print(dashmillions + dashhunthousands + dashdecthousands + dashthousands)
        print (millions + hunthousands + decthousands + thousands + hundreds + tens + ones + "\n")
        continue
