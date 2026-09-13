import pygame
import random

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# رنگ‌ها
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# اندازه هر قسمت مار
SIZE = 20

# مار
snake = [
    [300, 200],
    [280, 200],
    [260, 200]
]

direction = "RIGHT"

# غذا
food_x = random.randrange(0, WIDTH, SIZE)
food_y = random.randrange(0, HEIGHT, SIZE)

score = 0

# فونت
font = pygame.font.Font(None, 36)

running = True
game_over = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

            # شروع دوباره
            if event.key == pygame.K_SPACE and game_over:
                snake = [
                    [300, 200],
                    [280, 200],
                    [260, 200]
                ]

                direction = "RIGHT"
                score = 0

                food_x = random.randrange(0, WIDTH, SIZE)
                food_y = random.randrange(0, HEIGHT, SIZE)

                game_over = False

    if not game_over:

        # حرکت سر مار
        head_x = snake[0][0]
        head_y = snake[0][1]

        if direction == "LEFT":
            head_x -= SIZE

        if direction == "RIGHT":
            head_x += SIZE

        if direction == "UP":
            head_y -= SIZE

        if direction == "DOWN":
            head_y += SIZE

        new_head = [head_x, head_y]

        snake.insert(0, new_head)

        # خوردن غذا
        if head_x == food_x and head_y == food_y:
            score += 1

            food_x = random.randrange(0, WIDTH, SIZE)
            food_y = random.randrange(0, HEIGHT, SIZE)

        else:
            snake.pop()

        # برخورد با دیوار
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        ):
            game_over = True

        # برخورد مار با خودش
        if new_head in snake[1:]:
            game_over = True

    # پس‌زمینه
    screen.fill(BLACK)

    # رسم مار
    for part in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (part[0], part[1], SIZE, SIZE)
        )

    # رسم غذا
    pygame.draw.rect(
        screen,
        RED,
        (food_x, food_y, SIZE, SIZE)
    )

    # نمایش امتیاز
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    # Game Over
    if game_over:
        game_over_text = font.render(
            "GAME OVER - Press SPACE",
            True,
            WHITE
        )

        screen.blit(
            game_over_text,
            (170, 180)
        )

    pygame.display.update()

    clock.tick(10)

pygame.quit()