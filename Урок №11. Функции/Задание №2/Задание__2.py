import collections

# База данных питомцев
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
    # добавьте дополнительные записи, если необходимо
}

def get_pet(ID):
    # Получение информации о питомце по ID
    return pets.get(ID, False)

def get_suffix(age):
    # Получение суффикса для возраста питомца
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

def pets_list():
    # Вывод всего списка питомцев
    for ID, pet_info in pets.items():
        for name, details in pet_info.items():
            print(f"ID: {ID}, Имя: {name}, Вид: {details['Вид питомца']}, Возраст: {details['Возраст питомца']} {get_suffix(details['Возраст питомца'])}, Владелец: {details['Имя владельца']}")

def create():
    # Создание новой записи о питомце
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1

    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Питомец {name} добавлен с ID {new_id}.")

def read():
    # Чтение информации о питомце
    ID = int(input("Введите ID питомца: "))
    pet_info = get_pet(ID)
    if pet_info:
        for name, details in pet_info.items():
            print(f"Это {details['Вид питомца']} по кличке \"{name}\". Возраст питомца: {details['Возраст питомца']} {get_suffix(details['Возраст питомца'])}. Имя владельца: {details['Имя владельца']}")
    else:
        print("Питомец с таким ID не найден.")

def update():
    # Обновление информации о питомце
    ID = int(input("Введите ID питомца: "))
    pet_info = get_pet(ID)
    if pet_info:
        name = input("Введите новое имя питомца (оставьте пустым, чтобы не изменять): ")
        pet_type = input("Введите новый вид питомца (оставьте пустым, чтобы не изменять): ")
        age = input("Введите новый возраст питомца (оставьте пустым, чтобы не изменять): ")
        owner = input("Введите новое имя владельца (оставьте пустым, чтобы не изменять): ")

        for pet_name in pet_info:
            if name:
                pet_info[name] = pet_info.pop(pet_name)
                pet_name = name
            if pet_type:
                pet_info[pet_name]["Вид питомца"] = pet_type
            if age:
                pet_info[pet_name]["Возраст питомца"] = int(age)
            if owner:
                pet_info[pet_name]["Имя владельца"] = owner
        
        pets[ID] = pet_info
        print(f"Информация о питомце с ID {ID} обновлена.")
    else:
        print("Питомец с таким ID не найден.")

def delete():
    # Удаление информации о питомце
    ID = int(input("Введите ID питомца: "))
    if ID in pets:
        del pets[ID]
        print(f"Питомец с ID {ID} удалён.")
    else:
        print("Питомец с таким ID не найден.")

# Основной цикл программы
command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, list, stop): ").strip().lower()
    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Программа завершена.")
    else:
        print("Неверная команда. Пожалуйста, попробуйте снова.")
    