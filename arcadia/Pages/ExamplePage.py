import pygame

import Components
import Pages
from Pages import Page


class ExamplePage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("green")
        self.components = [
            Components.Label.Label([20, 20], 50, "Example", ["red", "red"]),
            Components.Label.Label([20, 80], 50, "Some Stuff", ["black", "red"], background=True, backWidth=200),
            Components.Button.Button([20, 140], 200, 50, "Example", ["blue", "green"]),
            Components.Label.Label([20, 200], 50, "Some Stuff", ["black", "red"], background=True),
            Components.Button.Button([240, 140], 100, 50, "Back", ["blue", "green"], function=Pages.MainPage.MainPage),
            Components.Button.Button([240, 200], 100, 50, "Exit", ["blue", "green"], function="x")

        ]
