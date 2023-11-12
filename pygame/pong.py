import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

size = (700, 500)
ballSize = 15
paddleWidth = 15
paddleHeight = 100

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

xVal = 350
yVal = 250
xOffset = 5
yOffset = 5

yVal2 = 200
yVal3 = 200
lives = 5

font = pygame.font.SysFont(None, 30)
end = ""

def drawObjects():
    pygame.draw.rect(screen, white, (xVal, yVal, ballSize, ballSize))
    pygame.draw.rect(screen, white, (5, yVal2, paddleWidth, paddleHeight))
    pygame.draw.rect(screen, white, (680, yVal3, paddleWidth, paddleHeight))

def checkCollision():
    global xVal, yVal, xOffset, lives, end

    if xVal > 670 and yVal >= yVal3 and yVal <= yVal3 + paddleHeight:
        xOffset = -xOffset
    elif xVal < 20 and yVal >= yVal2 and yVal <= yVal2 + paddleHeight:
        xOffset = -xOffset

    if xVal > size[0] or xVal < 0:
        xVal, yVal = 350, 250
        lives -= 1

    if lives == -1:
        end = "GAME OVER"
        endMessage = font.render(end, True, white)
        screen.blit(endMessage, [271, 103])
        screen.blit(livesCount, [271, 130])
        pygame.display.flip()
        pygame.time.delay(1500)
        return True

    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(black)

    drawObjects()

    livesCount = font.render("Life Count: " + str(lives), True, white)
    endMessage = font.render(end, True, white)
    screen.blit(endMessage, [271, 103])
    screen.blit(livesCount, [271, 130])

    keys = pygame.key.get_pressed()
    yVal3 -= 5 if keys[pygame.K_UP] else 0
    yVal3 += 5 if keys[pygame.K_DOWN] else 0
    yVal2 += 5 if keys[pygame.K_s] else 0
    yVal2 -= 5 if keys[pygame.K_w] else 0

    yVal += yOffset
    xVal += xOffset

    if yVal < 0 or yVal > size[1] - ballSize:
        yOffset = -yOffset

    if checkCollision():
        break

    pygame.display.flip()
    clock.tick(60)
