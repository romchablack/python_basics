miles = float(input("Введіть кількість миль"))


def convert_miles_to_km(miles):
    return round(miles*1.6, 2)


print(convert_miles_to_km(miles))
