import pygame
pygame.init()
print("hallo")
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
x=100
y=100
change_x=0
change_y=0
bg=pygame.display.set_mode((800,600))
pygame.display.set_caption("motion of object")
pygame.display.update()
game_over =False
while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                change_x=0.5
            if event.key==pygame.K_RIGHT:
                change_x=-0.5
            if event.key==pygame.K_UP:
                change_y=0.5
            if event.key==pygame.K_DOWN:
                change_y=-0.5
    bg.fill(black)

    x=x-change_x
    y=y-change_y

    myrec=pygame.draw.rect(bg,green,[x,y,50,50])
    pygame.display.update()