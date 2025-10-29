def book_seat_func(booked, seat):
    if seat in booked:
        print(f"Seat {seat} is already booked.")
    elif seat < 1 or seat > total_seats:
        print(f"Seat {seat} is invalid.")
    else:
        booked.append(seat)

def cancel_seat_func(booked, seat):
    if seat in booked:
        booked.remove(seat)
    else:
        print(f"Seat {seat} was not booked.")

total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5

book_seat_func(booked_seats, book_seat)
cancel_seat_func(booked_seats, cancel_seat)

all_seats = list(range(1, total_seats + 1))
available_seats = [seat for seat in all_seats if seat not in booked_seats]

print("Available seats:", available_seats)