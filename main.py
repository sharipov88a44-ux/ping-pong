from pygame import *

SKY_BLUE = (117, 187, 253)
INDIGO = (50, 18, 122)

WIN_WIDTH = 700
WIN_HEIGHT = 600

class GameSprite(sprite.Sprite):
    def __init__(self, imagePath, corX, corY, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.rotate(transform.scale(image.load(imagePath), (width, height)), 90)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = corX
        self.rect.y = corY
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def move_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
            
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
window.fill(SKY_BLUE) 
display.set_caption('ping-pong')
clock = time.Clock()
font.init()

racket1 = Player('platform.png', 5, 300, 100, 20, 4)
racket2 = Player('platform.png', 675, 300, 100, 20, 4)
ball = GameSprite('tenis_ball.png', 300, 300, 65, 65, 3)

win1 = font.SysFont('Comic Sans MS', 60).render('Игрок справа победил!', 1, INDIGO)
win2 = font.SysFont('Comic Sans MS', 60).render('Игрок слева победил!', 1, INDIGO)

d_x = 3
d_y = 3

FPS = 60
game = True
finish = False
while game:
    window.fill(SKY_BLUE) 
    
    racket1.reset()
    racket2.reset()
    ball.reset()
    racket1.move_r()
    racket2.move_l()
    
    if ball.rect.x < -ball.rect.width:
        window.blit(win1, (10, 10))
        
    if ball.rect.x >= WIN_WIDTH + ball.rect.width:
        window.blit(win2, (10, 10))
     
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    ball.rect.x += d_x
    ball.rect.y += d_y
    if ball.rect.y > WIN_HEIGHT - ball.rect.width:
        d_y *= -1
    if ball.rect.y < 0:
        d_y *= -1
        
    if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
        d_x *= -1
    
            
    display.update()
    clock.tick(FPS)