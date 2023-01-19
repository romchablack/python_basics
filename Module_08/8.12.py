s = input("Enter your text: ")
flag = 0

for x in ("ы", "ъ", "ё", "э"):
    if x in s:
        flag = 1
        break

if flag == 1:
    print("Ми не обслуговуємо замовлення мовою окупантів. Слава Україні!")
else:
    print("Дякуємо за замовлення!")
