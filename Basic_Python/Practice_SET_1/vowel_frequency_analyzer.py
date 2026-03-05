sentence = input()

vowels = {"a", "e", "i", "o", "u"}

counter = 0
for character in sentence.lower():
    if character in vowels:
        counter += 1

print(counter)
