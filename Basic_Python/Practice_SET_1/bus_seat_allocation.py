TOTAL_NUMBER_OF_SEATS = 40

number_requests = int(input())

requests = []

for _ in range(number_requests):
    requests.append(int(input()))

booked_seats = 0

for request in requests:
    booked_seats += request
    if booked_seats <= TOTAL_NUMBER_OF_SEATS:
        print("CONFIRMED")
    else:
        print("WAITLISTED")
        break
