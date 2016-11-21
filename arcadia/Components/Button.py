import pygame

"""
Button Class
Author: William Savage
Email:savage.programing@gmail.com

This class displays and handles buttons.
"""


class Button:
    def __init__(self, loc, width, height, text, colors, **kwargs):
        """

        :param loc: the top left corner coordinates with 0,0 being at the top left of the window
        :param width: the width of the background of the button
        :param height: Height of the background of the button
        :param text: Button Text
        :param colors: A 2 element array the first color is the background color of the button, the second is Text color
        :param kwargs: Dictionary which receives keyword arguments
            Keyword Arguments
            :function: can receive a page class, which must be instantiable, or "x" or None, The default is None
            :font: can receive the path of a font file, defaults to "font\\BebasNeue Bold.otf"
            :textLoc: can receive the location of the top left corner of the text, defaults to :param loc
            :textHeight: can receive the height of the button's text, defaults to :param height

        """

        self.loc = self.x, self.y = loc
        self.text = text
        self.lw = self.width, self.height = width, height
        self.rect = pygame.Rect(loc, self.lw)
        self.colors = pygame.Color(colors[0]), pygame.Color(colors[1])

        self.hover = False
        self.clicked = False

        if "function" in kwargs:
            self.function = kwargs["function"]
        else:
            self.function = None

        if "font" in kwargs:
            self.font = kwargs["font"]
        else:
            self.font = "font\\BebasNeue Bold.otf"

        if "textLoc" in kwargs:
            self.textLoc = kwargs["textPosition"]
        else:
            self.textLoc = [self.loc[0] + 4, self.loc[1] + 4]

        if "textHeight" in kwargs:
            self.textHeight = kwargs["textHeight"]
        else:
            self.textHeight = self.height - 8

    def check(self, mouse):
        x, y = mouse.x, mouse.y
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            self.hover = True
            if mouse.clicked:
                self.clicked = True
                if self.function == "x" or self.function is None:
                    return [True, self.function]
                else:
                    return [True, self.function()]
            else:
                return [False, None]
        else:
            self.hover = False
            self.clicked = False
            return [False, None]

    def display(self, surface):
        color = self.colors[0]
        color2 = self.colors[1]
        if self.hover:
            #print 1
            c1 = 0
            c2 = 0
            c3 = 0
            if not color[0] < 50:
                c1 = color[0] - 50
            elif not color[1] < 50:
                c2 = color[1] - 50
            elif not color[2] < 50:
                c3 = color[2] - 50
            color = c1, c2, c3, 255
            c1 = 0
            c2 = 0
            c3 = 0
            if not color2[0] < 50:
                c1 = color2[0] - 50
            elif not color2[1] < 50:
                c2 = color2[1] - 50
            elif not color2[2] < 50:
                c3 = color2[2] - 50
            color2 = c1, c2, c3, 255
        c1 = 255
        c2 = 255
        c3 = 255
        if not color[0] > 235:
            c1 = color[0] + 20
        elif not color[1] > 235:
            c2 = color[1] + 20
        elif not color[2] > 235:
            c3 = color[2] + 20
        color_ = c1, c2, c3, 255
        pygame.draw.rect(surface, color, self.rect)
        font = pygame.font.Font(self.font, self.textHeight)
        text = font.render(self.text, 1, color2)
        surface.blit(text, self.textLoc)
