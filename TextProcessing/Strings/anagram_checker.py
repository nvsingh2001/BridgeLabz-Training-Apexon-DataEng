def are_anagram(s1, s2):

    def normalize(s):
        return sorted(ch.lower() for ch in s if ch.isalpha())

    return normalize(s1) == normalize(s2)


print(are_anagram("Listen", "Silent"))
print(are_anagram("Dormitory", "Dirty room"))
