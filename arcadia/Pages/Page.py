import pygame

"""
Page Class
Author: William Savage
Email:savage.programing@gmail.com

This is the Superclass case for the Pages

Each page should have Components and a background color.

None of the methods should need to be modified.
Display(screen) Fills the screen with the Background cover, then calls the display method of all of it's components
Check(mouse) runs the check methods of all of its components then returns the output from the last true output, or None


"""


class Page:
    def __init__(self):
        self.components = []
        self.backgroundColor = pygame.Color("black")


    # def __init__(self, components, color):
    #     self.components = components
    #     self.backgroundColor = pygame.Color(color)

    def check(self, mouse):
        output = [False, None]
        for component in self.components:
            returned = component.check(mouse)
            if returned[0]:
                output = returned
        return output

    def display(self, screen):
        screen.fill(self.backgroundColor)
        for component in self.components:
            component.display(screen)
