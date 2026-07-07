import pygame
import random
import math

# ============================================================
#  初始化
# ============================================================
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
FPS = 60

FONT_SMALL = pygame.font.Font(None, 30)
FONT_LARGE = pygame.font.Font(None, 40)

# ============================================================
#  加载素材
# ============================================================
IMG_DIR = r"D:\补课资料\Introduction-to-Computer-Science\20260704\space_invaders\img"

bg = pygame.image.load(f"{IMG_DIR}/bg.png")
ship_img = pygame.image.load(f"{IMG_DIR}/spaceship.png")
bullet_img = pygame.image.load(f"{IMG_DIR}/bullet.png")
alien_bullet_img = pygame.image.load(f"{IMG_DIR}/alien_bullet.png")
alien_imgs = [pygame.image.load(f"{IMG_DIR}/alien{i}.png") for i in range(1, 6)]
explosion_imgs = [pygame.image.load(f"{IMG_DIR}/exp{i}.png") for i in range(1, 6)]

laser_snd = pygame.mixer.Sound(f"{IMG_DIR}/laser.wav")
explosion_snd = pygame.mixer.Sound(f"{IMG_DIR}/explosion.wav")
explosion2_snd = pygame.mixer.Sound(f"{IMG_DIR}/explosion2.wav")
laser_snd.set_volume(0.25)
explosion_snd.set_volume(0.25)
explosion2_snd.set_volume(0.25)

# ============================================================
#  玩家飞船
# ============================================================
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = ship_img
        self.image = ship_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 8
        self.angle = 0
        self.max_health = 3
        self.health = self.max_health
        self.shoot_cooldown = 500
        self.last_shot = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.rect.top > 0:
            self.rect.y -= self.speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_q]:
            self.angle += 5
        if keys[pygame.K_e]:
            self.angle -= 5

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

        now = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and now - self.last_shot > self.shoot_cooldown:
            laser_snd.play()
            rad = math.radians(self.angle)
            bullet = Bullet(self.rect.centerx, self.rect.top, rad)
            all_sprites.add(bullet)
            player_bullets.add(bullet)
            self.last_shot = now

        # 血条
        bar_w = self.rect.width
        bar_h = 15
        bar_y = self.rect.bottom + 10
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, bar_y, bar_w, bar_h))
        if self.health > 0:
            green_w = int(bar_w * (self.health / self.max_health))
            pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, bar_y, green_w, bar_h))

        if self.health <= 0:
            Explosion(self.rect.center, "big")
            self.kill()

# ============================================================
#  玩家子弹
# ============================================================
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle=0):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.vx = math.sin(angle) * self.speed
        self.vy = -math.cos(angle) * self.speed

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
            return
        hit = pygame.sprite.spritecollide(self, aliens, True)
        if hit:
            explosion_snd.play()
            Explosion(self.rect.center, "medium")
            self.kill()

# ============================================================
#  外星人
# ============================================================
class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = random.choice(alien_imgs)
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = 1
        self.counter = 0

    def update(self):
        self.rect.x += self.direction
        self.counter += 1
        if self.counter > 75:
            self.direction *= -1
            self.counter = 0

# ============================================================
#  外星人子弹
# ============================================================
class AlienBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = alien_bullet_img
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += 2
        if self.rect.top > HEIGHT:
            self.kill()
            return
        if pygame.sprite.spritecollide(self, ship_group, False, pygame.sprite.collide_mask):
            explosion2_snd.play()
            ship.health -= 1
            Explosion(self.rect.center, "small")
            self.kill()

# ============================================================
#  爆炸动画
# ============================================================
class Explosion(pygame.sprite.Sprite):
    SIZES = {"small": (20, 20), "medium": (40, 40), "big": (160, 160)}

    def __init__(self, center, size):
        super().__init__()
        w, h = self.SIZES.get(size, (40, 40))
        self.frames = [pygame.transform.scale(img, (w, h)) for img in explosion_imgs]
        self.index = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=center)
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer % 3 == 0 and self.index < len(self.frames) - 1:
            self.index += 1
            self.image = self.frames[self.index]
        if self.index >= len(self.frames) - 1:
            self.kill()

# ============================================================
#  精灵组
# ============================================================
all_sprites = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
aliens = pygame.sprite.Group()
alien_bullets = pygame.sprite.Group()
explosions = pygame.sprite.Group()
ship_group = pygame.sprite.Group()

ship = Ship()
ship_group.add(ship)
all_sprites.add(ship)

for row in range(5):
    for col in range(5):
        x = 100 + col * 100
        y = 100 + row * 70
        alien = Alien(x, y)
        aliens.add(alien)
        all_sprites.add(alien)

# ============================================================
#  游戏变量
# ============================================================
countdown = 3
last_count = pygame.time.get_ticks()
alien_shot_cooldown = 1000
last_alien_shot = 0
game_over = 0

# ============================================================
#  辅助函数
# ============================================================
def draw_text(text, font, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

# ============================================================
#  主循环
# ============================================================
running = True
while running:
    clock.tick(FPS)
    screen.blit(bg, (0, 0))

    if countdown > 0:
        draw_text("GET READY!", FONT_LARGE, WIDTH // 2 - 110, HEIGHT // 2 + 50)
        draw_text(str(countdown), FONT_LARGE, WIDTH // 2 - 10, HEIGHT // 2 + 100)
        now = pygame.time.get_ticks()
        if now - last_count > 1000:
            countdown -= 1
            last_count = now
    else:
        now = pygame.time.get_ticks()
        if (now - last_alien_shot > alien_shot_cooldown
                and len(alien_bullets) < 5
                and len(aliens) > 0):
            shooter = random.choice(aliens.sprites())
            ab = AlienBullet(shooter.rect.centerx, shooter.rect.bottom)
            alien_bullets.add(ab)
            all_sprites.add(ab)
            last_alien_shot = now

        if len(aliens) == 0:
            game_over = 1
        elif ship.health <= 0:
            game_over = -1

        if game_over == 0:
            ship_group.update()
            player_bullets.update()
            aliens.update()
            alien_bullets.update()
        else:
            if game_over == 1:
                draw_text("YOU WIN!", FONT_LARGE, WIDTH // 2 - 100, HEIGHT // 2 + 50)
            elif game_over == -1:
                draw_text("GAME OVER!", FONT_LARGE, WIDTH // 2 - 100, HEIGHT // 2 + 50)

    explosions.update()

    ship_group.draw(screen)
    player_bullets.draw(screen)
    aliens.draw(screen)
    alien_bullets.draw(screen)
    explosions.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
