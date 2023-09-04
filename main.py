import pygame

pygame.init()
screen = pygame.display.set_mode((10, 600))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():  #this means its running yo
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white") #ho ho ho merru chritysalma


    pygame.display.flip()

    clock.tick(60)

pygame.quit()