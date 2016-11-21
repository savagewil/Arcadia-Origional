import pygame

CHANGE = 2


class Mouse():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.clicked = False

    def display(self, Screen):
        if not self.clicked:
            pygame.draw.circle(Screen, pygame.Color("Black"), [self.x, self.y], 5)
            pygame.draw.circle(Screen, pygame.Color("white"), [self.x, self.y], 2)
        else:
            pygame.draw.circle(Screen, pygame.Color("white"), [self.x, self.y], 5)
            pygame.draw.circle(Screen, pygame.Color("black"), [self.x, self.y], 2)

    def HandleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.y -= CHANGE
                elif event.key == pygame.K_DOWN:
                    self.y += CHANGE
                elif event.key == pygame.K_LEFT:
                    self.x -= CHANGE
                elif event.key == pygame.K_RIGHT:
                    self.x += CHANGE
                elif event.key == pygame.K_SPACE:
                    self.clicked = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.clicked = False
