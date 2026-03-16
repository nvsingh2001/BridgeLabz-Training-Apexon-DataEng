def reverse_words(sentence):
    words = sentence.split()
    revesed = [word[::-1] for word in words]

    return " ".join(revesed)


print(reverse_words("Python is a very language"))
