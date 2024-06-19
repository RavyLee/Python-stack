class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Создание объекта класса Transport
transport = Transport("Renaul Logan", 180, 12)

# Вывод информации об объекте
print(f"Название автомобиля: {transport.name} Скорость: {transport.max_speed} Пробег: {transport.mileage}")
