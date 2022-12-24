import pygame
import random


class Player(pygame.sprite.Sprite):

    def __init__(self, gs=None):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("images/spaceU.png"), pygame.image.load("images/spaceD.png") , pygame.image.load("images/spaceR.png"), pygame.image.load("images/spaceL.png")]
        self.current_image = pygame.transform.scale(self.images[0], (50, 50))
        self.rect = self.current_image.get_rect()

        self.direction =0

    def swap(self, direction):
        if direction ==0 and self.direction!= 0:
            self.current_image= pygame.transform.scale(self.images[0], (50, 50))
            self.direction = direction

        if direction ==1 and self.direction!= 1:
            self.current_image= pygame.transform.scale(self.images[1], (50, 50))
            self.direction = direction

        if direction ==2 and self.direction!= 2:
            self.current_image= pygame.transform.scale(self.images[2], (50, 50))
            self.direction = direction

        if direction ==3 and self.direction!= 3:
            self.current_image= pygame.transform.scale(self.images[3], (50, 50))
            self.direction = direction


pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Navezinha")

bg = pygame.image.load('images/bg2.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))


pos_player_x = 200
pos_player_y = 300

play = True
player = Player()

player_rect = player.current_image.get_rect()


while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    screen.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))  # background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 1
        player.swap(direction=0)
       

    if key[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 1
        player.swap(direction=1)

    if key[pygame.K_RIGHT] and pos_player_y < 665:
        pos_player_x += 1
        player.swap(direction=2)

    if key[pygame.K_LEFT] and pos_player_y < 665:
        pos_player_x -= 1
        player.swap(direction=3)

 

    player_rect.y= pos_player_y
    player_rect.x= pos_player_x

    x -= 0.5

    pygame.draw.rect(screen,(255,0,0), player_rect,4)
 
    screen.blit(player.current_image, (pos_player_x, pos_player_y))

    pygame.display.update()
