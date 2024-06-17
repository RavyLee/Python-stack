# Считываем количество чисел в первом списке
N = int(input())

# Считываем первый список чисел
first_list = []
for _ in range(N):
    first_list.append(int(input()))

# Считываем количество чисел во втором списке
M = int(input())

# Считываем второй список чисел
second_list = []
for _ in range(M):
    second_list.append(int(input()))

# Преобразуем списки в множества
first_set = set(first_list)
second_set = set(second_list)

# Находим пересечение двух множеств
intersection = first_set.intersection(second_set)

# Выводим количество элементов в пересечении
print(len(intersection))