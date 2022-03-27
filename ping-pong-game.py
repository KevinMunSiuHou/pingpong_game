from pygame import *
from random import randint

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

back = (200, 255, 255)

#Superclass
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height, color):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
        self.image.set_colorkey(color)
        self.rect =  self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    #Control funtion
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    

white = (255, 255, 255)
pad_1 = Player('C:\\Users\\hp\\Desktop\\Ping-Pong\\Pad 1.png',30,200,4,50,150,white)
pad_2 = Player('C:\\Users\\hp\\Desktop\\Ping-Pong\\Pad 2.png',520,200,4,50,150,white)
ball = GameSprite('C:\\Users\\hp\\Desktop\\Ping-Pong\\ball.png',200,200,4,50,50,white)

game = True
finish = False

speed_x = 3
speed_y = 3

clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 5)
lose1 = font.render('Player 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('Player 2 LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        pad_1.update_left()
        pad_2.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        #reaction (ball)
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        
        if sprite.collide_rect(pad_1, ball) or sprite.collide_rect(pad_2, ball):
            speed_x *= -1
            speed_y *= 1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x > win_width - 50:
            finish = True
            window.blit(lose2, (200,200))
            
        pad_1.reset()
        pad_2.reset()
        ball.reset()
    
    display.update()
    clock.tick(FPS)