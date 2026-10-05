##    def start_screen(self):    
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##        screen.fill((146, 144, 106))
##        screen.blit(textsurface, (245,15))
##        if level_button.draw(screen):
##            self.state = "levels"
##        if tutorial_button.draw(screen):
##            self.state = "main_game"
##        if settings_button.draw(screen):
##            self.state = "settings"
##        if quitgame_button.draw(screen):
##            event.type==pygame.QUIT
##            pygame.quit()
##            
##        pygame.display.update()
##                
##    def levels(self):
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##        screen.fill((146, 144, 106))
##        screen.blit(textsurface2, (375,15))
##        if level1.draw(screen):
##            self.state = "main_game"
##        if level2.draw(screen):
##            self.state = "main_game"
##        if level3.draw(screen):
##            self.state = "main_game"
##        if level4.draw(screen):
##            self.state = "main_game"
##        if level5.draw(screen):
##            self.state = "main_game"
##        pygame.display.update()

##    def settings(self):
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##        screen.fill((146, 144, 106))
##        screen.blit(rtext, (447,34))
##        screen.blit(menu, (63, 60))
##        pygame.display.update()
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_r:
##                screen.fill((146,144,106))
                
##    def state_manager(self):
##        if self.state == "start_screen":
##            self.start_screen()
##        if self.state == "levels":
##            self.levels()
##        if self.state == "main_game":
##            self.main_game()
##        if self.state == "settings":
##            self.settings()
##        if self.state == "actual_bulk":
##            self.actual_bulk()
