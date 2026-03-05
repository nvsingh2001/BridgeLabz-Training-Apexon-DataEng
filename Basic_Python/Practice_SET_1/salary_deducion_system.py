salary = int(input())
late_days = int(input())
absent_days = int(input())

penalty_rate = 0

if 5 < late_days <= 10:
    penalty_rate += 0.05
elif late_days > 10:
    penalty_rate += 0.1

if absent_days > 2:
    penalty_rate += 0.05

final_salary = salary * (1 - penalty_rate)
print(final_salary)
