import pygame

#button class 
class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.action = False

    #draws buttons and checks to see if they are clicked
    def draw(self,surface):
        action = False
        # find the position of the mouse
        pos = pygame.mouse.get_pos()

        #check if mouse is over the buttons
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #[0] is left mouse button 
                self.clicked = True
                self.action = True
                print("button clicked")
                return self.action

        #if mouse button is not clicked reset the trigger
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        #draw button on screen
        surface.blit(self.image,(self.rect.x, self.rect.y))

        return self.action
        
        