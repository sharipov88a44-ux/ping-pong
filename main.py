from pygame import *

SKY_BLUE = (117, 187, 253)

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
    pass

window = display.set_mode((700, 600))
window.fill(SKY_BLUE)       
display.set_caption('ping-pong')
clock = time.Clock()

racket1 = Player('platform.png', 5, 300, 100, 20, 3)
racket2 = Player('platform.png', 675, 300, 100, 20, 3)
ball = GameSprite('ball.webp', 350, 300, 65, 65, 3)

mixer.init()

FPS = 60
game = True
while game:
    racket1.reset()
    racket2.reset()
    ball.reset()
        
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    display.update()
    clock.tick(FPS)