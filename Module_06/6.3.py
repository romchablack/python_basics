number = int(input("Введіть число"))

# your code goes here
n = 0
while n <= number:
    if n % 2 == 0:
        print(n**2)
    else:
        print(n)
    n += 1
