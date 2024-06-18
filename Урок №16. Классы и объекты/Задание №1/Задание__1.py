class Касса:
    def __init__(self):
        self.balance = 0

    def top_up(self, X):
        """Пополнить кассу на X."""
        self.balance += X
        print(f"Касса пополнена на {X}. Текущий баланс: {self.balance}")

    def count_1000(self):
        """Вывести количество целых тысяч в кассе."""
        thousands = self.balance // 1000
        print(f"Целых тысяч в кассе: {thousands}")
        return thousands

    def take_away(self, X):
        """Забрать X из кассы, либо выкинуть ошибку."""
        if X > self.balance:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= X
        print(f"Из кассы взято {X}. Текущий баланс: {self.balance}")

# Пример использования класса
касса = Касса()

# Пополнение кассы
касса.top_up(500)
касса.top_up(2000)

# Проверка целых тысяч
касса.count_1000()

# Снятие денег из кассы с обработкой ошибки
try:
    касса.take_away(1500)
except ValueError as e:
    print(e)

# Еще одна попытка снять деньги из кассы
try:
    касса.take_away(2000)  # Это вызовет ошибку, так как недостаточно средств
except ValueError as e:
    print(e)
