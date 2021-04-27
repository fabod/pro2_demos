class Car:
    def __init__(self, colour, seats):
        self.colour = colour
        self.seats = seats
        self.message = f"Brumm brumm I am a {self.colour} car."
        self.get_message()

    def get_colour(self):
        print(f"The car's colour is {self.colour}")

    def get_message(self):
        print(self.message)

    def get_free_seats(self):
        print(f"The car has {self.seats} free seats.")

    def enter_passengers(self, passengers):
        if passengers > self.seats:
            print("There are not enough seats in the car")
        else:
            self.seats = self.seats - passengers

        self.get_free_seats()