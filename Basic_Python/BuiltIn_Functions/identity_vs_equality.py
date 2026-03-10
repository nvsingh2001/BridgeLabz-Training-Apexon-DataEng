a = [1, 2, 3]
b = [1, 2, 3]

c = a

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is c)

print(a == b)

a.append(4)

print(c)
