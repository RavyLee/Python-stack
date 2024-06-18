class Черепашка:
    def __init__(self, x=0, y=0, s=1):
        self.x = x  # Начальная позиция по оси x
        self.y = y  # Начальная позиция по оси y
        self.s = s  # Количество клеток, на которое черепашка перемещается за ход

    def go_up(self):
        self.y += self.s  # Увеличиваем y на s

    def go_down(self):
        self.y -= self.s  # Уменьшаем y на s

    def go_left(self):
        self.x -= self.s  # Уменьшаем x на s

    def go_right(self):
        self.x += self.s  # Увеличиваем x на s

    def evolve(self):
        self.s += 1  # Увеличиваем s на 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1  # Уменьшаем s на 1, если s больше 1
        else:
            raise ValueError("s не может быть меньше или равно 0")

    def count_moves(self, x2, y2):
        # Вычисляем минимальное количество ходов для достижения (x2, y2)
        x_distance = abs(x2 - self.x)  # Расстояние по оси x
        y_distance = abs(y2 - self.y)  # Расстояние по оси y
        
        # Вычисляем количество ходов для каждой координаты
        x_moves = x_distance // self.s
        if x_distance % self.s != 0:
            x_moves += 1
            
        y_moves = y_distance // self.s
        if y_distance % self.s != 0:
            y_moves += 1

        return x_moves + y_moves  # Общее количество ходов

# Пример использования:
черепашка = Черепашка(0, 0, 1)
черепашка.go_up()
черепашка.go_right()
print(черепашка.x, черепашка.y)  # Должно вывести: 1 1
print(черепашка.count_moves(3, 3))  # Должно вывести: 6
черепашка.evolve()
print(черепашка.s)  # Должно вывести: 2
черепашка.go_right()
print(черепашка.x, черепашка.y)  # Должно вывести: 3 1
