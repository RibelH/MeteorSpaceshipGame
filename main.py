import pygame
pygame.init()


#Create Window
screen_w = 500
screen_h = 500

win = pygame.display.set_mode((screen_w,screen_h))

#Setting the Window Caption
pygame.display.set_caption("First Game")

#Player Position


#Player size
player = pygame.image.load("char/PurpleSpaceship3.png")


#Player speed/directional change



#OBJECT CLASSES

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.player = pygame.image.load("char/PurpleSpaceship3.png")

    def draw(self,win):
        win.blit(self.player, (self.x, self.y))

class projectile(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12

        self.vel = -8
        self.projectile = pygame.image.load("projectiles/Fireball.png")

    def draw(self, win):
        win.blit(self.projectile, (self.x, self.y))




def RedrawGameWindow():
    #ReDraw Background

    win.fill((0,0,0)) #win.blit(BG, (x, y) ) for image BG

    #Draw Player
    #pygame.draw.rect(win, (255,255,255), (x, y, width, height))
    ship.draw(win)

    for bullet in bullets:
        bullet.draw(win)

    #Updating Window
    pygame.display.update()


#Loop for Game
ship = player(300, 410, 64, 64)
shootLoop = 0
bullets = []
run = True
while run:
    #Delay for Loop
    pygame.time.delay(15)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    #Checking for events
    for event in pygame.event.get():

        #Quit event
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y > 0 and bullet.y < 500:
            bullet.y += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    #Gets the state of ALL keys on the keyboard
    keys = pygame.key.get_pressed()

    #Checking for Key inputs
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if len(bullets) < 100:
            bullets.append(projectile(round(ship.x + ship.width//2 - 6), round(ship.y + ship.height//4) ))
        shootLoop = 1

    if keys[pygame.K_LEFT]:
        #Checking for Left-Border
        if ship.x > 0:
            ship.x -= ship.vel
    if keys[pygame.K_RIGHT]:
        #Checking for Right-Border
        if ship.x < (screen_w - ship.width):
            ship.x += ship.vel
    if keys[pygame.K_DOWN]:
        #Checking for Bottom-Border
        if ship.y < (screen_h - ship.width):
            ship.y += ship.vel
    if keys[pygame.K_UP]:
        #Checking for Top-Border
        if ship.y > 0:
            ship.y -= ship.vel




    RedrawGameWindow()





pygame.quit()