# This version only runs the game itself without menus the full version has a main menu select game will play through 
#10 rounds click the top card to hear the sound and pick the correct card that it matches
import pygame
import button
import teachingGame

# Initializes the pygame
pygame.init()
pygame.mixer.init()

#display for game
screen = pygame.display.set_mode((1000,500))
bg_img = pygame.image.load('backgroundImages/mainBackround.webp') #backround image for selection screen
bg_img = pygame.transform.scale(bg_img,(1000,500))
gate_bg = pygame.image.load('backgroundImages/gateevening.jpg')   #backround image for selection screen
gate_bg = pygame.transform.scale(gate_bg,(1000,500))
class_bg = pygame.image.load('backgroundImages/classroom a day.png') #backround for teaching game 
class_bg = pygame.transform.scale(class_bg,(1000,500))

#title and icon
pygame.display.set_caption("Living Language")
icon = pygame.image.load('translation.png')
pygame.display.set_icon(icon)

answered = True
clicked = False
action = False

#start,exit button,text box,cards 
start_img = pygame.image.load('backgroundImages/buttonAssets/PlayBtn.png').convert_alpha()   #start button
exit_img = pygame.image.load('backgroundImages/buttonAssets/ExitBtn.png').convert_alpha()   #exit button
exit_press = pygame.image.load('backgroundImages/buttonAssets/ExitClick.png').convert_alpha() #exit pressed 

#button instances
start_button = button.Button(350,400, start_img,0.2)
exit_button = button.Button(550,400, exit_img,0.2)

#game object
game_Begin = teachingGame.TeachingGame()

#changes the game modes
class GameState():
    def __init__(self):
        self.state = 'intro'

    # intro screen for game
    def intro(self):
   
        screen.blit(bg_img,(0,0))
        start_button.draw(screen) 
        exit_button.draw(screen)
        pygame.display.set_caption('Hiragana matching game')
        # get mouse position

        for event in pygame.event.get():
            #if you press the x in the corner exit
            if event.type == pygame.QUIT:
                 pygame.quit()
                 exit()
            #if you press the exit button exit
            if exit_button.draw(screen):
                pygame.quit()
                exit()
            # if you press the start button change states and start the game
            if start_button.draw(screen):
                self.state = 'teaching_Game'
        pygame.display.update()

      
    #screen for teaching game
    def teaching_Game(self):
        #game_Begin.randomizedCards(screen)
        while not game_Begin.playAgain:
            screen.blit(class_bg,(0,0))
            levels = game_Begin.randomizedCards(screen)
            pygame.display.update()
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                pygame.display.update()
            if levels == 0:
                pos = pygame.mouse.get_pos()
                screen.blit(class_bg,(0,0))
                game_Begin.replay(screen)
                #playAgain = True
               

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_Begin.playAgain = False
                        levels = 10
                    
                pygame.display.update()
         

    #manages the states of the game
    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'teaching_Game':
            self.teaching_Game() 

#game state object
game_state = GameState() 

#main game loop 
while True:
    game_state.state_manager()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
 
#<a href="https://www.flaticon.com/free-icons/japanese" title="japanese icons">Japanese icons created by BomSymbols - Flaticon</a> game icon info