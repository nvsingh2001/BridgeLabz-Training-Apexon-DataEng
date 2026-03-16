def count_vowels_consonants(s):
    vowels = "aeiou"
    count_vowels = 0
    count_consonants = 0

    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                count_vowels += 1
            else:
                count_consonants += 1

    return count_vowels, count_consonants


text = "Hello, Python 3!"

print(count_vowels_consonants(text))
