import pygame

from Components import Component


class Container(Component.Component):
    def __init__(self, Top, Left, Length, hieght, Components, color):
        self.conponents = Components
        self.color = pygame.Color(color)
        self.rect = pygame.Rect(Left, Top, Length, hieght)

    def check(self, events):
        test = [False, None]
        for Component in self.conponents:
            output = Component.check(events)
            if output[0]:
                test = output
        return test

    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        for Component in self.conponents:
            Component.display(screen)