last_name = input("Введіть прізвище ")
name = input("Введіть ім'я ")
second_name = input("Введіть по батькові ")

if len(last_name) == 0 or len(name) == 0 or len(second_name) == 0:
    print("Не введений ключовий параметр")
else:
    print("{} {}.{}.".format(last_name, name[0], second_name[0]))
