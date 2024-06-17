def factorial(n):
    """
    Функция для вычисления факториала числа n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def factorial_list(number):
    """
    Функция для создания списка факториалов чисел от number до 1.
    """
    result = []
    for i in range(number, 0, -1):
        result.append(factorial(i))
    return result

# Пример использования
number = 3
fact_number = factorial(number)
result_list = factorial_list(fact_number)
print(result_list)