from car import Car


def main():
    my_car = Car("blue", 5)

    my_car.get_message()
    my_car.get_colour()
    my_car.get_free_seats()
    my_car.enter_passengers(4)
    my_car.get_free_seats()
    my_car.enter_passengers(2)

    my_new_car = Car("Green", 2)
    my_new_car.get_colour()
    my_new_car.get_free_seats()


if __name__ == "__main__":
    main()
