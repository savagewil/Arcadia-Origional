import pygame
import Pages
import Mouse
import Constants

pygame.init()

Screen = pygame.display.set_mode(Constants.SCREENSIZE, pygame.FULLSCREEN)

pygame.key.set_repeat(30, 1)
mouse = Mouse.Mouse(Constants.SCREENSIZE[0]/2, Constants.SCREENSIZE[1]/2)

Currentpage = Pages.ExamplePage.ExamplePage()
Currentpage.check(mouse)
Currentpage.display(Screen)

Done = False
x = 0
count = 0
while not Done:
    pygame.time.delay(1)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            Done = True
    mouse.HandleEvents(events)
    output = Currentpage.check(mouse)
    #print output

    if output[0]:
        if output[1] == "x":
            Done = True
        elif not output[1] is None:
            Currentpage = output[1]
    if count % 10 == 0:
        Currentpage.display(Screen)
    mouse.display(Screen)
    pygame.display.flip()
    count += 1

pygame.quit()
