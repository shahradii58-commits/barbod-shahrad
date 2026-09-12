import pygame

pygame.init()


WIDTH = 600
HEIGHT = 400

screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake game")

clock = pygame.time.Clock()

snake_x = 300
snake_y = 200
speed = 5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= speed

    if keys[pygame.K_RIGHT]:
        snake_x += speed

    if keys[pygame.K_UP]:
        snake_y -= speed

    if keys[pygame.K_DOWN]:
        snake_y += speed

    screen.fill ((0, 0, 0))

    pygame.draw.rect(screen,(0, 255, 0),(snake_x, snake_y, 20, 20))

    pygame.display.update()

    clock.tick(60)

pygame.quit()