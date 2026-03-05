def apply_slab(units, rate):
    return units * rate


units = int(input())
original_units = units

bill = apply_slab(min(units, 100), 3)
units -= 100

if units > 0:
    bill += apply_slab(min(units, 100), 5)
    units -= 100

if units > 0:
    bill += apply_slab(units, 8)

if original_units > 300:
    bill += bill * 0.1

print(round(bill, 2))
