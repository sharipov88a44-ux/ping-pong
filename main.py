from pygame import *
        
window = display.set_mode((500, 700))

window.fill((0,0,0))
             
display.set_caption('')
clock = time.Clock()

mixer.init()

FPS = 60
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
            
    display.update()
    clock.tick(FPS)