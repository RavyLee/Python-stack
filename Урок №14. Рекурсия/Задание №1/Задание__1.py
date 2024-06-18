def print_list_recursively(my_list, index=0):
    # Базовый случай: если индекс выходит за пределы списка, выводим сообщение
    if index >= len(my_list):
        print("Конец списка")
        return
    # Вывод текущего элемента
    print(my_list[index])
    # Рекурсивный вызов функции для следующего элемента
    print_list_recursively(my_list, index + 1)

# Исходный список
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Вызов функции для печати элементов списка
print_list_recursively(my_list)

