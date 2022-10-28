import pygame
import global_variables
from random import random


class Enemy:
    x = 0
    y = 0
    curVelY = 0
    curAccY = 0
    curVelX = 0
    size = 20
    lvl = 1
    dead = False

    def __init__(self) -> None:
        if (int)(random()*100) % max(2, 10 - global_variables.difficulty) != 0 or global_variables.noSideEnemies:
            self.x = random() * global_variables.w
        elif (int)(random()*100) % max(2, 10 - global_variables.difficulty) != 0:
            self.y = random() * global_variables.h/2
            self.curVelX = random() * global_variables.w/5
            self.curVelY = random() * -global_variables.h/10
        else:
            self.x = global_variables.w
            self.y = random() * global_variables.h/2
            self.curVelY = random() * -global_variables.h/10
            self.curVelX = random() * -global_variables.w/5
        

    def render(self):
        pygame.draw.rect(global_variables.win, (255, 0, 0), (self.x, self.y, self.size, self.size))

    def jump(self):
        self.curAccY -= self.jumpPower
    
    def updatePos(self, sc):
        if self.y < global_variables.h - self.size:
            self.curVelY += sc.gravity
            self.curAccY = 0
            self.y += self.curVelY
            if self.curVelX != 0:
                    self.x += self.curVelX
                    if self.curVelX > 0:
                        self.curVelX -= sc.friccAir
                        self.curVelX = max(self.curVelX, 0)
                    else:
                        self.curVelX += sc.friccAir
                        self.curVelX = min(self.curVelX, 0)
        else:
            self.dead = True
            
        self.x = max(0, self.x)
        self.x = min(self.x, global_variables.w - self.size)
        self.y = max(0, self.y)
        self.y = min(self.y, global_variables.h - self.size)