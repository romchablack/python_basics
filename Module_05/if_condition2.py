distance1 = int(input("Введіть довжину першого маршруту: "))
distance2 = int(input("Введіть довжину другого маршруту: "))

if distance1 < distance2:
    min = distance1
else:
    min = distance2

print("Мінімальний маршрут =", min)
