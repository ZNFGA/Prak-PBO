import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Kelas Paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

# Kelas Ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect()
        self.reset()
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

    def reset(self):
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x = 4 * random.choice([-1, 1])
        self.speed_y = 4 * random.choice([-1, 1])

# Kelas Game
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.paddles = pygame.sprite.Group()
        self.ball = Ball()
        self.player1 = Paddle(20, SCREEN_HEIGHT // 2 - 50)
        self.player2 = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - 50)
        self.all_sprites.add(self.ball, self.player1, self.player2)
        self.paddles.add(self.player1, self.player2)
        
        # Load background image
        self.background = pygame.image.load("C:/Users/HP/Desktop/pbo/Prak-PBO/Prak-5/kim junggo.jpg")

        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player1.move_up()
            if keys[pygame.K_s]:
                self.player1.move_down()
            if keys[pygame.K_UP]:
                self.player2.move_up()
            if keys[pygame.K_DOWN]:
                self.player2.move_down()

            self.ball.update()

            # Check collisions
            if pygame.sprite.spritecollide(self.ball, self.paddles, False):
                self.ball.speed_x *= -1

            # Check if the ball went out of bounds (goal)
            if self.ball.rect.left <= 0 or self.ball.rect.right >= SCREEN_WIDTH:
                self.ball.reset()

            # Draw background
            self.screen.blit(self.background, (0, 0))
            
            # Draw sprites
            self.all_sprites.draw(self.screen)
            
            # Update display
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
