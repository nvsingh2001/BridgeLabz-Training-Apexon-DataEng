def most_frequent_character(text):
    freq = {}

    for ch in text:
        if not ch.isspace():
            freq[ch] = freq.setdefault(ch, 0) + 1

    max_char = None
    max_count = 0

    for character, frequecy in freq.items():
        if frequecy > max_count:
            max_char = character
            max_count = frequecy

    return max_char, max_count


print(most_frequent_character("mississippi river"))
