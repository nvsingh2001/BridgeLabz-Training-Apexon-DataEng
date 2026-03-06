import random

num_coin_flip = int(input("Enter the number times the coin needs to be flipped: "))

heads = 0
tails = 0

for _ in range(num_coin_flip):
    if random.random() > 0.5:
        heads += 1
    else:
        tails += 1

print(f"Heads Percentage: {heads / num_coin_flip * 100:.2f}")
print(f"Tails Percentage: {tails / num_coin_flip * 100:.2f}")
