# Считываем последовательность чисел через пробел
numbers = list(map(int, input().split()))

# Создаем пустое множество для отслеживания встреченных чисел
seen_numbers = set()

# Проходим по каждому числу в последовательности
for number in numbers:
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(number)
