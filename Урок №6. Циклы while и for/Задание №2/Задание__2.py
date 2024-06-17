# Запрашиваем у пользователя ввод натурального числа X
X = int(input("Введите натуральное число X: "))

# Инициализируем счётчик делителей
divisor_count = 0

# Проверяем делители от 1 до квадратного корня из X
import math
sqrt_X = int(math.sqrt(X))

for i in range(1, sqrt_X + 1):
    if X % i == 0:
        divisor_count += 1
        if i != X // i:
            divisor_count += 1

# Выводим результат
print("Количество натуральных делителей числа:", divisor_count)
