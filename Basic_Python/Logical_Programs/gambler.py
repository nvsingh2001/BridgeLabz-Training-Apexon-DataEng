import random


def gamble(stake, goal):
    while 0 < stake < goal:
        stake += random.choice([-1, 1])

    return stake >= goal


stake, goal, num_times = map(int, input().split())

if stake <= 0:
    raise ValueError("Stake should be greater than 0")
elif goal <= stake:
    raise ValueError("Goal cannot be less than Stake")
elif num_times <= 0:
    raise ValueError("Number of times should be greater than 0")

wins = 0

for _ in range(num_times):
    if gamble(stake, goal):
        wins += 1

loss = num_times - wins

print(f"Win Percentage: {wins / num_times * 100:.2f}")
print(f"Loss Percentage: {loss / num_times * 100:.2f}")
