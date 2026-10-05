import pygame, Button, sys, Videomodule, random, time 
pygame.init()

### screens, displays and images ###
screen = pygame.display.set_mode((1000,700))
screen2 = pygame.image.load("mainscreen.png").convert_alpha()
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Chai Central")
clock=pygame.time.Clock()
me = pygame.image.load("eeha.jpg").convert_alpha()
me1 = pygame.transform.scale(me, (244,242))
recipepage = pygame.image.load("recipes.png").convert_alpha()
recip = pygame.transform.scale(recipepage, (1000,700))
end_game = pygame.image.load("endgame.png").convert_alpha()
endgame = pygame.transform.scale(end_game, (1000,700))
setting_pic = pygame.image.load("settings screen.png").convert_alpha()
settingpic = pygame.transform.scale(setting_pic, (950, 650))

### buttons ###
pointer = pygame.image.load("sugar.png").convert_alpha()
points = pygame.transform.scale(pointer, (412, 92))
speech = pygame.image.load("speechbubble.png").convert_alpha()
speechbubble = pygame.transform.scale(speech, (400, 187))
level = pygame.image.load("level_button.png").convert_alpha()
tutorial = pygame.image.load("tutorial_button.png").convert_alpha()
settings = pygame.image.load("settings_button.png").convert_alpha()
quit_game = pygame.image.load("quitgame_button.png").convert_alpha()

level_button = Button.Button(380, 140, level, 0.4)
tutorial_button = Button.Button(380, 280, tutorial, 0.4)
settings_button = Button.Button(380, 420, settings, 0.4)
quitgame_button = Button.Button(380, 560, quit_game, 0.4)

level1button = pygame.image.load("level1.png").convert_alpha()
level2button = pygame.image.load("level2.png").convert_alpha()
level3button = pygame.image.load("level3.png").convert_alpha()
level4button = pygame.image.load("level4.png").convert_alpha()
level5button = pygame.image.load("level5.png").convert_alpha()

level1 = Button.Button(116, 126, level1button, 0.3)
level2 = Button.Button(232, 242, level2button, 0.3)
level3 = Button.Button(348, 358, level3button, 0.3)
level4 = Button.Button(464, 474, level4button, 0.3)
level5 = Button.Button(580, 590, level5button, 0.3)

pause = pygame.image.load("pause.png").convert_alpha()
pause_button = Button.Button(940, 1, pause, 0.2)

confirm = pygame.image.load("confirm.png").convert_alpha()
confirm_button = Button.Button(0, 95, confirm, 0.4)

recipe = pygame.image.load("recipebook.png").convert_alpha()
recipe_book = Button.Button(800, 1, recipe, 0.2)

Return = pygame.image.load("Return.png").convert_alpha()
return_button = Button.Button(0, 0, Return, 0.2)

### sounds ###

ding = pygame.mixer.Sound("service-bell-ring-14610.mp3")
ding.set_volume(0.4)
coffee = pygame.mixer.Sound("coffee_V1.mp3")
coffee.set_volume(0.4)
ambience = pygame.mixer.Sound("ambience.mp3")
ambience.set_volume(0.4)
sinks = pygame.mixer.Sound("sinks_V11.mp3")
sinks.set_volume(0.4)
cups = pygame.mixer.Sound("cups_V1.mp3")
cups.set_volume(0.4)
sizzle = pygame.mixer.Sound("sizzle.mp3")
sizzle.set_volume(0.4)
keyboard = pygame.mixer.Sound("keyboards_V1.mp3")
keyboard.set_volume(0.4)
chopping = pygame.mixer.Sound("chops_V1.mp3")
chopping.set_volume(0.4)
elevator = pygame.mixer.Sound("jazz music.mp3")
elevator.set_volume(0.4)

### texts and fonts ###

font = pygame.font.SysFont("Comic Sans MS", 90)
font1 = pygame.font.SysFont("Comic Sans MS", 45)
font2 = pygame.font.SysFont("Comic Sans MS", 30)
textsurface = font.render("Chai Central", True, (0,0,0))
textsurface2 = font.render("Levels", True, (0,0,0))

title = font.render("Settings", True, (0,0,0))
pausemenu = font.render("Game paused", True, (0,0,0))
pausemenu1 = font1.render("Press c to continue or q to quit", True, (0,0,0))

# cm = coffee machine, i = interactives, cb = chopping board, cr = cash register

cm1 = pygame.Rect(551, 449, 76, 146)
cm2 = pygame.Rect(892, 459, 107, 155)
pan = pygame.Rect(643, 514, 83, 37)
cb = pygame.Rect(383, 534, 129, 59)
cup = pygame.Rect(29, 517, 83, 64)
cr = pygame.Rect(152, 400, 180, 112)
sink = pygame.Rect(944, 628, 55, 48)

i = pygame.Surface((146,76))
i = pygame.Surface((155,107))
i = pygame.Surface((37,83))
i = pygame.Surface((59,129))
i = pygame.Surface((64,83))
i = pygame.Surface((112,180))
i = pygame.Surface((48,55))

### all procedures, classes etc###

# pause screen
def pauses():
    elevator.play()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                    elevator.stop()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        screen.fill((146, 144, 106))
        screen.blit(pausemenu, (245,15))
        screen.blit(pausemenu1, (190,200))
        screen.blit(me1, (350,357))
        pygame.display.update()
        clock.tick(5)

def recipebook():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))
        screen.blit(recip, (0,0))
        if return_button.draw(screen):
            paused = False
        pygame.display.update()
        clock.tick(5)


# initial start up for the main game
num = 0
def startup():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    screen.blit(screen2, (0,0))
    screen.blit(points, (0,0))
    point = font1.render(str(num), True, (0,0,0))
    screen.blit(point, (299,12))
    if pause_button.draw(screen2):
        pauses()

# the actual game requiring the user
correction = ""
def main_game():
    global correction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cm1.collidepoint(event.pos):
                print("pouring coffee")
                coffee.play()
                correction = correction+"cm1"
                print(correction)
            if cm2.collidepoint(event.pos):
                print("pouring coffee")
                coffee.play()
                correction = correction+"cm2"
                print(correction)
            if pan.collidepoint(event.pos):
                print("warming pan...")
                sizzle.play()
                correction = correction+"pan"
                print(correction)
            if cb.collidepoint(event.pos):
                print("chopping ingredients...")
                chopping.play()
                correction = correction+"cb"
                print(correction)
            if cup.collidepoint(event.pos):
                print("one cup taken")
                cups.play()
                correction = correction+"cup"
                print(correction)
            if cr.collidepoint(event.pos):
                print("cash register")
                keyboard.play()
                correction = correction+"cr"
                print(correction)
            if sink.collidepoint(event.pos):
                print("washing...")
                sinks.play()
                correction = correction+"sink"
                print(correction)
            pygame.display.update()

### customer class & sprites ###

customerlist=["sprite1.png", "sprite2.png"]
             
class Customer(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(peoples)
        self.image = pygame.transform.scale(image, (image.get_width() / 2, image.get_height() / 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
           
class timer():
    def __init__(self, x, y, w, h, max_time):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.time = max_time
        self.max_time = max_time
    def draw(self, surface):
        ratio = self.time / self.max_time
        rect1 = pygame.draw.rect(surface, "green", (self.x, self.y, self.w, self.h))
        rect2 = pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h * ratio))


# randomly selects elements for the customer's "order"

def teastuff():
    assam = "cm2"+"pan"+"sink"+"cb"
    masala = "cr"+"cup"+"cm1"+"sink"
    badshah = "pan"+"cup"+"cm2"+"cm1"
    royal = "cr"+"cm2"+"cup"+"sink"
    tulsi = "cb"+"pan"+"sink"+"cm1"
    darjeeling = "cup"+"cr"+"pan"+"sink"
    kashmiri = "cm1"+"cm2"+"sink"+"cup"
    
    tea = [("assam",assam),("masala",masala),("badshah",badshah),("royal",royal),("tulsi",tulsi),("darjeeling",darjeeling),("kashmiri",kashmiri)]
    
    menu1 = random.choice(tea)
    menu2 = random.choice(tea)
    tea1, tea2 = menu1
    i1, i2 = menu2
    return tea1, tea2
    return i1, i2



peoples = random.choice(customerlist)
customers = pygame.sprite.Group()
customer = Customer(peoples, 445, 400)
customers.add(customer)
timing = 100
timervalue = 73
#timer value is the amount of time user gets to complete order
timer = timer(370, 200, 20, 100, timervalue)


def game():
    global t0
    global t1
    global dt
    global customers
    global tea1
    global tea2
    global i1
    global i2
    global t4
    global t2
    global dt2
    global correction
    global num
    global count
    t1= time.time()
    dt = t1 - t0
    startup()
    if dt >= 3:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    correction = ""
                    print("restarted recipe")
        customers.update()
        customers.draw(screen)
        screen.blit(speechbubble, (430,120))
        # tea1+" "+i1 represents the customer's order on screen
        speech = "I want"+" "+(tea1+" "+"and"+" "+i1)
        customer_speech = font2.render(speech, True, (0,0,0))
        screen.blit(customer_speech, (435,155))
        t2 = time.time()
        dt2 = t2 - t4
        timer.time = dt2
        timer.draw(screen)
        if timer.time>=timervalue:
            t0 = t1
            t4 = t2
            count = count + 1
            peoples = random.choice(customerlist)
            customers = pygame.sprite.Group()
            customer = Customer(peoples, 445, 400)
            customers.add(customer)
            correction = ""
            tea1, tea2 = teastuff()
            i1, i2 = teastuff()
        main_game()
        #checks user input over answer
        if confirm_button.draw(screen):
            # tea2+i2 represents the user's answer
            if tea2+i2 == correction:
                num = num + 1
                count = count +1
                t0 = t1
                t4 = t2
                print("correct")
                correction = ""
                tea1, tea2 = teastuff()
                i1, i2 = teastuff()
                peoples = random.choice(customerlist)
                customers = pygame.sprite.Group()
                customer = Customer(peoples, 445, 400)
                customers.add(customer)
                pygame.display.update()
            else:
                count = count +1
                t0 = t1
                t4 = t2
                print("incorrect")
                correction = ""
                tea1, tea2 = teastuff()
                i1, i2 = teastuff()
                peoples = random.choice(customerlist)
                customers = pygame.sprite.Group()
                customer = Customer(peoples, 445, 400)
                customers.add(customer)
                pygame.display.update()





        
### main game loop ###

game_state = 1
t0 = time.time()
t4 = time.time()
tea1, tea2 = teastuff()
i1, i2 = teastuff()
run = True
while run:

    #creates a timer
    t1 = time.time()
    t2 = time.time()
    
    #menu screen
    if game_state==1:
        screen.fill((146, 144, 106))
        screen.blit(textsurface, (245,15))
        if level_button.draw(screen):
            game_state=2
        if tutorial_button.draw(screen):
            game_state=3
        if settings_button.draw(screen):
            game_state=4
        if quitgame_button.draw(screen):
            event.type==pygame.QUIT
            run = False
        pygame.display.update()
    
    #levels screen
    elif game_state==2:
        screen.fill((146, 144, 106))
        screen.blit(textsurface2, (375,15))
        if level1.draw(screen):
            game_state=5
        if level2.draw(screen):
            game_state=6
        if level3.draw(screen):
            game_state=7
        if level4.draw(screen):
            game_state=8
        if level5.draw(screen):
            game_state=9
        pygame.display.update()

    #tutorial level
    elif game_state==3:
        num = 0
        screen.fill((255, 255, 255))
        screen.blit(screen2, (0,0))
        startup()
        main_game()
        customers.update()
        customers.draw(screen)
        pygame.display.update()
        
    #settings screen
    elif game_state==4:
        screen.fill((146, 144, 106))
        screen.blit(title, (310,15))
        screen.blit(settingpic, (0,0))
        pygame.display.update()

#main game after level is chosen
        
    #level 1
    elif game_state==5:
        num = 0
        t0 = t1
        t4 = t2
        count = 0
        while game_state == 5:
            game()
            if recipe_book.draw(screen):
                recipebook()
            if count == 3:
                game_state = 10
                break
            pygame.display.update()

    #level 2
    elif game_state == 6:
        num = 0
        t0 = t1
        t4 = t2
        count = 0
        while game_state == 6:
            game()
            if recipe_book.draw(screen):
                recipebook()
            if count == 3:
                game_state = 10
                break
            pygame.display.update()
            
    #level 3
    elif game_state == 7:
        num = 0
        t0 = t1
        t4 = t2
        count = 0
        while game_state == 7:
            game()
            if recipe_book.draw(screen):
                recipebook()
            if count == 3:
                game_state = 10
                break
            pygame.display.update()
            
    #level 4
    elif game_state == 8:
        num = 0
        t0 = t1
        t4 = t2
        count = 0
        while game_state == 8:
            game()
            if count == 5:
                game_state = 10
                break
            pygame.display.update()

    #level 5
    elif game_state == 9:
        num = 0
        t0 = t1
        t4 = t2
        count = 0
        while game_state == 9:
            game()
            if count == 5:
                game_state = 10
                break
            pygame.display.update()
            
    #endgame screen
    elif game_state == 10:
        screen.fill((0,0,0))
        screen.blit(endgame, (0,0))
        cubes = font2.render(str(num)+"/"+str(count)+" sugar cubes!", True, (0,0,0))
        screen.blit(cubes, (584, 138))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    game_state = 2
            if event.type==pygame.QUIT:
                run = False
        
    #the main event loop                                             
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state=1
        if event.type==pygame.QUIT:
            run = False
        #makes the rect of input transparent on screen.
        i.set_alpha(128)
        i.fill((255,255,255))          
        screen2.blit(i, (0,0))
        pygame.display.update()
        


pygame.display.update()
clock.tick(60)
pygame.quit()
