deposit_amount = float(input("Введіть початкову суму депозиту "))
annual_rate = float(input("Введіть річну відсоткову ставку "))
desired_amount = float(input("Введіть бажану суму накопичення "))

deposit_period = 0

while deposit_amount < desired_amount: # умова циклу
    deposit_period = deposit_period + 1 # термін депозиту збільшуємо на 1 рік
    deposit_amount = deposit_amount + deposit_amount * (annual_rate / 100) #збільшити суму депозиту

print("Очікуваний термін депозиту =", deposit_period, "років")
