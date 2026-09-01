import random
import os
import time

WIDTH = 12
HEIGHT = 4

snake = [(0, 0)]
apple = '*'

apple_x = random.randint(0, WIDTH - 1)
apple_y = random.randint(0, HEIGHT - 1)

while True:

    # Clear the terminal
    os.system("cls")

    # Create empty scene
    scene = [
        [' ' for _ in range(WIDTH)]
        for _ in range(HEIGHT)
    ]

    # Draw snake
    for x, y in snake:
        scene[y][x] = '='

    # Draw apple
    scene[apple_y][apple_x] = apple

    # Display scene
    for row in scene:
        print(''.join(row))

    # Move snake
    head_x, head_y = snake[-1]

    if head_x < WIDTH - 1:
        head_x += 1
    else:
        head_x = 0
        head_y += 1

        if head_y >= HEIGHT:
            head_y = 0

    snake.append((head_x, head_y))

    # Eat apple
    if (head_x, head_y) == (apple_x, apple_y):
        apple_x = random.randint(0, WIDTH - 1)
        apple_y = random.randint(0, HEIGHT - 1)
    else:
        snake.pop(0)

    # Control refresh speed
    time.sleep(0.2)