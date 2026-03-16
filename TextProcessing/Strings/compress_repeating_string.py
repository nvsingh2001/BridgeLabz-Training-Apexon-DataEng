def compress_string(text):
    if not text:
        return ""

    result = []

    current = text[0]
    count = 1

    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            result.append(current + str(count))
            current = ch
            count = 1

    result.append(current + str(count))

    return "".join(result)


print(compress_string("aaabbbccccdddaae"))

