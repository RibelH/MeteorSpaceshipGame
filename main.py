import pygame
pygame.init()


#Create Window
win = pygame.display.set_mode((500,500))

#Setting the Window Caption
pygame.display.set_caption("First Game")

#Player Position
x = 50
y = 50

#Player size
width = 40
height = 40

#Player speed/directional change
vel = 5

#Loop for Game
run = True
while run:
    #Delay for Loop
    pygame.time.delay(10)

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
        if x < (500 - width):
            x += vel
    if keys[pygame.K_DOWN]:
        #Checking for Bottom-Border
        if y < (500 - width):
            y += vel
    if keys[pygame.K_UP]:
        #Checking for Top-Border
        if y > 0:
            y -= vel

    if keys[pygame.K_SPACE]:
        pass

    #ReDraw Background
    win.fill((0,0,0))

    #Draw Player
    pygame.draw.rect(win, (255,255,255), (x, y, width, height))

    #Updating Window
    pygame.display.update()




pygame.quit()