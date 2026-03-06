while True:
    name = input("Enter your name: ")
    if len(name) < 3:
        print("Name cannot be less than 3 character")
    else:
        break

print(f"Hello {name}, How are you?")
