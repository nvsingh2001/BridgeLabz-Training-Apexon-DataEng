nums = [1, 2, 3, 4, 5, 6]

string_num = list(map(str, nums))

print(string_num)

print(list(filter(lambda num: num % 2 == 0, nums)))
