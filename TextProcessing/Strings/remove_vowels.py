def remove_vowels(string):
    vowels = "aeiouAEIOU"

    result = []

    for ch in string:
        if ch not in vowels:
            result.append(ch)

    return "".join(result)


print(remove_vowels("Beautiful Day"))
