def count_types(text):
    letters = digits = spaces = others = 0

    for ch in text:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            others += 1

    return letters, digits, spaces, others


text = "Hi 123! @Python"
print(count_types(text))
