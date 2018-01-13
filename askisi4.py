
while True:
    try:
        user_input = int(input("Roman Number Converter\nType in an integer up to 3999:\n"))
    except ValueError:
        print("\n\nPlease, input an integer up to 3999!")
        continue
    else:
        if int(user_input) > 3999:
            print("\n\nPlease, input an integer up to 3999!")
            continue
        print("well, that's an integer up to 3999, nice")
        break
