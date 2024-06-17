# Считываем число N
N = int(input())

# Создаем список для хранения чисел
numbers = []

# Считываем N чисел и добавляем их в список
for _ in range(N):
    number = int(input())
    numbers.append(number)

# Переворачиваем список
numbers.reverse()

# Выводим перевернутый список чисел
for number in numbers:
    print(number)
