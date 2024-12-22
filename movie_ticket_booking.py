def book_seat(total_seats, booked_seats, seat_to_book):
    if seat_to_book in booked_seats:
        print(f"Seat {seat_to_book} is already booked!")
    elif seat_to_book > total_seats or seat_to_book < 1:
        print(f"Invalid seat number {seat_to_book}. Please choose a seat between 1 and {total_seats}.")
    else:
        booked_seats.append(seat_to_book)

def cancel_seat(booked_seats, seat_to_cancel):
    if seat_to_cancel in booked_seats:
        booked_seats.remove(seat_to_cancel)
    else:
        print(f"Seat {seat_to_cancel} was not booked!")

def get_available_seats(total_seats, booked_seats):
    available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return available_seats

total_seats = 10
booked_seats = [2, 5, 7]
book_seat_number = 3
cancel_seat_number = 5

book_seat(total_seats, booked_seats, book_seat_number)

cancel_seat(booked_seats, cancel_seat_number)

available_seats = get_available_seats(total_seats, booked_seats)
print(f"Available seats: {available_seats}")
