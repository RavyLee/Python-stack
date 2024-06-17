# Запрашиваем у пользователя ввод слова
word = input("Введите слово из маленьких латинских букв: ")

# Определяем гласные буквы
vowels = 'aeiou'

# Инициализируем счётчики для гласных и согласных букв
vowel_count = 0
consonant_count = 0

# Инициализируем словарь для подсчёта каждой гласной
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Проходим по каждой букве в слове
for letter in word:
    if letter in vowels:
        vowel_count += 1
        vowel_counts[letter] += 1
    else:
        consonant_count += 1

# Выводим результаты
print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)
print("Количество 'a':", vowel_counts['a'])
print("Количество 'e':", vowel_counts['e'])
print("Количество 'i':", vowel_counts['i'])
print("Количество 'o':", vowel_counts['o'])
print("Количество 'u':", vowel_counts['u'])

# Проверяем, есть ли отсутствующие гласные
missing_vowels = False
for vowel in vowels:
    if vowel_counts[vowel] == 0:
        missing_vowels = True

print("Отсутствуют ли какие-то гласные?", missing_vowels)
