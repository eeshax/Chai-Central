import pygame, random, time
pygame.init()


screen = pygame.display.set_mode((1000,700))
screen.fill((255,255,255))
customerlist=["sprite1.png", "sprite2.png"]
peoples = random.choice(customerlist)
pygame.display.update()
clock = pygame.time.Clock()

class Customer(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(peoples)
        self.image = pygame.transform.scale(image, (image.get_width() / 2, image.get_height() / 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

customers = pygame.sprite.Group()
customer = Customer(peoples, 397, 211)
customers.add(customer)

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
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h * ratio))

timer = timer(250, 200, 20, 100,5)

button = 0
run = True
t0 = time.time()
while run:
    t1 = time.time()
    dt = t1 - t0
    timer.time = dt
    print(dt)
    customers.update()
    customers.draw(screen)
    timer.draw(screen)
    if dt >= 5:
        break
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

        

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()

