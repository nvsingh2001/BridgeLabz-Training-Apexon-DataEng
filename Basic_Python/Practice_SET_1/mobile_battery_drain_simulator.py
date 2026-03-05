drain_per_minute = int(input())

battery = 100

if not (0 < drain_per_minute <= 100):
    raise ValueError("Drain per minute must be between 0 and 100")

minutes = 0

while battery > 0:
    battery -= drain_per_minute
    minutes += 1

print(minutes)
