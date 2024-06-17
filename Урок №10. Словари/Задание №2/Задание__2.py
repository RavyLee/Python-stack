# Создание словаря с использованием цикла for
my_dict = {}

for i in range(10, -6, -1):
    my_dict[i] = i ** i

# Вывод содержимого словаря
for key, value in my_dict.items():
    print(f"{key}: {value}")


print("Словарь my_dict:", my_dict)
