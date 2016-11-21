import pygame

from Components import Component


def abc():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
        , 'q', 'r', 's', 't', 'u', 'v', 'w', 's', 'x', 'y', 'z']


def Backspace(string):
    List = []
    for char in string:
        List.append(char)
    if not List.__len__() == 0:
        List.__delitem__(List.__len__() - 1)
    return "".join(List)


class Label(Component.Component):
    def __init__(self, loc, height, text, colors, **kwargs): #textsize=0, font="font/BebasNeue Bold.otf", background=False
        self.visible = True
        self.loc = self.x, self.y = loc
        self.text = text
        self.height = height

        self.colors = pygame.Color(colors[0]), pygame.Color(colors[1])
        self.clicked = False
        self.hover = False
        self.count = 0

        if "textsize" in kwargs:
            self.textsize = kwargs["textsize"]
        else:
            self.textsize = height

        if "background" in kwargs:
            self.background = kwargs["background"]
        else:
            self.background = False

        if "backLocation" in kwargs:
            loc = kwargs["BackLocation"]
        else:
            pass

        #print text

        if "backWidth" in kwargs:
            self.width = kwargs["backWidth"]
        else:
            self.width = int(len(text) * float(height) * 3.0/ 8.0)

        if "backLength_Width" in kwargs:
            self.backLength_Width = kwargs["backLength_Width"]
        else:
            self.backLength_Width = [self.width, self.height]

        if "font" in kwargs:
            self.font = kwargs["font"]
        else:
            self.font = "font/BebasNeue Bold.otf"





        self.rect = pygame.Rect(loc, self.backLength_Width)

    def check(self, mouse):
        x, y = mouse.x, mouse.y
        if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
            self.hover = True
            if mouse.clicked:
                self.clicked = True
        else:
            if mouse.clicked:
                if not self.count == 0:
                    self.hover = False
                    self.clicked = False
                else:
                    self.count += 1
        return [self.clicked, None]

#    def EventHandle(self,Events):
#        if self.clicked:
#            for event in Events:
#                if event.type == pygame.KEYUP:
#                    if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
#                        self.control = False
#                    elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
#                        self.shift = False
#                if event.type == pygame.KEYDOWN:
#                    print event.type,event.key,"("+event.unicode+")"
#                    if event.key == pygame.K_BACKSPACE:
#                        self.text = Backspace(self.text)
#                    elif event.key == pygame.K_RETURN:
#                        self.clicked = False
#                        self.done = True
#                    elif event.key == 9:
#                        self.text += "     "
#                    elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
#                        self.control = True
#                    else:
#                        self.text += event.unicode

    def display(self, surface):
        if self.visible:
            #            print ":P"
            color2 = self.colors[1]
            color = self.colors[0]
            text_ = self.text
            if self.background:
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
                rect = pygame.Rect(self.loc, self.backLength_Width)
                pygame.draw.rect(surface, color, rect)
            font = pygame.font.Font(self.font, self.textsize)
            text = font.render(text_, 1, color2)
            surface.blit(text, self.loc)
