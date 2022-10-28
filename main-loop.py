from random import random
import pygame
from character import Character
from enemy import Enemy
from Scenery import Scenery
import global_variables
import pickledb
import pygame_menu

pygame.init()
pygame.display.set_caption("Squarey")
db = pickledb.load('high-score.db', True)
ch = Character()
en = []
highScore = db.get('high-score')
sc = Scenery(highScore)

run = True

def draw_game():
          sc.render()
          ch.render()
          for el in en:
            el.render()
          pygame.display.update()
def play(run):
    while run:
        pygame.time.delay(100)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            ch.jump()
        if keys[pygame.K_RIGHT]:
            ch.move(1)
        if keys[pygame.K_LEFT]:
            ch.move(-1)

        

        ch.updatePos(sc)
        run = ch.checkCollision(en)

        if pygame.time.get_ticks() % max(2,((10 - global_variables.difficulty)*10 - ch.lvl)) == 0:  
            for i in range(ch.lvl):
                en.append(Enemy())

        for el in en:
            el.updatePos(sc)
            if el.dead:
                sc.updateScore(ch.addExp(1))
                en.remove(el)

        if keys[pygame.K_ESCAPE]:
            run = False
        draw_game()
    if(highScore.get(str(global_variables.difficulty), {}).get(str(global_variables.noSideEnemies), 0) < sc.score):
        if(highScore.get(str(global_variables.difficulty), {}) == {}):
            highScore[str(global_variables.difficulty)] = {}    
        highScore[str(global_variables.difficulty)][str(global_variables.noSideEnemies)] = sc.score
        db.set('high-score', highScore)

def startGame():
    run = True
    sc.reset(highScore)
    en.clear()
    ch.reset()
    play(run)

def setDifficulty(value, difficulty):
    global_variables.difficulty = difficulty

def setSideEnemies(value, sideEnemies):
    global_variables.noSideEnemies = not sideEnemies

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Difficulty :', global_variables.difficultySelector, onchange=setDifficulty)
menu.add.selector('Side Enemies :', [('Yes', True),('No', False)], onchange=setSideEnemies)
menu.add.button('Play', startGame)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(global_variables.win)



pygame.quit()
