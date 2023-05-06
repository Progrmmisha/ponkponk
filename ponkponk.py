from pygame import*
from random import randint
window = display.set_mode((700, 550))
display.set_caption('ponkping')
color = 0, 0, 255
v_x = 3
v_y = 3
player1_score = 0
player2_score = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, s_x, s_y):
        super().__init__()
        self.s_x = s_x
        self.s_y = s_y
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (s_x, s_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, image, speed, x, y, s_x, s_y, tp):
        super().__init__(image, speed, x, y, s_x, s_y)
        self.tp = tp
    def moving(self):
        if self.tp == 1:
            keys_pressed = key.get_pressed()
            if keys_pressed[K_w] and self.rect.y > 75:
                self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y < 455:
                self.rect.y += self.speed
        if self.tp == 2:
            keys_pressed = key.get_pressed()
            if keys_pressed[K_UP] and self.rect.y > 75:
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN] and self.rect.y < 455:
                self.rect.y += self.speed
    def restart(self):
        if self.tp == 1:
            self.rect.x = 10
        if self.tp == 2:
            self.rect.x = 665
class Ball(GameSprite):
    def __init__(self, image, speed, x, y, s_x, s_y):
        super().__init__(image, speed, x, y, s_x, s_y)
    def update(self, vect_x, vect_y):
        self.rect.x += vect_x
        self.rect.y += vect_y
    def start(self, p1_s, p2_s, win):
        if p1_s > p2_s:
            self.rect.x = 600
            self.rect.y = 300
        if p1_s < p2_s:
            self.rect.x = 50
            self.rect.y = 300
        if p1_s == p2_s:
            if win == 1:
                self.rect.x = 600
                self.rect.y = 300
            if win == 2:
                self.rect.x = 600
                self.rect.y = 50
player1 = Player('player1.png', 5, 10, 300, 25, 100, 1)
player2 = Player('player2.png', 5, 665, 300, 25, 100, 2)
ball = Ball('ball.png', 5, 50, 300, 50, 50)
py = True
clock = time.Clock()
while py: 
    window.fill((color))
    player1.moving()
    player2.moving()
    player1.reset()
    player2.reset()
    ball.update(v_x, v_y)
    ball.reset()
    if ball.rect.y < 75:
        v_y *= -1
    if ball.rect.y > 500:
        v_y *= -1
    if sprite.collide_rect(player1, ball):
        v_x *= -1
    if sprite.collide_rect(player2, ball):
        v_x *= -1
    if ball.rect.x < 0:
        player2_score += 1
        ball.start(player1_score, player2_score, 2)
        player1.rect.x = 10
        player2.rect.x = 665
    if ball.rect.x > 700:
        player1_score += 1
        ball.start(player1_score, player2_score, 1)
        player1.rect.x = 10
        player2.rect.x = 665
    if player1_score > player2_score:
        color = 0, 0, 128
    if player1_score < player2_score:
        color = 128, 0, 0
    if player1_score == player2_score:
        color = 255, 255, 255
    display.update()
    clock.tick(60)
    for i in event.get():
            if i.type == QUIT:
                py = False  