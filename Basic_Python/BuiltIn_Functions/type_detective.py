list1 = [10, 3.14, "hello", [1, 2], (5, 6), {1, 2}, {"a": 1}, True]

count_numeric = 0

for i in list1:
    if isinstance(i, (int, float, complex)):
        count_numeric += 1

print([type(i) for i in list1])
print(count_numeric)

print(isinstance(True, int))

print(bool.__base__)

print(True + True)
