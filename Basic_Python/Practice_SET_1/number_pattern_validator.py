number = input()

if all(prev < curr for prev, curr in zip(number, number[1:])):
    print("YES")
else:
    print("NO")
