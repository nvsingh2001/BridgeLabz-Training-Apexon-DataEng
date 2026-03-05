distance = int(input())
age = int(input())

BASE_RATE = 2

discount = 0

if age >= 60:
    discount = 0.3
elif age < 12:
    discount = 0.5

fare = distance * BASE_RATE
fare = fare * (1 - discount)
