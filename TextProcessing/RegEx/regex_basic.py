import re
from typing import Counter

# pattern = "^a.[1-9A-Z].s$"
#
# test_string = "ab4ss"
#
# result = re.match(pattern, test_string)
#
# if result:
#     print("Search Successful.")
# else:
#     print("Search Unsucsessful.")

string = "hello 12 hi 89. Howdy 34"

pattern = r"\d+"

result = re.findall(pattern, string)
print(result)

result = re.split(pattern, string)
print(result)

string_2 = "Order123 shipped45 on2024"

print(re.findall(r"\d", string_2))

urls = ["https://google.com", "https://example.com"]

for url in urls:
    if re.match(r"^https", url):
        print("Yes")
    else:
        print("No")

string_3 = "a1b2c3"

print(re.sub(r"\d", "#", string_3))

print(re.split(r",|\s", "apple,banana orange,grape"))

print(re.findall(r"\b\w{4}\b", "This is a test code snippet"))

print(re.findall(r"\ba\w*", "apple bat ant anchor ball"))

print(len(re.findall(r"\bcat\b", "cat bat cat rat cat")))


count = sum(1 for _ in re.finditer(r"\bcat\b", "cat bat cat rat cat"))

print(count)

print(re.sub(r"\s{2,}", " ", "Hello    world   python"))

print(re.split(r"\d+\s\b", "abc123 def456 ghi"))

print(re.findall(r"\b(\w+)\s+\1\b", "This is is a test test string"))

repeated_words = [
    m.group() for m in re.finditer(r"\b(\w+)\s+\1\b", "This is is a test test string")
]

print(repeated_words)
