number = int(input("Введіть число"))


def is_even_or_odd(number):
    if number % 2 == 0:
        return "число {x} парне".format(x=number)
    else:
        return "число {x} непарне".format(x=number)


print(is_even_or_odd(number))
