import random
import os
import time

# Константы
EMPTY = 0
TREE = 1
FIRE = 2
LAKE = 3
CLOUD = 4
THUNDER = 5

# Символы для отображения
SYMBOLS = {
    EMPTY: '.',
    TREE: '🌳',
    FIRE: '🔥',
    LAKE: '🌊',
    CLOUD: '☁️',
    THUNDER: '⚡',
}

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[EMPTY for _ in range(width)] for _ in range(height)]
        self.score = 0
        self.lives = 3
        self.helicopter_x = width // 2
        self.helicopter_y = height // 2
        self.water = 0
        self.max_water = 1

    def generate_map(self):
        # Генерация рек
        for _ in range(self.width // 10):
            x, y = self.random_empty_cell()
            for _ in range(random.randint(5, 10)):
                self.map[y][x] = LAKE
                x += random.choice([-1, 0, 1])
                y += random.choice([-1, 0, 1])
                x = max(0, min(x, self.width - 1))
                y = max(0, min(y, self.height - 1))

        # Генерация деревьев
        for _ in range(self.width * self.height // 20):
            x, y = self.random_empty_cell()
            self.map[y][x] = TREE

    def random_empty_cell(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.map[y][x] == EMPTY:
                return x, y

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if x == self.helicopter_x and y == self.helicopter_y:
                    print('🚁', end='')
                else:
                    print(SYMBOLS[self.map[y][x]], end='')
            print()
        print(f"Score: {self.score} | Lives: {self.lives} | Water: {self.water}/{self.max_water}")

    def move_helicopter(self, dx, dy):
        new_x = max(0, min(self.helicopter_x + dx, self.width - 1))
        new_y = max(0, min(self.helicopter_y + dy, self.height - 1))
        self.helicopter_x, self.helicopter_y = new_x, new_y

    def handle_input(self):
        key = input("Move (wasd), take water (f), extinguish fire (e), or quit (q): ").lower()
        if key == 'w':
            self.move_helicopter(0, -1)
        elif key == 's':
            self.move_helicopter(0, 1)
        elif key == 'a':
            self.move_helicopter(-1, 0)
        elif key == 'd':
            self.move_helicopter(1, 0)
        elif key == 'f':
            self.take_water()
        elif key == 'e':
            self.extinguish_fire()
        elif key == 'q':
            return False
        return True

    def take_water(self):
        if self.map[self.helicopter_y][self.helicopter_x] == LAKE and self.water < self.max_water:
            self.water += 1

    def extinguish_fire(self):
        if self.water > 0:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    x = self.helicopter_x + dx
                    y = self.helicopter_y + dy
                    if 0 <= x < self.width and 0 <= y < self.height:
                        if self.map[y][x] == FIRE:
                            self.map[y][x] = EMPTY
                            self.score += 1
                            self.water -= 1
                            return

    def spread_fire(self):
        new_fires = []
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == FIRE:
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.width and 0 <= ny < self.height:
                                if self.map[ny][nx] == TREE and random.random() < 0.1:
                                    new_fires.append((nx, ny))
        for x, y in new_fires:
            self.map[y][x] = FIRE

    def run(self):
        self.generate_map()
        while True:
            self.draw()
            if not self.handle_input():
                break
            self.spread_fire()
            if random.random() < 0.1:
                x, y = self.random_empty_cell()
                self.map[y][x] = FIRE
            time.sleep(0.1)

if __name__ == "__main__":
    game = Game(20, 10)
    game.run()