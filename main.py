import sys

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
BG = (pygame.image.load("envi/SpaceBG.png").convert_alpha(),
      pygame.image.load("envi/SpaceBG2.png").convert_alpha())

Hearts = (pygame.image.load("hud/Hearts0.png").convert_alpha(),
          pygame.image.load("hud/Hearts1.png").convert_alpha(),
          pygame.image.load("hud/Hearts2.png").convert_alpha(),
          pygame.image.load("hud/Hearts3.png").convert_alpha() )
mainClock = pygame.time.Clock()




#OBJECT CLASSES

class Enemy(object):


    def __init__(self, x, y):
        self.meteor= [pygame.image.load("enemy/MeteoEnemy.png").convert_alpha(),
                      pygame.image.load("enemy/MeteoEnemy2.png").convert_alpha(),
                      pygame.image.load("enemy/MeteoEnemy3.png").convert_alpha()]
        self.x = x
        self.y = y
        self.img_size = randint(0,2)
        self.health_list = [1, 2, 3]

        if self.img_size == 2:
            self.width = 64
            self.height = 64
            self.health = self.health_list[self.img_size]
            self.vel = 1.3

        elif self.img_size ==1:
            self.width = 48
            self.height = 48
            self.health = self.health_list[self.img_size]
            self.vel = 1.5

        else:
            self.width = 32
            self.height = 32
            self.health = self.health_list[self.img_size]
            self.vel = 1.7


        self.hitbox = (self.x, self.y, self.width, self.height)
    def draw(self, win):
        win.blit(self.meteor[self.img_size], (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        pass

    def hit(self):
        global enemies, bullets, score
        #self.health -= 1
        enemies = [enemy for enemy in enemies if enemy not in enemies_removed]

    def delete_enemy(self):
        global enemies, bullets, score
        enemies = [enemy for enemy in enemies if enemy not in enemies_removed]







class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 3
        self.vel = 4
        self.player = pygame.image.load("char/PurpleSpaceship3.png").convert_alpha()
        self.hitbox = (self.x , self.y, width, height)

    def draw(self,win):
        win.blit(self.player, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        self.health -= 1

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





#Ship-Particles
class particlePrinciple:
    def __init__(self):
        self.particles = []
        self.particle_color = (pygame.Color("Red"),pygame.Color("Orange"),
                               pygame.Color("Yellow"), pygame.Color("White"))

    def emit(self):   #ship_width, ship_height
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2]#move
                particle[1] -= 0.2 #shrink
                if particle[1]>5:
                    pygame.draw.circle(win, self.particle_color[0], particle[0], int(particle[1]))#draw circle around particle
                elif particle[1]<=5 and particle[1] >=4:
                    pygame.draw.circle(win, self.particle_color[1], particle[0], int(particle[1]))
                elif particle[1]< 4 and particle[1] >=3:
                    pygame.draw.circle(win, self.particle_color[2], particle[0], int(particle[1]))
                elif particle[1]<3:
                    pygame.draw.circle(win, self.particle_color[3], particle[0], int(particle[1]))


    def add_particles(self, ship_x, ship_y):
        pos_x = ship_x
        pos_y = ship_y
        radius = 6
        direction = 2
        particle_circle = [[round(pos_x+64//2), round(pos_y + 64)], radius, direction] #(ship.x + ship.width//2 - 6), round(ship.y + ship.height//4)
        self.particles.append(particle_circle)

    def delete_particles(self):
        particles_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particles_copy

#-------------------------- FUNCTIONS FOR FAST USE -----------------------------------------#

def RedrawGameWindow():
    #ReDraw Background
    if BG_current == 1:
        win.blit(BG[1], (0, BG_y - screen_h))
        win.blit(BG[0], (0, BG_y) )
    else:
        win.blit(BG[1], (0, BG_y ))
        win.blit(BG[0], (0, BG_y- screen_h))
    text = font.render("SCORE: " + str(score), 1, (255,255,255))


    if ship.health == 3:
        win.blit(Hearts[3], (5, 6))
    elif ship.health == 2:
        win.blit(Hearts[2], (5, 6))
    elif ship.health == 1:
        win.blit(Hearts[1], (5, 6))

    #Draw Player
    #pygame.draw.rect(win, (255,255,255), (x, y, width, height))
    ship.draw(win)
    particle1.emit()

    for enemy in enemies:
        if enemy.y < 500:
            enemy.y += enemy.vel
        else:
            enemies_removed.add(enemy)
            enemy.hit()
        enemy.draw(win)

    win.blit(text, (210, 10))
    for bullet in bullets:
        bullet.draw(win)


    #Updating Window
    pygame.display.update()

def main_menu():
    run = True
    titlefont = pygame.font.SysFont("comicsans", 60,True)
    startfont = pygame.font.SysFont("comicsans",40)
    title = titlefont.render("METEO SHOWER", 1, (255, 255,255))
    start = startfont.render("ENTER TO START",1, (255, 255, 255))
    rect = start.get_rect()
    while run:
        mainClock.tick(60)
        win.blit(BG[0],(0,0))
        win.blit(title, (55, 150))

        win.blit(start,(130, 350))
        pygame.draw.rect(start,(255, 255, 255), rect, 1, border_radius=4)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            run = False





        mainClock.tick(60)
        pygame.display.update()

def game_over():
    global score, enemies
    run = True
    endfont = pygame.font.SysFont("comicsans", 50, True, True)
    end_text = endfont.render("GAME OVER", 1, (137,207,240))
    while run:
        mainClock.tick(60)
        win.blit(end_text, (150, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            run = False
            ship.health = 3
            score = 0
            ship.y = 410
            ship.x = 300
            enemies = []


        pygame.display.update()


def delete_bullets():
    global bullets
    #Updates current bullet list
    bullets = [bullet for bullet in bullets if bullet not in bullets_removed]



#--------------------------------------------------------------------------------------------#


PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 60)

#Important Variables and Objects
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

particle1 = particlePrinciple()



#menu Loop
main_menu()
#MainLoop
while run:

    #register Hit
    hit=False

    #GameClock
    mainClock.tick(60)

    #Checks for current number of enemies : 4 enemies is MAX
    if len(enemies) < 4 and meteoLoop == 0:
        enemies.append(Enemy(randint(50, 450), -64))
        meteoLoop += 1

    #Spawn-Delay for Shots
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    #Spawn-Delay for Enemies
    if meteoLoop > 0:
        meteoLoop += 1
    if meteoLoop >20:
        meteoLoop = 0

    #Checking for events
    for event in pygame.event.get():

        #Quit event
        if event.type == pygame.QUIT:
            run = False
        #Particle Event (adds particles to particle1.particles[])
        if event.type == PARTICLE_EVENT:
            particle1.add_particles(ship.x,ship.y)

    #Checking for projectile & enemy collision
    for bullet in bullets:
        for enemy in enemies:
            if bullet.y + 5  < enemy.hitbox[1] + enemy.height and bullet.y + bullet.height > enemy.hitbox[1]:
                if bullet.x - bullet.width < enemy.hitbox[0] + enemy.width and bullet.x + bullet.width > enemy.hitbox[0]:
                    enemy.health -=1
                    if enemy.health == 0:
                        score += 1
                        enemies_removed.add(enemy)
                    bullets_removed.add(bullet)
                    delete_bullets()
                    hit = True

        #Bullet travelanimation and tracking in boundaries
        if bullet.y > 0 and bullet.y < 500:
            bullet.y += bullet.vel

        else:
            bullets_removed.add(bullet)
            delete_bullets()

    #Checking for enemy & player collision
    for enemy in enemies:

        if ship.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and ship.hitbox[1] + ship.hitbox[3] > enemy.hitbox[1]: #(x, y, 64, 64)
            if ship.hitbox[0] + ship.hitbox[2] > enemy.hitbox[0] and ship.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]: #(x, y , 32, 32)
                enemies_removed.add(enemy)
                enemy.hit()
                ship.hit()

        if hit == True:
            enemy.hit()
            hit = False

    #Gets the state of ALL keys on the keyboard
    keys = pygame.key.get_pressed()



    #Checking for Key inputs
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if len(bullets) < 100:
            bullets.append(projectile(round(ship.x + ship.width//2 - 6), round(ship.y + ship.height//4)))
            #bullets.append(projectile(round(ship.x + ship.width//2 + 6), round(ship.y + ship.height//4) ))
            #bullets.append(projectile(round(ship.x + ship.width//2 - 12), round(ship.y + ship.height//4)))
        shootLoop = 1

    #Main Controls
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

    #Checking & Updating UI according to player-health (ship.health)
    if ship.health == 0:
        win.blit(Hearts[0], (5, 6))
        game_over()

    #Redrawing
    RedrawGameWindow()


pygame.quit()