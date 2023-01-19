print("Введіть довжину першого маршруту")
distance1 = int(input())
print("Введіть довжину другого маршруту")
distance2 = int(input())

if distance1 < distance2:
    min = distance1

if distance2 <= distance1:
    min = distance2

print("Мінімальний маршрут =", min)
