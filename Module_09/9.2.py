car_1 = input("Введіть марку автомобіля 1 ")
car_2 = input("Введіть марку автомобіля 2 ")
car_3 = input("Введіть марку автомобіля 3 ")


class Cars:
    list_of_cars = []

    def __init__(self, car):
        self.list_of_cars.append(car)

    # def add_car(self, car):
    #     self.list_of_cars.append(car)


cars = Cars(car_1)
cars = Cars(car_2)
cars = Cars(car_3)


print("Список авто: " + "{}".format(" та ".join(Cars.list_of_cars)))
