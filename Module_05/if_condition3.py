count = float(input("Введіть бажану кількість електроенергії: "))
tariff = 7.80
price = tariff * count
print("Ціна заряджання =", round(price, 2))

cash = float(input("Введіть суму готівки: "))
if cash >= price:
    rest = cash - price
    print("Решта =", round(rest, 2))
else:
    print("Недостатньо готівки")

    


