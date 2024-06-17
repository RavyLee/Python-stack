# Изначально пустой словарь для хранения данных о питомцах
pets = {}

# Функция для получения информации о питомце
def get_pet_info():
    # Запрос имени питомца
    pet_name = input("Введите имя питомца: ")

    # Запрос вида питомца
    pet_type = input("Введите вид питомца: ")

    # Запрос возраста питомца
    while True:
        try:
            pet_age = int(input("Введите возраст питомца: "))
            break
        except ValueError:
            print("Пожалуйста, введите корректный возраст (число).")

    # Запрос имени владельца
    owner_name = input("Введите имя владельца: ")

    # Заполнение словаря информацией о питомце
    pets[pet_name] = {
        'Вид питомца': pet_type,
        'Возраст питомца': pet_age,
        'Имя владельца': owner_name
    }

# Функция для получения правильного склонения слова "год"
def get_age_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"

# Запрос данных о питомце
get_pet_info()

# Получение данных из словаря и форматирование строки
for pet_name, pet_info in pets.items():
    pet_type = pet_info['Вид питомца']
    pet_age = pet_info['Возраст питомца']
    owner_name = pet_info['Имя владельца']
    age_suffix = get_age_suffix(pet_age)
    print(f"Это {pet_type} по кличке \"{pet_name}\". Возраст питомца: {pet_age} {age_suffix}. Имя владельца: {owner_name}")

# Убрал вывод содержимого словаря pets
