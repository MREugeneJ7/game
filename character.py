import pygame
import global_variables
from random import random


class Character:
    x = 0
    curVelY = 0
    curAccY = 0
    curVelX = 0
    jumpPower = 40
    speed = 40
    size = 100
    y = global_variables.h - size
    boostPower = 1.1
    lvl = 1
    exp = 0

    def reset(self):
        self.x = 0
        self.curVelY = 0
        self.curAccY = 0
        self.curVelX = 0
        self.jumpPower = 40
        self.speed = 40
        self.size = 100
        self.y = global_variables.h - self.size
        self.boostPower = 1.1
        self.lvl = 1
        self.exp = 0

    def render(self):
        pygame.draw.rect(global_variables.win, (0, 0, 255), (self.x, self.y, self.size, self.size))

    def jump(self):
        self.curAccY -= self.jumpPower

    def move(self, dir):
        if(self.y == global_variables.h - self.size):
            self.curVelX = dir * self.speed
    
    def updatePos(self, sc):
        if self.y <= global_variables.h - self.size:
            if(self.y != global_variables.h - self.size):
                if self.curVelX != 0:
                    self.x += self.curVelX
                    if self.curVelX > 0:
                        self.curVelX -= sc.friccAir
                        self.curVelX = max(self.curVelX, 0)
                    else:
                        self.curVelX += sc.friccAir
                        self.curVelX = min(self.curVelX, 0)
                self.curVelY += sc.gravity
                self.curAccY = 0
                self.y += self.curVelY
            else:
                if self.curVelX != 0:
                    self.x += self.curVelX
                    if self.curVelX > 0 and self.curAccY == 0:
                        self.curVelX -= sc.friccFloor
                        self.curVelX = max(self.curVelX, 0)
                    elif self.curVelX < 0 and self.curAccY == 0:
                        self.curVelX += sc.friccFloor
                        self.curVelX = min(self.curVelX, 0)
                if self.curAccY != 0:
                    self.curVelY += sc.gravity + self.curAccY
                    self.curAccY = 0
                    self.y += self.curVelY
                else:
                    self.curAccY = 0
                    self.curVelY = 0
        self.x = max(0, self.x)
        self.x = min(self.x, global_variables.w - self.size)
        self.y = max(0, self.y)
        self.y = min(self.y, global_variables.h - self.size)
    
    def addExp(self, qt):
        self.exp += qt
        if self.exp > pow(self.lvl, 10 - global_variables.difficulty):
            self.lvl += 1
            boost = (int) (random() * 4)
            if boost == 0:
                self.speed = min(global_variables.w, self.speed * self.boostPower)
            elif boost == 1:
                self.jumpPower = min(global_variables.h, self.jumpPower * self.boostPower)
            elif boost == 2:
                self.size = max(5, self.size / self.boostPower)
            else:
               self.boostPower = min(pow(self.boostPower, 2), 10000)
        return self
    
    def checkCollision(self, en):
        for el in en:
            if(self.x < el.x + el.size 
            and self.x + self.size > el.x
            and self.y < el.y + el.size 
            and self.y + self.size > el.y):
                return False
        else:
            return True