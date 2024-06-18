class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass

# Создание объекта класса Autobus
autobus = Autobus("Renaul Logan", 180, 12)

# Вывод информации об объекте
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")

