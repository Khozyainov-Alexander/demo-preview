import pygame
import random

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
PLAYER1_COLOR = (0, 0, 255)
PLAYER2_COLOR = (255, 0, 0)
BULLET_COLOR = (0, 0, 0)  # Чёрный цвет пуль

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Корабли - ПВП")
clock = pygame.time.Clock()


class Player:
    def __init__(self, color, controls):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50), 50, 50)
        self.color = color
        self.health = 3
        self.direction = (0, 0)  # Направление движения

    def move(self, controls):
        keys = pygame.key.get_pressed()
        self.direction = (0, 0)  # Сбросить направление
        if keys[controls['up']]:
            self.rect.y -= 5
            self.direction = (0, -1)
        if keys[controls['down']]:
            self.rect.y += 5
            self.direction = (0, 1)
        if keys[controls['left']]:
            self.rect.x -= 5
            self.direction = (-1, 0)
        if keys[controls['right']]:
            self.rect.x += 5
            self.direction = (1, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def draw_health(self, surface):
        font = pygame.font.Font(None, 36)
        health_text = font.render(str(self.health), True, (0, 0, 0))
        surface.blit(health_text, (self.rect.centerx - 10, self.rect.top - 30))


class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, 5, 5)
        self.direction = direction

    def move(self):
        self.rect.x += self.direction[0] * 10  # Умножаем направление на скорость
        self.rect.y += self.direction[1] * 10  # Умножаем направление на скорость

    def draw(self, surface):
        pygame.draw.rect(surface, BULLET_COLOR, self.rect)


def main():
    running = True
    player1 = Player(PLAYER1_COLOR, {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d})
    player2 = Player(PLAYER2_COLOR,
                     {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT})
    bullets1 = []
    bullets2 = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player1.direction != (0, 0):  # Проверка на движение
                    # Создать пулю с направлением игрока 1
                    bullets1.append(Bullet(player1.rect.centerx, player1.rect.top, player1.direction))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and player2.direction != (0, 0):  # Проверка на движение
                    # Создать пулю с направлением игрока 2
                    bullets2.append(Bullet(player2.rect.centerx, player2.rect.bottom, player2.direction))

        player1.move({'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d})
        player2.move({'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT})

        # Обработка пуль игрока 1
        for bullet in bullets1[:]:  # Используем копию списка для безопасного удаления
            bullet.move()
            if bullet.rect.colliderect(player2.rect):
                player2.health -= 1
                bullets1.remove(bullet)

                # Обработка пуль игрока 2
            for bullet in bullets2[:]:  # Используем копию списка для безопасного удаления
                bullet.move()
                if bullet.rect.colliderect(player1.rect):
                    player1.health -= 1
                    bullets2.remove(bullet)

            screen.fill(WHITE)
            player1.draw(screen)
            player2.draw(screen)
            player1.draw_health(screen)  # Отображение здоровья игрока 1
            player2.draw_health(screen)  # Отображение здоровья игрока 2
            for bullet in bullets1:
                bullet.draw(screen)
            for bullet in bullets2:
                bullet.draw(screen)

            if player1.health <= 0:
                print("Игрок 2 победил!")
                running = False
            if player2.health <= 0:
                print("Игрок 1 победил!")
                running = False

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

    if __name__ == "__main__":
        main()
