import pygame

w = 1280
h = 720
difficultySelector = [('Boring', 0), 
                      ('Less Boring', 1),
                      ('Easy', 2),
                      ('Appropiate', 3),
                      ('Less Than Medium', 4),
                      ('Medium', 5),
                      ('Medium High', 6),
                      ('Hard', 7),
                      ('Very Hard', 8),
                      ('Impossible', 9),
                      ('Don\'t Try This', 10)]
difficulty = 0
noSideEnemies = False

win = pygame.display.set_mode((w, h))
