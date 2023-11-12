import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
HOUSE_WIDTH, HOUSE_HEIGHT = 200, 200
SUN_RADIUS = 40
BG_COLOR = (135, 206, 250)
HOUSE_COLOR = (255, 0, 0)
SUN_COLOR = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Sun and House")

sun_x = 100
sun_y = 100

clock = pygame.time.Clock()

running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    sun_x = WIDTH // 2 + 200 * math.cos(angle)
    sun_y = HEIGHT // 2 - 100 * math.sin(angle)

    pygame.draw.circle(screen, SUN_COLOR, (int(sun_x), int(sun_y)), SUN_RADIUS)

    pygame.draw.rect(screen, HOUSE_COLOR, (300, 400, HOUSE_WIDTH, HOUSE_HEIGHT))
    pygame.draw.polygon(screen, HOUSE_COLOR, [(300, 400), (500, 400), (400, 300)])

    pygame.display.flip()

    angle += 0.01

    clock.tick(60)

pygame.quit()
