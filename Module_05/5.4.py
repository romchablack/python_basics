temp = int(input("Enter C tempetature, int value: "))

if temp <= 0:
    print("Лід")
elif temp > 0 and temp < 100:
    print("Вода")
else:
    print("Пара")
