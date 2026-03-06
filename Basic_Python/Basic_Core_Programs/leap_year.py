while True:
    year = int(input("Enter the year: "))
    if year < 1000:
        print("Year should be atleast 4 digit.")
    else:
        break

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
