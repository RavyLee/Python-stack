# Считываем количество чисел
N = int(input())

# Считываем сами числа через пробел и превращаем их в список чисел
numbers = list(map(int, input().split()))

# Создаем множество для хранения уникальных чисел
unique_numbers = set(numbers)

# Выводим количество уникальных чисел
print(len(unique_numbers))