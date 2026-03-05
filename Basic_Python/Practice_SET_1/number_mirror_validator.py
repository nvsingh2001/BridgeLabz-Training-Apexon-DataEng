def reverse_number(num):
    rev_num = 0
    while num:
        rev_num = rev_num * 10 + (num % 10)
        num //= 10
    return rev_num


num = int(input())

if num == reverse_number(num):
    print("PALINDROME")
else:
    print("NOT PALINDROME")
