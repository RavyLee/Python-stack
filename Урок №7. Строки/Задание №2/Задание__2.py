# Считываем строку
input_string = input()

# Разбиваем строку на слова
words = input_string.split()

# Соединяем слова обратно в строку с одним пробелом между ними
result_string = ' '.join(words)

# Выводим изменённую строку
print(result_string)
