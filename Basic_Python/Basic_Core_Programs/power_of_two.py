import sys

n = int(sys.argv[1])

if not (0 <= n < 31):
    print("Input should be between 0 and 31")
else:
    for num in range(n + 1):
        print(f"2 ^ {num} = {2**num}")
