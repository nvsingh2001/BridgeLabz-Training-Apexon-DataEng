squares_generators = (x**2 for x in range(10))

print(next(squares_generators))
print(next(squares_generators))
print(next(squares_generators))
print(next(squares_generators))
print(next(squares_generators))

even_squares = (x**2 for x in range(10) if x % 2 == 0)
for num in even_squares:
    print(num)

data = range(1, 11)

pipeline = (x**2 for x in (n for n in data if n % 2 == 0))

print(list(pipeline))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = (num for row in matrix for num in row)
print(list(flat))


def running_total():
    total = 0
    while True:
        number = yield total
        if number is None:
            break
        total += number


calc = running_total()
next(calc)

print(calc.send(10))
print(calc.send(20))
print(calc.send(20))
