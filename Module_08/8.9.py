user = {
        'name': 'sergii',
        'age': 100500,
        'country': 'Ukraine'
        }

key = input("Введіть ім'я ключа ")
new_key = input("Введіть нове ім'я ключа ")

# your code goes here
if key in user.keys():
    for old_key in user.keys():
        if old_key == key:
            user[new_key] = user[old_key]
            del user[old_key]
            break
    print(user)
else:
    print("Шуканого ключа немає")
