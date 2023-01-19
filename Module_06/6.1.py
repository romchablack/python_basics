number = int(input("Введіть шуканий член арифметичної прогресії "))

# your code goes here
start = 5
step = 3

for i in range(1, number):
    start = start + step

print(start)
