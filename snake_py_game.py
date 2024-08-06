import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 1280, 720
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)

# Colors
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Clock
clock = pygame.time.Clock()
snake_block = 20
initial_snake_speed = 10
speed_increase = 2
snake_speed = initial_snake_speed

font_style = pygame.font.SysFont(None, 50)

def gameLoop():
    global snake_speed  # Use global to modify the snake_speed variable
    game_over = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True

        for segment in snake_List:
            pygame.draw.rect(screen, red, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            snake_speed += speed_increase  # Increase speed

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
