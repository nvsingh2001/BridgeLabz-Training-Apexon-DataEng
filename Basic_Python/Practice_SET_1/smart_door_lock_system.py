CORRECT_PIN = 4321

attempts = 3

while attempts > 0:
    input_pin = int(input())
    if input_pin == CORRECT_PIN:
        print("ACCESS GRANTED")
        break
    attempts -= 1
else:
    print("LOCKED")
