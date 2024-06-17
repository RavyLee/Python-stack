# Запрашиваем у пользователя пятизначное число
number = int(input("Введите пятизначное число: "))

# Выделяем необходимые разряды
units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = (number // 10000) % 10

# Возводим количество десятков в степень количества единиц
result = tens ** units

# Умножаем результат на количество сотен
result *= hundreds

# Находим разность между количеством десятков тысяч и количеством тысяч
difference = ten_thousands - thousands

# Делим результат на разность
if difference != 0:
    result /= difference
else:
    print("Ошибка: разность между десятками тысяч и тысячами равна нулю, деление невозможно.")
    result = None

# Выводим результат
if result is not None:
    print("Результат:", result)