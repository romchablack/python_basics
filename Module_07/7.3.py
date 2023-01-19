number = int(input("Введіть число"))


def print_numbers(number):
    for i in range(0, number+1, 2):
        print(i)


print_numbers(number)
