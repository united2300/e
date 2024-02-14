import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Azur Lane Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ship class
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.width = 50
        self.height = 30
        self.color = color
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.health = 100

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ships = pygame.sprite.Group()

    def add_ship(self, ship):
        self.ships.add(ship)

    def draw(self, screen):
        self.ships.draw(screen)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, color, speed):
        super().__init__()
        self.width = 50
        self.height = 30
        self.color = color
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.health = 100
        self.speed = speed

    def move(self):
        self.rect.x += self.speed
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed = -self.speed
            self.rect.y += 30  # Move down after changing direction

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# Main function
def main():
    # Initialize
    player = Player()
    enemy = Enemy(random.randint(50, SCREEN_WIDTH - 50), 50, RED, 3)
    player_ship = Ship(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 50, BLUE)
    player.add_ship(player_ship)

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_ship.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            player_ship.move(5, 0)

        # Drawing
        player.draw(screen)
        enemy.draw(screen)

        # Enemy movement
        enemy.move()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
