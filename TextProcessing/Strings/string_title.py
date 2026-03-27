string = "hello world python"

words = string.split()

result = []

for word in words:
    result.append(word.capitalize())

print(" ".join(result))
