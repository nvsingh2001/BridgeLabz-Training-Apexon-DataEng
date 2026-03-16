def remove_duplicates(text):
    seen = set()
    result = []

    for ch in text:
        if ch not in seen:
            result.append(ch)
            seen.add(ch)

    return "".join(result)


print(remove_duplicates("banana"))
