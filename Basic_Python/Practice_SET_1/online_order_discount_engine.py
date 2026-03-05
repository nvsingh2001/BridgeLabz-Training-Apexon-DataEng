amount = int(input())

discount = 0

if amount >= 5000:
    discount = 0.2
elif amount >= 3000:
    discount = 0.1
elif amount >= 1000:
    discount = 0.05

payable_amount = int(amount * (1 - discount))

print(payable_amount)
