import pygame

pygame.init()

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
