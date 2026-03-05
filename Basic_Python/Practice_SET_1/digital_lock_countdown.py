def sum_of_digits(num: int) -> int:
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total


num = int(input())

while num >= 10:
    num -= sum_of_digits(num)

print(num)
