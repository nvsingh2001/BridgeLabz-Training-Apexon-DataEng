string = "apple banana orange umbrella"

words = string.split()

vowels = "aeiou"

result = [word for word in words if word[0].lower() in vowels]

print(result)
