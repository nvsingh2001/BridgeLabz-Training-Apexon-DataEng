def insert_middle(s1, s2):
    mid = len(s1) // 2

    return s1[:mid] + s2 + s1[mid:]


s1 = "Hello World"
s2 = " Python"

print(insert_middle(s1, s2))
