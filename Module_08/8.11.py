line1 = input("Введіть перший рядок ")
line2 = input("Введіть другий рядок ")

# your code goes here
line11 = ''
line22 = ''

for x in line1:
    if x.isalpha():
        line11 += x.lower()
    else:
        line11 += x

for x in line2:
    if x.isalpha():
        line22 += x.lower()
    else:
        line22 += x

if line11 == line22:
    print("Рядки співпадають")
else:
    print("Рядки не співпадають")
