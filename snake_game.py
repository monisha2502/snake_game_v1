import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 10
font = pygame.font.SysFont(None, 30)

def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def main():
    snake = [(100, 100)]
    direction = (CELL_SIZE, 0)
    food = (
        random.randrange(0, WIDTH, CELL_SIZE),
        random.randrange(0, HEIGHT, CELL_SIZE)
    )
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN:
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT:
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT:
                    direction = (CELL_SIZE, 0)

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        if head == food:
            score += 1
            food = (
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            )
        else:
            snake.pop()

        if (
            head[0] < 0 or head[0] >= WIDTH
            or head[1] < 0 or head[1] >= HEIGHT
            or head in snake[1:]
        ):
            pygame.quit()
            sys.exit()

        screen.fill(BLACK)

        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
        draw_text(f"Score: {score}", WHITE, 10, 10)

        pygame.display.flip()
        clock.tick(FPS)

main()

