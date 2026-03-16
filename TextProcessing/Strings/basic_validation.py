input_string = input()

if input_string.isdigit():
    print("Only digits")
elif input_string.isalpha():
    print("Only letters")
else:
    print("Mixed")

