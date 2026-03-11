"""
Q8. Create a HotelRoom class that:
•	Keeps a base price per night (shared).
•	Each room has room_number, nights_booked, and guest_name.
•	Has a method to calculate total bill.
•	Allows updating the base price across all rooms.
•	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
Demonstrate:
1.	Creating rooms and bookings.
2.	Changing base price.
3.	Checking bill updates and validation.
"""

class HotelRoom:
    base_price=700
    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number = room_number
        self.nights_booked = nights_booked
        self.guest_name = guest_name
    def total_bill(self):
        bill = self.nights_booked * HotelRoom.base_price
        return bill
    @classmethod
    def new_price(cls, new_price):
        cls.base_price = new_price
    @staticmethod
    def is_valid(nights):
        return nights > 0

h1 = HotelRoom(201,4,"Rishi")
print(h1.total_bill())
print(h1.is_valid(h1.nights_booked))
h1.new_price(800)
print(h1.total_bill())