input_string = input()

input_string = input_string.lower()

if input_string == input_string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
