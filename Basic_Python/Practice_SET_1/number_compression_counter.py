input_number = int(input())

number = input_number

counter = 0

while number % 2 == 0 and number > 0:
    number //= 2
    counter += 1

print(counter)
