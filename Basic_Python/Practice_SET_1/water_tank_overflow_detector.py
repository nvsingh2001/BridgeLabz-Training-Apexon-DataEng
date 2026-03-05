TANK_CAPACITY = 1000

num_of_minutes = int(input())

inflows = list(map(int, input().split()))

if len(inflows) != num_of_minutes:
    raise ValueError("Number of inflows should be equal to Number of minutes")

vol_of_water = 0

for minute, inflow in enumerate(inflows, start=1):
    vol_of_water += inflow
    if vol_of_water > TANK_CAPACITY:
        print(minute)
        break
