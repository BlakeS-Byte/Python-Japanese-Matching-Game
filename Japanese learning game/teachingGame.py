import pygame
import random
import button
from gtts import gTTS    #library for the reading out loud
from io import BytesIO  

class TeachingGame():
    def __init__ (self):
        self.answered = True
        self.begin = True  
        self.clicked = False
        self.playAgain = False
        self.rounds = 10      

    #function that randomizes card choices
    def randomizedCards(self,screen): 

        duplicates = True

        #font, color, cards 
        base_font = pygame.font.Font("cyberbit.ttf",130)
      
        x = 15
        y = 100
        #top Japanese cards
        displayCard = pygame.Rect(420,y,150,150)   #arguments x,y,pixelWidth,pixelHeight


        #bottom English cards
        answerCard = pygame.Rect(x,y+200,200,150)
        answerCard1 = pygame.Rect(x+260,y+200,200,150)
        answerCard2 = pygame.Rect(x+520,y+200,200,150)
        answerCard3 = pygame.Rect(x+780,y+200,200,150)
        color = pygame.Color('black')    #color of cards

        #Japanese alphabet
        textAlphabet = {'a':'あ','i':'い','u':'う','e':'え','o':'お','ka':'か','ki':'き','ku':'く','ke':'け','ko':'こ','sa':'さ','shi':'し','su':'す','se':'せ','so':'そ','ta':'た',
                        'chi':'ち','tsu':'つ','te':'て','to':'と','na':'な','ni':'に','nu':'ぬ','ne':'ね','no':'の','ma':'ま','mi':'み','mu':'む','me':'め','mo':'も','ya':'や','yu':'ゆ',
                        'yo':'よ','ra':'ら','ri':'り','ru':'る','re':'れ','ro':'ろ','wa':'わ','wo':'を','n':'ん'}
        
        
        if self.answered:
            self.answered = False
        #pick a random elements to display from alphabet dictionary
            self.display = random.sample(textAlphabet.items(),1)
            self.choice1 = random.sample(textAlphabet.items(),1)
            self.choice2 = random.sample(textAlphabet.items(),1)
            self.choice3 = random.sample(textAlphabet.items(),1)

            self.eng, self.jap = self.display[0]
            self.eng1, self.jap1 = self.choice1[0]
            self.eng2 , self.jap2 = self.choice2[0]
            self.eng3 , self.jap3 = self.choice3[0]

        #randomizes the order of the choices
            self.correct_choice = self.eng
            self.tempList = [self.eng,self.eng1,self.eng2,self.eng3]

        
            #Checks for duplicates in the answer cards
            #to do: reassign duplicates
            if(len(set(self.tempList)) == len(self.tempList)):
                duplicates = False
                print("Elements are Unique")
            else:
                print("There are duplicates")
                    

            for p in range(len(self.tempList)-1,0,-1):
                q = random.randint(0,p)
                self.tempList[p],self.tempList[q]= self.tempList[q], self.tempList[p]
        

        #hirigana matching card
            self.text_surface = base_font.render(self.jap,True,(255,255,255))
        
              #english sound matching cards
            self.text_surface4 = base_font.render(self.tempList[0],True,(255,255,255))
            self.text_surface5 = base_font.render(self.tempList[1],True,(255,255,255))
            self.text_surface6 = base_font.render(self.tempList[2],True,(255,255,255))
            self.text_surface7 = base_font.render(self.tempList[3],True,(255,255,255))


        #display all the matching cards
        pygame.draw.rect(screen,color,displayCard)
        pygame.draw.rect(screen,color,answerCard)
        pygame.draw.rect(screen,color,answerCard1)
        pygame.draw.rect(screen,color,answerCard2)
        pygame.draw.rect(screen,color,answerCard3)

        pos = pygame.mouse.get_pos()

        #speaks when you click on the display card
        if displayCard.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                text = str(self.jap)
            
                sound = speak(text)
                pygame.mixer.music.load(sound)
                pygame.mixer.music.play()

        if answerCard.collidepoint(pos):
            #checks if the button has been pressed and if it is the correct answer
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if str(self.tempList[0]) == str(self.correct_choice):
                    self.clicked = True
                    pygame.draw.rect(screen,'green',answerCard)
                    self.answered = True
                    self.begin = True
                    self.rounds-=1
                elif str(self.tempList[0]) != str(self.correct_choice):
                    pygame.draw.rect(screen,'red',answerCard)

        elif answerCard1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                if str(self.tempList[1]) == str(self.correct_choice):
                    pygame.draw.rect(screen,'green',answerCard1)
                    self.answered = True
                    self.begin = True
                    self.rounds-=1
                elif str(self.tempList[1]) != str(self.correct_choice):
                    pygame.draw.rect(screen,'red',answerCard1)
        elif answerCard2.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                if str(self.tempList[2]) == str(self.correct_choice):
                    pygame.draw.rect(screen,'green',answerCard2)
                    self.answered = True
                    self.begin = True
                    self.rounds-=1
                elif str(self.tempList[2]) != str(self.correct_choice):
                    pygame.draw.rect(screen,'red',answerCard3)
        elif answerCard3.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                if str(self.tempList[3]) == str(self.correct_choice):
                    pygame.draw.rect(screen,'green',answerCard3)
                    self.answered = True
                    self.begin = True
                    self.rounds-=1
                elif str(self.tempList[3]) != str(self.correct_choice):
                    pygame.draw.rect(screen,'red',answerCard3)

        #resets the cards so they can be clicked again
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
     
        #display hirigana matching card
        screen.blit(self.text_surface,(displayCard.x,displayCard.y-5))


        #display english matching cards
        screen.blit(self.text_surface4,(answerCard.x,answerCard.y-5))
        screen.blit(self.text_surface5,(answerCard1.x,answerCard1.y-5))
        screen.blit(self.text_surface6,(answerCard2.x,answerCard2.y-5))
        screen.blit(self.text_surface7,(answerCard3.x,answerCard3.y-5))

        self.begin = False

        return self.rounds
    
    #replay screen
    #To do implement replay
    def replay(self,screen):
       
        base_font = pygame.font.Font("cyberbit.ttf",80)
        displayText = pygame.Rect(300,20,150,150)   #arguments x,y,pixelWidth,pixelHeight
        displayText2 = pygame.Rect(200,80,150,150)

        text = "Great Job!"
        text2 = "Thanks for playing!"
        self.text_surface5 = base_font.render(text,True,(255,255,255))
        self.text_surface6 = base_font.render(text2,True,(255,255,255))
        
        screen.blit(self.text_surface5,displayText)
        screen.blit(self.text_surface6,displayText2)
        self.playAgain = True


#creates and plays sound file for alphabet letter    
def speak(sound,language = 'ja'):
    mp3_fo = BytesIO()
    tts = gTTS(sound, lang = language)
    tts.save("sound.mp3")
    title = "sound.mp3"
    return title




    


     







