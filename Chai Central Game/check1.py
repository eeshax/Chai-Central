import pygame, sys
from pygame import mixer
mixer.init()
pygame.init() 

screen_width = 800 # This sets the screen width to 800
screen_height = 800 # This sets the screen height to 800
screen = pygame.display.set_mode((screen_width,screen_height))

button_surface = pygame.image.load("level_button.png").convert_alpha()
bg0 = pygame.image.load("mainscreen.png") # This loads the intro screen
bg1 = pygame.image.load("icon.png")
bg2 = pygame.image.load("setting.png") #This loads the jumpscare picture

button_surface = pygame.transform.scale(button_surface, (400,150))
bg0 = pygame.transform.scale(bg0, (screen_width,screen_height))
bg1 = pygame.transform.scale(bg1, (screen_width,screen_height))
bg2 = pygame.transform.scale(bg2, (screen_width,screen_height))

main_font = pygame.font.SysFont("cambria", 50)

path_1 = [((0,400),(200,30)),((200,400),(30,200)),((200,600),(300,30)),((500,300),(30,330)),((530,300),(250,30))] # The rectangle coordinates is written like this ((x,y),(width,height)) , the next rectangle (x+width),y)

path_2 = [((0,600),(200,30)),(())]
run = True

pygame.mouse.set_pos((50,415))
font = pygame.font.Font(None,60)

#engageSound= mixer.Sound("female_scream.wav")

#def scary_pop_up(): #This function allows the jumpscare to appear on the screen when the user fails to stay on the path
    #screen.blit(bg2,(0,0))
    #mixer.Sound.play(engageSound)

class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "yellow")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Button Press!")
    
    def changeColour(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")

button_surface = pygame.image.load("level1.png")
button_surface = pygame.transform.scale(button_surface, (400,150))


class GameState():
    def __init__(self):
        self.state = 'main_menu'


    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.checkForInput(pygame.mouse.get_pos()):
                        self.state = 'level1'
        
        while run:
            button = Button(button_surface, 400, 450, "PLAY")
            msg=main_font.render("THE SCARY MAZE GAME",1,(255,255,0))
            screen.blit(msg,(150,100))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.checkForInput(pygame.mouse.get_pos()):
                            self.state = 'level1'
                            checkGameState()
                    pygame.display.update()
                
            button.update()
            button.changeColour(pygame.mouse.get_pos())
            pygame.display.update()
            screen.fill("black")

    def level1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
##            if self.state == 'level1':
        screen.blit(bg1,(0,0)) # This prints the path onto the screen
        if ((pygame.mouse.get_pos()[0]-730))**2+(pygame.mouse.get_pos()[1]-315)**2<=100:
            msg=font.render("YOU WON",1,(255,255,0)) 
            screen.blit(msg,(300,100)) #This prints the ''YOU WON'' message onto the screen
        
        for x in path_1:
            pygame.draw.rect(screen,(255,255,255),x)
            pygame.draw.circle(screen,(255,0,0),(730,315),10)
            pygame.display.update()
        if any(b[0][0]<pygame.mouse.get_pos()[0]<b[1][0]+b[0][0] and b[0][1]<pygame.mouse.get_pos()[1]<b[1][1]+b[0][1] for b in path_1):
                print("True")
        else:
            print("False")
            run=False

    def level2(self):
        screen.blit(bg1,(0,0)) # This prints the path onto the screen
        if ((pygame.mouse.get_pos()[0]-730))**2+(pygame.mouse.get_pos()[1]-315)**2<=100: #This prints the ''YOU WON'' message onto the screen
            msg=font.render("YOU WON",1,(255,255,0))
            screen.blit(msg,(300,100))    
    
        for x in path_1:
            pygame.draw.rect(screen,(255,255,255),x)
            pygame.draw.circle(screen,(255,0,0),(730,315),10)
            pygame.display.update()
        if any(b[0][0]<pygame.mouse.get_pos()[0]<b[1][0]+b[0][0] and b[0][1]<pygame.mouse.get_pos()[1]<b[1][1]+b[0][1] for b in path_1):
                print("True")
        else:
            print("False")
            run = False







    def state_manager(self):
        if self.state == 'main_menu':
            self.main_menu()
        if self.state == 'level1':
            self.level1()

def checkGameState():
    while True:
        game_state.state_manager()
game_state=GameState()
checkGameState()

