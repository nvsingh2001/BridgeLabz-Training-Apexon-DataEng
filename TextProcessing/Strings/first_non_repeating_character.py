from collections import Counter


string = "aabbcde"

count = Counter(string)

result = next((ch for ch in string if count[ch] == 1), None)

print(result)

for freq in count.items():
    print(freq)
