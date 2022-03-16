import pygame
import random
import math
 
WIDTH = 480
HEIGHT = 600
FPS = 60
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("move")
clock = pygame.time.Clock()
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.angle = 90
 
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_z]:
            player.angle -= 1
        if keystate[pygame.K_x]:
            player.angle += 1
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
 
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.angle)
        all_sprites.add(bullet)
        bullets.add(bullet)
 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.angle = (angle * math.pi) / 180
        self.speedy = -10
 
    def update(self):
        self.rect.y += self.speedy * math.sin(self.angle)
        self.rect.x += self.speedy * math.cos(self.angle)
 
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
 
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
 
# Game loop
running = True
while running:
    clock.tick(FPS)
 
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                
    all_sprites.update()
 
    screen.fill(BLACK)
    all_sprites.draw(screen)
 
    pygame.display.flip()
 
pygame.quit()