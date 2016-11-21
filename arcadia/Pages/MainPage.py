import pygame
import ExamplePage
import Components
from Pages import Page


class MainPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([250, 50], 100, "RED SHIFT", ["red", "black"]),
            Components.Container.Container(300, 0, 800, 300, [
                Components.Button.Button([750-200, 350], 200, 60, "Example", ["black", "white"], textHeight=68,
                                         function=ExamplePage.ExamplePage),
                Components.Button.Button([750 - 200, 420], 100, 60, "Exit", ["black", "white"], textHeight=68,
                                         function="x")
            ], "grey")
        ]
