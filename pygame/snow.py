import pygame
import random

pygame.init()

width, height = 700, 500
window_size = (width, height)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snow")

class Snow(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length):
        super().__init__()
        self.width = s_width
        self.length = s_length
        self.speed = random.randrange(1, 3)
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)
        self.horizontal_speed = random.randrange(-2, 2)

    def update(self):
        self.rect.move_ip(self.horizontal_speed, self.speed)
        if self.rect.y > height or (self.rect.x < 0 and self.rect.y > height) or (self.rect.x > width and self.rect.y > height):
            self.rect.y = -50
            self.speed = random.randrange(1, 3)
            self.rect.x = random.randrange(width)

clock = pygame.time.Clock()
snowList = pygame.sprite.Group()

numberOfFlakes = 600
for _ in range(numberOfFlakes):
    size = random.randrange(2, 5)
    snowflake = Snow(size, size)
    snowList.add(snowflake)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(blue)
    
    snowList.update()
    snowList.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
