def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


print(reverse_words("Python is a very language"))
