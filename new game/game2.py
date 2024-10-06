import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Настройки игроков
player1_pos = [100, 300]
player2_pos = [600, 300]
player_size = 50
player1_HP = 3
player2_HP = 3

# Настройки снарядов
bullet_size = 5
bullet_speed = 10
player1_bullets = []
player2_bullets = []

# Основной игровой цикл
while player1_HP > 0 and player2_HP > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Стрельба для игрока 1
            if event.key == pygame.K_SPACE:
                player1_bullets.append([player1_pos[0] + player_size // 2, player1_pos[1]])
            # Стрельба для игрока 2
            if event.button == 1:  # Левый клик мыши
                player2_bullets.append([player2_pos[0], player2_pos[1] + player_size // 2])

    # Движение первого игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1_pos[0] > 0:
        player1_pos[0] -= 5
    if keys[pygame.K_d] and player1_pos[0] < SCREEN_WIDTH - player_size:
        player1_pos[0] += 5
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= 5
    if keys[pygame.K_s] and player1_pos[1] < SCREEN_HEIGHT - player_size:
        player1_pos[1] += 5

    # Движение второго игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player2_pos[0] > 0:
        player2_pos[0] -= 5
    if keys[pygame.K_RIGHT] and player2_pos[0] < SCREEN_WIDTH - player_size:
        player2_pos[0] += 5
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= 5
    if keys[pygame.K_DOWN] and player2_pos[1] < SCREEN_HEIGHT - player_size:
        player2_pos[1] += 5

    # Движение снарядов игрока 1
    for bullet in player1_bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            player1_bullets.remove(bullet)
            continue

    # Движение снарядов игрока 2
    for bullet in player2_bullets[:]:
        bullet[0] += bullet_speed
        if bullet[0] > SCREEN_WIDTH:
            player2_bullets.remove(bullet)
            continue

    # Проверка столкновений снарядов
    for bullet in player1_bullets[:]:
        if (bullet[0] >= player2_pos[0] and bullet[0] <= player2_pos[0] + player_size) and \
                (bullet[1] >= player2_pos[1] and bullet[1] <= player2_pos[1] + player_size):
            player1_bullets.remove(bullet)
            player2_HP -= 1

    for bullet in player2_bullets[:]:
        if (bullet[0] >= player1_pos[0] and bullet[0] <= player1_pos[0] + player_size) and \
                (bullet[1] >= player1_pos[1] and bullet[1] <= player1_pos[1] + player_size):
            player2_bullets.remove(bullet)
            player1_HP -= 1

    # Отрисовка всего
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (player1_pos[0], player1_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (player2_pos[0], player2_pos[1], player_size, player_size))

    for bullet in player1_bullets:
        pygame.draw.rect(screen, BLUE, (bullet[0], bullet[1], bullet_size, bullet_size))

    for bullet in player2_bullets:
        pygame.draw.rect(screen, BLUE, (bullet[0], bullet[1], bullet_size, bullet_size))

    # Отображение HP
    font = pygame.font.SysFont("Arial", 30)
    hp_text1 = font.render(f"Player 1 HP: {player1_HP}", True, (0, 0, 0))
    hp_text2 = font.render(f"Player 2 HP: {player2_HP}", True, (0, 0, 0))
    screen.blit(hp_text1, (10, 10))
    screen.blit(hp_text2, (10, 40))

    pygame.display.flip()
print("Game Over!")
if player1_HP <= 0:
    print("Player 2 Wins!")
else:
    print("Player 1 Wins!")
pygame.quit()