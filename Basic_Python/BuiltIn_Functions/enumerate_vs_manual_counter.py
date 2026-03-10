words = ["apple", "banana", "cherry"]

# Manual Counter
counter = 0

for i in words:
    print(f"{counter} {i}")
    counter += 1

# Using enumerate()
for word, index in enumerate(words):
    print(f"{word} {index}")
