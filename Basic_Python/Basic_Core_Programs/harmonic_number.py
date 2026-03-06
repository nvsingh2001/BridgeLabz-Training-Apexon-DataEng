n = int(input())

if n == 0:
    print("Input cannot be 0")
else:
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i
    print(sum)
