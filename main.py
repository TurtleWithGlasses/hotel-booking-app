import pandas as pd

df = pd.read_csv("hotels.csv")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        pass


    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object
    def generate(self):
        pass


print(df)
hotel_ID = input("Enter the id of the hotel")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservartion_ticket = ReservationTicket(name, hotel)
    print(reservartion_ticket.generate())
else:
    print("Hotel is not available...")

