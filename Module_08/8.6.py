str_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

element = input("Введіть елемент, який хочете видалити ")
if element in str_set:
    print(str_set - {element})
else:
    print(str_set)
