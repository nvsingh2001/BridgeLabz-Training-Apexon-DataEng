# import math

# def countDigit(number):
#     return math.floor(math.log10(number) + 1)

number = int(input())

original_number = number

digit_sum = 0

num_of_digits = len(str(number))

while number > 0:
    digit = number % 10
    digit_sum += digit**num_of_digits
    number //= 10

if digit_sum == original_number:
    print("YES")
else:
    print("NO")
