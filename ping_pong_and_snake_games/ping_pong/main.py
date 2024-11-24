

import os
import pygame
import sys
os.environ["SDL_AUDIODRIVER"] = "dummy"
# Инициализация Pygame
pygame.init()
print("Pygame initialized")
print(f"SDL_AUDIODRIVER={os.environ.get('SDL_AUDIODRIVER')}")
# Константы
WIDTH, HEIGHT = 800, 400
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
FPS = 60

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Шрифт
font = pygame.font.SysFont('Arial', 24)

# Мяч
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed = [3, 3]

# Ракетки
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
computer = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player_speed = 0
computer_speed = 3

# Счёт
player_score, computer_score = 0, 0

# Часы
clock = pygame.time.Clock()

# Основной цикл игры
running = True
while running:
    screen.fill(BLACK)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(0, 0, WIDTH, HEIGHT), 3)

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -5
            if event.key == pygame.K_DOWN:
                player_speed = 5
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                player_speed = 0

    # Движение ракетки игрока
    player.y += player_speed
    player.y = max(0, min(HEIGHT - PADDLE_HEIGHT, player.y))

    # Движение компьютера
    if ball.centery > computer.centery:
        computer.y += computer_speed
    if ball.centery < computer.centery:
        computer.y -= computer_speed
    computer.y = max(0, min(HEIGHT - PADDLE_HEIGHT, computer.y))

    # Движение мяча
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Отражение от стен
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Отражение от ракеток
    if ball.colliderect(player) or ball.colliderect(computer):
        ball_speed[0] = -ball_speed[0]

    # Счёт
    if ball.left <= 0:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed = [3, 3]
    if ball.right >= WIDTH:
        computer_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed = [-3, -3]

    # Отрисовка элементов
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, computer)
    pygame.draw.ellipse(screen, GREEN, ball)

    # Счёт
    player_text = font.render(f"Player: {player_score}", True, GREEN)
    computer_text = font.render(f"Computer: {computer_score}", True, RED)
    screen.blit(player_text, (WIDTH - 150, 10))
    screen.blit(computer_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
