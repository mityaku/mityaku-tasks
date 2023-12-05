import pygame
import random

pygame.init()

width, height = 800, 600
cell_size = 40
grid_width, grid_height = width // cell_size, height // cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PacMan")

white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

class Pacman:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.direction = (1, 0)

    def move(self, keys, grid):
        if keys[pygame.K_RIGHT]:
            self.direction = (1, 0)
        elif keys[pygame.K_LEFT]:
            self.direction = (-1, 0)
        elif keys[pygame.K_DOWN]:
            self.direction = (0, 1)
        elif keys[pygame.K_UP]:
            self.direction = (0, -1)

        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]

        if 0 <= new_x < grid_width and 0 <= new_y < grid_height and grid[new_y][new_x] != 1:
            self.x = new_x
            self.y = new_y

    def draw(self):
        pygame.draw.circle(screen, yellow, (int(self.x * cell_size + cell_size / 2), int(self.y * cell_size + cell_size / 2)), self.size // 2)


class Ghost:
    def __init__(self, size):
        self.size = size
        self.reset()

    def reset(self):
        self.x = random.randint(0, grid_width - 1)
        self.y = random.randint(0, grid_height - 1)

    def move_randomly(self, grid):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for direction in directions:
            new_x = self.x + direction[0]
            new_y = self.y + direction[1]

            if 0 <= new_x < grid_width and 0 <= new_y < grid_height and grid[new_y][new_x] != 1:
                self.x = new_x
                self.y = new_y
                break

    def draw(self):
        pygame.draw.rect(screen, green, (self.x * cell_size, self.y * cell_size, self.size, self.size))


class Dot:
    def __init__(self, size):
        self.size = size
        self.reset()

    def reset(self):
        self.x = random.randint(0, grid_width - 1)
        self.y = random.randint(0, grid_height - 1)

    def draw(self):
        pygame.draw.circle(screen, red, (int(self.x * cell_size + cell_size / 2), int(self.y * cell_size + cell_size / 2)), self.size // 2)

class Grid:
    def __init__(self):
        self.grid = [[0] * grid_width for _ in range(grid_height)]
        self.generate_walls()

    def generate_walls(self):
        walls = [[0,0], [0,1], [0,2], [0,0], [0,1], [0,2], [0,0], [0,1], [0,2], [0,0], [0,1], [0,2], [0,0], [0,1], [0,2], [0,0], [0,1], [0,2], [0,0], [0,1]]
        for i in range(50):
            randomMathList = [1, -1]
            radomMath = randomMathList[random.randint(0, 1)]
            wall_x = random.randint(0, grid_width - 1)
            wall_y = random.randint(0, grid_height - 1)
            self.grid[wall_y][wall_x] = 1
            

            

    def draw(self):
        for x in range(0, width, cell_size):
            pygame.draw.line(screen, (255, 0, 0), (x, 0), (x, height))
        for y in range(0, height, cell_size):
            pygame.draw.line(screen, (255, 0, 0), (0, y), (width, y))

        for y in range(grid_height):
            for x in range(grid_width):
                if self.grid[y][x] == 1:  
                    pygame.draw.rect(screen, (100, 100, 100), (x * cell_size, y * cell_size, cell_size, cell_size))

pacman = Pacman(grid_width // 2, grid_height // 2, cell_size, 1)
ghost = Ghost(cell_size)
dot = Dot(cell_size)
grid = Grid()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    pacman.move(keys, grid.grid)
    ghost.move_randomly(grid.grid)


    if pacman.x == dot.x and pacman.y == dot.y:
        dot.reset()

    if pacman.x == ghost.x and pacman.y == ghost.y:
        print("Game Over")
        running = False

    screen.fill(white)

    grid.draw()

    pacman.draw()
    ghost.draw()
    dot.draw()

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
