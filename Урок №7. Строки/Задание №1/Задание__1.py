# Считываем строку
input_string = input()

# Проверяем, является ли строка палиндромом
if input_string == input_string[::-1]:
    print("yes")
else:
    print("no")
