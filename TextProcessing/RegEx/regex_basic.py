import re

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
