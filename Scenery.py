import global_variables
from random import random
import pygame

class Scenery:
    gravity = 9.8
    friccFloor = 30
    friccAir = 1.8
    r = 0
    g = 0
    b = 0
    score = 0
    currentLvl = 1
    highScore = 0

    def __init__(self, highScore) -> None:
        if highScore:
            self.highScore = highScore.get(str(global_variables.difficulty), 0)
        self.gravity = 9.8
        self.friccFloor = 30
        self.friccAir = 1.8
        self.r = 0
        self.g = 0
        self.b = 0
        self.score = 0
        self.currentLvl = 1
    
    def reset(self, highScore):
        if highScore:
            self.highScore = highScore.get(str(global_variables.difficulty), {}).get(str(global_variables.noSideEnemies), 0)
        self.gravity = 9.8
        self.friccFloor = 30
        self.friccAir = 1.8
        self.r = 0
        self.g = 0
        self.b = 0
        self.score = 0
        self.currentLvl = 1

    def render(self):
        global_variables.win.fill((self.r, self.g, self.b))
        pygame.font.init()
        pygame.font.get_init()
        font1 = pygame.font.SysFont('freesanbold.ttf', 50)
        text1 = font1.render('Score: ' + (str)(self.score) , True, (255-self.r, 255-self.g, 255-self.b))
        textRect1 = text1.get_rect()
        textRect1.center = (global_variables.w/2, global_variables.h/2)
        global_variables.win.blit(text1, textRect1)
        text2 = font1.render('Level: ' + (str)(self.currentLvl), True, (255-self.r, 255-self.g, 255-self.b))
        textRect2 = text2.get_rect()
        textRect2.center = (global_variables.w - textRect2.width/2, textRect2.height/2)
        global_variables.win.blit(text2, textRect2)
        text3 = font1.render("High Score: " + (str)(self.highScore), True, (255-self.r, 255-self.g, 255-self.b))
        textRect3 = text3.get_rect()
        textRect3.center = (global_variables.w/2, global_variables.h/2 + textRect1.height/2 + textRect3.height/2)
        global_variables.win.blit(text3, textRect3)

    def randomScenery(self, character):
        self.r = random() * 255
        self.g = random() * 255
        self.b = random() * 255
        self.gravity = random() * 25
        self.friccFloor = random() * character.speed
        self.friccAir = random() * character.speed
        pygame.display.update()

    def updateScore(self, character):
        self.score += character.lvl
        self.currentLvl = character.lvl
        if(self.score % 100 < character.lvl):
            self.randomScenery(character)