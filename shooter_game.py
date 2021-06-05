
#Создай собственный Шутер!

from pygame import *
from random import *
monsters = sprite.Group()
bullets = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class UFO(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15)
        bullets.add(bullet)
roceta = UFO('rocket.png', 350, 600, 30)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.rect.x = randint(80, 620)
            self.rect.y = 0
for i in range(10):
    eneme_1_Ufo = Enemy('ufo.png', randint(200, 600), 0, 10)
    monsters.add(eneme_1_Ufo)
for i in range(3):
    eneme_2_asteroid = Enemy('asteroid.png', randint(300, 600), 0, 20)
    monsters.add(eneme_2_asteroid)
for i in range(6):
    eneme_2_Ufo = Enemy('678243768324678.jpg',randint(100, 600), 0, 15)
    monsters.add(eneme_2_Ufo)



class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0: 
            self.kill()
font.init()
font = font.SysFont('Arial', 40)



window = display.set_mode((1000, 700))
display.set_caption("v_1.0")
background = transform.scale(image.load("galaxy.jpg"), (1000, 700))
mixer.init()
mixer.music.load('F-7_-_Sonic_Blaster_b128f0d182.mp3')
mixer.music.play()
clock = time.Clock()
FPS = 30


game = True
while game:
    window.blit(background,(0, 0))
    keys = key.get_pressed()
    for A in event.get():
        if A.type == QUIT:
            game = False
        if keys[K_SPACE]:
            roceta.fire()
    if sprite.groupcollide(monsters, bullets, True, True):
        kill = font.render('KILL! +1G', True, (225, 215, 0))
    roceta.reset()
    roceta.update()
    bullets.update()
    bullets.draw(window)
    monsters.draw(window)
    monsters.update()
    display.update()
    time.delay(50)