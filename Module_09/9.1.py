windows_count = int(input("Введіть кількість вікон "))
flors_count = int(input("Введіть кількість поверхів "))


class Building:
    def __init__(self, windows_count, flors_count):
        self.windows_count = windows_count
        self.flors_count = flors_count


building = Building(windows_count, flors_count)

print("Загальна кількість вікон {}".format(building.windows_count * building.flors_count))
