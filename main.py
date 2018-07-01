import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
bright_red = (200,0,0)
bright_green = (0,200,0)

red = (255,0,0)
green = (0,255,0)

g_color = (100,217,135)
grey = (192,192,192)
bug_width = 58

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bug\'s Race')
clock = pygame.time.Clock()

bugImg = pygame.image.load('bug.png')

pause = False

def bug(x,y):
    gameDisplay.blit(bugImg,(x,y))

def thing_dodged(count):
    font = pygame.font.SysFont('comicsansms',30)
    text = font.render("Dodged : "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def text_objects(text,font):
    textSurface = font.render(text,True,red)
    return textSurface,textSurface.get_rect()

def intro_text(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text,dodged):
    crashText = pygame.font.SysFont('comicsansms',30)
    TextSurf , TextRect = text_objects(text,crashText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(1)
    message_display1("""Your  Score : """ + str(dodged))

def message_display1(text):
    crashText = pygame.font.SysFont('comicsansms',20)
    TextSurf , TextRect = text_objects(text,crashText)
    TextRect.center = ((display_width/2.1),(display_height/1.8))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(1)
    game_intro()


def crash(dodged):
    message_display(""" You Crashed !!! """,dodged)


def thing(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def circle(cx, cy, cr, color):
    pygame.draw.circle(gameDisplay,color,(cx, cy), cr)

def button(msg,x,y,w,h,ic,ac,action=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x+w > mouse[0] > x and y+h > mouse[1] >y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action!=None:
                if action == "play":
                    game_loop()
                if action == "quit":
                    pygame.quit()
                    quit()
                if action == "unpause":
                    global pause
                    pause = False
            
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

        introText = pygame.font.SysFont('comicsansms',10)
        TextSurf , TextRect = intro_text(msg,introText)
        TextRect.center = (x+(w/2),y+(h/2))
        gameDisplay.blit(TextSurf,TextRect)  



def paused():
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        bugImg = pygame.image.load('bug.png')
        bug(365,185)
        introText = pygame.font.SysFont('comicsansms',20)
        TextSurf , TextRect = text_objects(" A BUG'S RACE ",introText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button("Continue", 180,420,100,50,green,bright_green,"unpause")
        button("QUIT", 530,420,100,50,red,bright_red,"quit")

        TextSurf , TextRect = text_objects(" Created By: Santosh ",introText)
        TextRect.center = (700,580)
        gameDisplay.blit(TextSurf,TextRect)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        bugImg = pygame.image.load('bug.png')
        bug(365,185)
        introText = pygame.font.SysFont('comicsansms',20)
        TextSurf , TextRect = text_objects(" A BUG'S RACE ",introText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button("GO!!!", 180,420,100,50,green,bright_green,"play")
        button("QUIT", 530,420,100,50,red,bright_red,"quit")

        TextSurf , TextRect = text_objects(" Created By: Santosh ",introText)
        TextRect.center = (700,580)
        gameDisplay.blit(TextSurf,TextRect)

        pygame.display.update()
        clock.tick(15)
    


def game_loop():
    gameExit = False
    global pause
    x =  (display_width * 0.45)
    y = (display_height * 0.80)
    dodged = 0

    #Dimensions of rectangle
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_startw = 80
    thing_starth = 80
    thing_speed = 5

    #Dimensions of circle

    circle_startx = random.randrange(0,display_width)
    circle_starty = -100
    circle_radiousr = 32
    circle_speed = 5
    
    x_change = 0
    y_change = 0

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5    
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change    
        gameDisplay.fill(grey)

        # thing(thingx, thingy, thingw, thingh, color):
        thing(thing_startx, thing_starty, thing_startw, thing_starth, g_color)


        #gameDisplay,color,cx, cy, cr
        circle(circle_startx, circle_starty, circle_radiousr, black)
        
        thing_starty  += thing_speed
        circle_starty += circle_speed
        bug(x,y)
        thing_dodged(dodged)
        
        if (x > display_width - bug_width or x < 0) or (y > display_height - bug_width or y < 0):
            crash(count)

        if thing_starty > display_height:
            thing_starty = 0 - thing_starth
            thing_startx = random.randrange(0,display_width)
            dodged+=1
            thing_speed +=0.5

        if circle_starty > display_height:
            circle_starty = 0 - circle_radiousr
            circle_startx = random.randrange(0,display_width)
            dodged += 1
            circle_speed +=1

        if y > thing_starty+thing_starth and y < thing_starty + thing_startw or y +bug_width >thing_starty and y+bug_width < thing_starty+thing_starth:
            print(" Y_crossover")

            if x > thing_startx and x < thing_startx + thing_startw or x+bug_width >thing_startx and x+bug_width < thing_startx+thing_starth:
                crash(dodged)

        if y > circle_starty+circle_radiousr and y <  circle_starty + circle_radiousr or y +bug_width >circle_starty and y+bug_width < circle_starty+circle_radiousr:
            print(" Y_crossover")

            if x > circle_startx and x < circle_startx + circle_radiousr or x+bug_width >circle_startx and x+bug_width < circle_startx+circle_radiousr:
                crash(dodged)

                
        pygame.display.flip()
        clock.tick(60)


game_intro()
pygame.quit()
quit()
