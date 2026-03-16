# name = input()
#
# print(name)
# print(name.strip())
# print(name.strip().title())

text = "Python is fun, and Python is powerful"

count_python = text.count("Python")
first_fun = text.find("fun")

print(count_python)
print(first_fun)

items = "apple,banana,grapes"

items_list = items.split(",")

items_formmated = " | ".join(item for item in items_list)

print(items_list)
print(items_formmated)
