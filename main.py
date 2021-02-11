import pygame
pygame.init()


#Create Window
screen_w = 500
screen_h = 500

win = pygame.display.set_mode((screen_w,screen_h))

#Setting the Window Caption
pygame.display.set_caption("First Game")

#Player Position
x = 50
y = 50

#Player size
player = pygame.image.load("char/PurpleSpaceShip2.png")
width = 16
height = 16

#Player speed/directional change
vel = 5


def RedrawGameWindow():
    #ReDraw Background

    win.fill((0,0,0)) #win.blit(BG, (x, y) ) for image BG

    #Draw Player
    #pygame.draw.rect(win, (255,255,255), (x, y, width, height))
    win.blit(player, (x,y))

    #Updating Window
    pygame.display.update()


#Loop for Game
run = True
while run:
    #Delay for Loop
    pygame.time.delay(15)

    #Checking for events
    for event in pygame.event.get():

        #Quit event
        if event.type == pygame.QUIT:
            run = False

    #Gets the state of ALL keys on the keyboard
    keys = pygame.key.get_pressed()

    #Checking for Key inputs
    if keys[pygame.K_LEFT]:
        #Checking for Left-Border
        if x > 0:
            x -= vel
    if keys[pygame.K_RIGHT]:
        #Checking for Right-Border
        if x < (screen_w - width):
            x += vel
    if keys[pygame.K_DOWN]:
        #Checking for Bottom-Border
        if y < (screen_h - width):
            y += vel
    if keys[pygame.K_UP]:
        #Checking for Top-Border
        if y > 0:
            y -= vel

    if keys[pygame.K_SPACE]:
        pass

    RedrawGameWindow()





pygame.quit()