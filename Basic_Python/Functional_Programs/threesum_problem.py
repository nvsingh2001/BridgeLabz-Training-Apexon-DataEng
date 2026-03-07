numbers = list(map(int, input().split()))

numbers.sort()

for i in range(len(numbers) - 2):
    left = i + 1
    right = len(numbers) - 1
    while left < right:
        sum = numbers[i] + numbers[left] + numbers[right]
        if sum == 0:
            print(numbers[i], numbers[left], numbers[right])
            left += 1
        elif sum < 0:
            left += 1
        else:
            right -= 1
