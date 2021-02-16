import pygame
from random import randint
pygame.init()


#TODO: Animations
#TODO: add MENU
#TODO: improve enemy spawning


#Create Window
screen_w = 500
screen_h = 500

win = pygame.display.set_mode((screen_w,screen_h))

#Setting the Window Caption
pygame.display.set_caption("First Game")
BG = (pygame.image.load("envi/SpaceBG.png").convert(),pygame.image.load("envi/SpaceBG2.png").convert_alpha())

#Player Position


#Player size



#Player speed/directional change



#OBJECT CLASSES

class Enemy(object):


    def __init__(self, x, y, width, height):
        self.meteor= [pygame.image.load("enemy/MeteoEnemy.png").convert_alpha(), pygame.image.load("enemy/MeteoEnemy2.png").convert_alpha(),
                      pygame.image.load("enemy/MeteoEnemy3.png").convert_alpha()]
        self.x = x
        self.y = y
        self.img_size = randint(0,2)
        self.vel = 4
        if self.img_size == 1:
            self.width = 64
            self.height = 64

        elif self.img_size ==2:
            self.width = 48
            self.height = 48

        else:
            self.width = 32
            self.height = 32


        self.hitbox = (self.x, self.y, self.width, self.height)
    def draw(self, win):
        win.blit(self.meteor[self.img_size], (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
    def move(self):
        pass
    def hit(self):
        global enemies, bullets, score
        enemies = [enemy for enemy in enemies if enemy not in enemies_removed]
        bullets = [bullet for bullet in bullets if bullet not in bullets_removed]
        score +=1





class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.player = pygame.image.load("char/PurpleSpaceship3.png").convert_alpha()
        self.hitbox = (self.x , self.y, width, height)

    def draw(self,win):
        win.blit(self.player, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class projectile(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12

        self.vel = -8
        self.projectile = pygame.image.load("projectiles/Fireball.png").convert_alpha()

    def draw(self, win):
        win.blit(self.projectile, (self.x, self.y))





def RedrawGameWindow():
    #ReDraw Background
    if BG_current == 1:
        win.blit(BG[1], (0, BG_y - screen_h))
        win.blit(BG[0], (0, BG_y) )
    else:
        win.blit(BG[1], (0, BG_y ))
        win.blit(BG[0], (0, BG_y- screen_h))
    text = font.render("SCORE: " + str(score), 1, (255,255,255))
    win.blit(text, (210, 10))

    #Draw Player
    #pygame.draw.rect(win, (255,255,255), (x, y, width, height))
    ship.draw(win)

    for enemy in enemies:
        enemy.draw(win)

    for bullet in bullets:
        bullet.draw(win)


    #Updating Window
    pygame.display.update()


#Loop for Game
BG_y = 0
font = pygame.font.SysFont("comicsans", 30, True, True)
enemies_removed = set()
bullets_removed = set()
enemies = []
ship = player(300, 410, 64, 64)
shootLoop = 0
meteoLoop = 0
bullets = []
run = True
score = 0
BG_current = 1
while run:

    #Checks for current number of enemies : 4 enemies is MAX
    if len(enemies) < 4 and meteoLoop == 0:
        enemies.append(Enemy(randint(50, 450), randint(50, 150), 64, 64))
        meteoLoop += 1
    #Delay for Shots
    pygame.time.delay(15)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    #Delay for Enemies
    if meteoLoop > 0:
        meteoLoop += 1
    if meteoLoop >20:
        meteoLoop = 0



    #Checking for events
    for event in pygame.event.get():

        #Quit event
        if event.type == pygame.QUIT:
            run = False

    #Checking for Projectile-Enemy Collision
    for bullet in bullets:
        for enemy in enemies:
            if bullet.y + 5  < enemy.hitbox[1] + enemy.height and bullet.y + bullet.height > enemy.hitbox[1]:
                if bullet.x - bullet.width < enemy.hitbox[0] + enemy.width and bullet.x + bullet.width > enemy.hitbox[0]:
                    enemies_removed.add(enemy)
                    bullets_removed.add(bullet)
                    enemy.hit()

        #Bullet Travelanimation and tracking
        if bullet.y > 0 and bullet.y < 500:
            bullet.y += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))


    #Gets the state of ALL keys on the keyboard
    keys = pygame.key.get_pressed()

    #Checking for Key inputs
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if len(bullets) < 100:
            bullets.append(projectile(round(ship.x + ship.width//2 - 6), round(ship.y + ship.height//4)))
            #bullets.append(projectile(round(ship.x + ship.width//2 + 6), round(ship.y + ship.height//4) ))
            #bullets.append(projectile(round(ship.x + ship.width//2 - 12), round(ship.y + ship.height//4)))
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

    #Scrolling BackgroundLoop
    if BG_y < 500:
        BG_y += 1
    else:
        if BG_current == 1:
            BG_current = 2
            BG_y = 0
        else:
            BG_current = 1
            BG_y = 0


    RedrawGameWindow()








pygame.quit()