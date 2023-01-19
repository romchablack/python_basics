number = int(input("Введіть число "))
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# your code goes here
match = 0

for element in a:
    if number == element:
        match = 1
        break

if match == 1:
    print("Введене число - існує")
else:
    print("Введене число - не існує")
