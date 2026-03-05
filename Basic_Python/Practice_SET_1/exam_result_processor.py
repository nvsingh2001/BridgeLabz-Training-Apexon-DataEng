marks = list(map(int, input().split()))

if len(marks) > 5:
    raise ValueError("Input should contains marks of 5 subjects only")

average_marks = sum(marks) / len(marks)

if any(mark < 35 for mark in marks):
    print("FAIL")
elif average_marks >= 75:
    print("DISTINCTION")
else:
    print("PASS")
