# python3 -m pip install pygame

# imports
import sys
import pygame
import math
import os
import random

# instantiations
width = 500
height = 500

#colors
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)


class target(object):
    
    # target initialization
    def __init__(self, color, width, height):
        self.color = color
        self.clicked = True
        # position
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0,0,500,500)
        
    # draw the piece
    def drawTarget(self, disp, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #self.rect = pygame.Rect(0,0,100,100)
        pygame.draw.rect(disp, self.color, self.rect)
        self.clicked = False

# score board class
class scoreboard(object):
    
    # score board initialization
    def __init__(self, disp):
        self.disp = disp
        self.name = pygame.font.match_font('arial')
    
    # draw text
    def text(self, disp, text, x, y, color, size):
        self.font = pygame.font.Font(self.name, size)
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        disp.blit(text_surface, text_rect)

# main thingy
def run():
    #print('run')
    # make display
    disp = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Aim Practice')
    
    # more initializations
    pygame.init()
    inGame = True
    inMenu = True
    clicked = True
    lose = False
    
    easyClicked = False
    normalClicked = False
    hardClicked = False
    customClicked = False
    edit1 = False
    edit2 = False
    text1 = ""
    text2 = ""
    
    color1 = black
    color2 = black
    color3 = black
    color4 = black
    color5 = black
    color6 = black
    
    # dimensions of target
    tarwidth = 100
    tarheight = 100
    
    cl = pygame.time.Clock()
    sb = scoreboard(disp)
    
    # create target
    tar = target(black, tarwidth, tarheight)
    tar.drawTarget(disp, 250, 250)
    
    # how many clickced/level
    clicked_count = 0
    # how much time you have
    time = 0
    # keep track of time
    time_count = 0
    # total reaction time
    total_time = 0

    # in menu
    while inMenu == True:

        easyRect = pygame.Rect(40, 220, 60, 60)
        normalRect = pygame.Rect(160, 220, 60, 60)
        hardRect = pygame.Rect(280, 220, 60, 60)
        customRect = pygame.Rect(400, 220, 60, 60)
        text1Rect = pygame.Rect(350, 335, 100, 36)
        text2Rect = pygame.Rect(350, 385, 100, 36)
        
        # key input to break loop
        for event in pygame.event.get():
            
            # exit game
            if event.type == pygame.QUIT:
                pygame.quit()
                    
            # if mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # see if clicked on
                if easyRect.collidepoint(pos):
                    color1 = green
                    color2 = black
                    color3 = black
                    color4 = black
                    color5 = black
                    color6 = black
                    edit1 = False
                    edit2 = False
                    
                elif normalRect.collidepoint(pos):
                    color1 = black
                    color2 = green
                    color3 = black
                    color4 = black
                    color5 = black
                    color6 = black
                    edit1 = False
                    edit2 = False
                    
                elif hardRect.collidepoint(pos):
                    color1 = black
                    color2 = black
                    color3 = green
                    color4 = black
                    color5 = black
                    color6 = black
                    edit1 = False
                    edit2 = False
                    
                elif customRect.collidepoint(pos):
                    color1 = black
                    color2 = black
                    color3 = black
                    color4 = green
                    color5 = red
                    color6 = red
                    edit1 = False
                    edit2 = False

                elif text1Rect.collidepoint(pos):
                    edit1 = True
                    edit2 = False

                elif text2Rect.collidepoint(pos):
                    edit1 = False
                    edit2 = True
                    
            # if a key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inMenu = False
                if event.key == pygame.K_1:
                    if edit1:
                        text1 = text1 + "1"
                    elif edit2:
                        text2 = text2 + "1"
                elif event.key == pygame.K_2:
                    if edit1:
                        text1 = text1 + "2"
                    elif edit2:
                        text2 = text2 + "2"
                elif event.key == pygame.K_3:
                    if edit1:
                        text1 = text1 + "3"
                    elif edit2:
                        text2 = text2 + "3"
                elif event.key == pygame.K_4:
                    if edit1:
                        text1 = text1 + "4"
                    elif edit2:
                        text2 = text2 + "4"
                elif event.key == pygame.K_5:
                    if edit1:
                        text1 = text1 + "5"
                    elif edit2:
                        text2 = text2 + "5"
                elif event.key == pygame.K_6:
                    if edit1:
                        text1 = text1 + "6"
                    elif edit2:
                        text2 = text2 + "6"
                elif event.key == pygame.K_7:
                    if edit1:
                        text1 = text1 + "7"
                    elif edit2:
                        text2 = text2 + "7"
                elif event.key == pygame.K_8:
                    if edit1:
                        text1 = text1 + "8"
                    elif edit2:
                        text2 = text2 + "8"
                elif event.key == pygame.K_9:
                    if edit1:
                        text1 = text1 + "9"
                    elif edit2:
                        text2 = text2 + "9"
                elif event.key == pygame.K_0:
                    if edit1:
                        text1 = text1 + "0"
                    elif edit2:
                        text2 = text2 + "0"
                elif event.key == pygame.K_PERIOD:
                    if edit1:
                        text1 = text1 + "."
                    elif edit2:
                        text2 = text2 + "."
                elif event.key == pygame.K_BACKSPACE:
                    #print('back')
                    if edit1 and len(text1) > 0:
                        text1 = text1[0:len(text1)-1]
                    if edit2 and len(text2) > 0:
                        text2 = text2[0:len(text2)-1]
                
                    
        # draw
        disp.fill(white)
        
        # draw buttons
        pygame.draw.rect(disp, color1, easyRect, 2)
        pygame.draw.rect(disp, color2, normalRect, 2)
        pygame.draw.rect(disp, color3, hardRect, 2)
        pygame.draw.rect(disp, color4, customRect, 2)

        # draw text in buttons
        sb.text(disp, 'Easy', 70, 245, color1, 18)
        sb.text(disp, 'Normal', 190, 245, color2, 18)
        sb.text(disp, 'Hard', 310, 245, color3, 18)
        sb.text(disp, 'Custom', 430, 245, color4, 18)

        # draw text box's
        if len(text1) > 0 and color4 == green:
            color5 = green
            pygame.draw.rect(disp, green, text1Rect, 2)
        elif (len(text1) < 1 and edit1) or color4 == black:
            color5 = black
            pygame.draw.rect(disp, black, text1Rect, 2)
        elif len(text1) < 1 and color4 == green:
            color5 = red
            pygame.draw.rect(disp, red, text1Rect, 2)
            
        if len(text2) > 0 and color4 == green:
            color6 = green
            pygame.draw.rect(disp, green, text2Rect, 2)
        elif (len(text2) < 1 and edit2) or color4 == black:
            color6 = black
            pygame.draw.rect(disp, black, text2Rect, 2)
        elif len(text2) < 1 and color4 == green:
            color6 = red
            pygame.draw.rect(disp, red, text2Rect, 2)

        # draw text in text box
        sb.text(disp, text1, 400, 350, black, 18)
        sb.text(disp, text2, 400, 400, black, 18)

        # draw information
        sb.text(disp, 'Welcome to Aim Practice', 250, 75, black, 48)
        sb.text(disp, 'Click on difficulty or create custom', 250, 175, black, 32)
        sb.text(disp, 'If creating custom:', 250, 300, black, 32)
        sb.text(disp, 'Input custom size (integer 1-100):', 150, 350, black, 16)
        sb.text(disp, 'Input custom time limit (0.1-10, 1 decimal):', 172, 400, black, 16)

        # continue when ready
        cont = False
        if color1 == green:
            cont = True
        elif color2 == green:
            cont = True
        elif color3 == green:
            cont = True
        elif color4 == green and color5 == green and color6 == green:
            cont = True
            
        if cont:
            sb.text(disp, 'Click enter to continue...', 192, 450, green, 32)

        # update
        pygame.display.flip()
        cl.tick(30)
        
    # in game
    while inGame == True:

        # increment to keep track of time
        time_count = time_count + 1

        # took too long so YOU LOSE
        if time_count == time*30:
            lose = True
        
        disp.fill(white)

        # when clicked
        if clicked:
            # generate random coordinates for target
            x = random.randint(0, width-tarwidth)
            y = random.randint(50, height-tarheight)

            # keep track of variables
            total_time = total_time + time_count
            clicked = False
            time_count = 0
            clicked_count = clicked_count + 1

            # assign easy levels
            if color1 == green:
                #print('easy')
                if clicked_count >= 0 and clicked_count <=5:
                    tarwidth = 100
                    tarheight = 100
                    time = 0
                    
                elif clicked_count > 5 and clicked_count <= 10:
                    tarwidth = 80
                    tarheight = 80
                    time = 0
                    
                elif clicked_count > 10 and clicked_count <= 15:
                    tarwidth = 80
                    tarheight = 80
                    time = 2
                    
                elif clicked_count > 15 and clicked_count <= 20:
                    tarwidth = 60
                    tarheight = 60
                    time = 2
                    
                elif clicked_count > 20 and clicked_count <= 25:
                    tarwidth = 60
                    tarheight = 60
                    time = 1
                    
                elif clicked_count > 25 and clicked_count <= 30:
                    tarwidth = 50
                    tarheight = 50
                    time = 1
                    
                elif clicked_count > 30 and clicked_count <= 35:
                    tarwidth = 40
                    tarheight = 40
                    time = 1
                    
                elif clicked_count > 35 and clicked_count <= 40:
                    tarwidth = 35
                    tarheight = 35
                    time = 1
                    
                elif clicked_count > 40 and clicked_count <= 45:
                    tarwidth = 30
                    tarheight = 30
                    time = 1
                    
                elif clicked_count > 45 and clicked_count <= 60:
                    tarwidth = 25
                    tarheight = 25
                    time = 1

                elif clicked_count > 60:
                    tarwidth = 20
                    tarheight = 20
                    time = 1
                    
            # assign normal levels
            elif color2 == green:
                #print('normal')
                if clicked_count >= 0 and clicked_count <=5:
                    tarwidth = 100
                    tarheight = 100
                    time = 0
                    
                elif clicked_count > 5 and clicked_count <= 10:
                    tarwidth = 80
                    tarheight = 80
                    time = 0
                    
                elif clicked_count > 10 and clicked_count <= 15:
                    tarwidth = 80
                    tarheight = 80
                    time = 2
                    
                elif clicked_count > 15 and clicked_count <= 20:
                    tarwidth = 60
                    tarheight = 60
                    time = 2
                    
                elif clicked_count > 20 and clicked_count <= 25:
                    tarwidth = 60
                    tarheight = 60
                    time = 1
                    
                elif clicked_count > 25 and clicked_count <= 30:
                    tarwidth = 50
                    tarheight = 50
                    time = 1
                    
                elif clicked_count > 30 and clicked_count <= 35:
                    tarwidth = 40
                    tarheight = 40
                    time = 1
                    
                elif clicked_count > 35 and clicked_count <= 40:
                    tarwidth = 35
                    tarheight = 35
                    time = 1
                    
                elif clicked_count > 40 and clicked_count <= 45:
                    tarwidth = 30
                    tarheight = 30
                    time = 1
                    
                elif clicked_count > 45 and clicked_count <= 50:
                    tarwidth = 25
                    tarheight = 25
                    time = 1
                    
                elif clicked_count > 50 and clicked_count <= 55:
                    tarwidth = 25
                    tarheight = 25
                    time = 0.6
                    
                elif clicked_count > 55 and clicked_count <= 60:
                    tarwidth = 20
                    tarheight = 20
                    time = 0.6
                    
                elif clicked_count > 60 and clicked_count <= 65:
                    tarwidth = 15
                    tarheight = 15
                    time = 0.6
                    
                elif clicked_count > 65 and clicked_count <= 75:
                    tarwidth = 10
                    tarheight = 10
                    time = 0.6
                    
                elif clicked_count > 75 and clicked_count <= 100:
                    tarwidth = 10
                    tarheight = 10
                    time = 0.4

                elif clicked_count > 100:
                    tarwidth = 6
                    tarheight = 6
                    time = 0.4

            # assign hard levels
            elif color3 == green:
                #print('hard')
                if clicked_count >= 0 and clicked_count <= 5:
                    tarwidth = 30
                    tarheight = 30
                    time = 1
                    
                elif clicked_count > 5 and clicked_count <= 10:
                    tarwidth = 25
                    tarheight = 25
                    time = 1
                    
                elif clicked_count > 10 and clicked_count <= 15:
                    tarwidth = 25
                    tarheight = 25
                    time = 0.6
                    
                elif clicked_count > 15 and clicked_count <= 20:
                    tarwidth = 20
                    tarheight = 20
                    time = 0.6
                    
                elif clicked_count > 20 and clicked_count <= 25:
                    tarwidth = 15
                    tarheight = 15
                    time = 0.6
                    
                elif clicked_count > 25 and clicked_count <= 35:
                    tarwidth = 10
                    tarheight = 10
                    time = 0.6
                    
                elif clicked_count > 35 and clicked_count <= 50:
                    tarwidth = 10
                    tarheight = 10
                    time = 0.4

                elif clicked_count > 50:
                    tarwidth = 6
                    tarheight = 6
                    time = 0.4
                    
            # assign custom levels:
            elif color4 == green:
                tarwidth = int(text1)
                tarheight = int(text1)
                time = float(text2)
            
            tar.width = tarwidth
            tar.height = tarheight
            
            #print(str(tar.width) + " " + str(tar.height))
            #print(clicked_count)

        # redraw target
        tar.drawTarget(disp, x, y)
        
        # get inputs
        for event in pygame.event.get():
            
            # exit game
            if event.type == pygame.QUIT:
                pygame.quit()

            # if mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # see if clicked on
                if tar.rect.collidepoint(pos):
                    clicked = True
                    
            # if a key is pressed
            if event.type == pygame.KEYDOWN:
                # escape exits loop (reset)
                if event.key == pygame.K_RETURN:
                    inGame = False
        
        # draw text
        if time == 0:
            sb.text(disp, 'click on the box', 250, 20, black, 20)
        else:
            sb.text(disp, 'click on the box in: ' + f'{(time - time_count/30):.1f}', 250, 20, black, 20)

        # at loss
        while lose:
            # inputs
            for event in pygame.event.get():
                
                # exit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                # key input to break loop
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        lose = False
                        inGame = False

            # draw information
            disp.fill(black)
            sb.text(disp, 'Too Slow :)', 250, 180, red, 48)
            sb.text(disp, 'Average Time to Click: ', 250, 240, yellow, 32)
            sb.text(disp, f'{((total_time/clicked_count)/30):.2f}' + ' seconds', 250, 280, yellow, 32)
            sb.text(disp, 'Total Correct Clicks: ' + str(clicked_count-1), 250, 320, green, 32)
            sb.text(disp, 'Hit Enter to Continue', 250, 450, white, 20)
            pygame.display.flip()

        # update game screen
        pygame.display.flip()
        cl.tick(30)
        
# run stuff
while True:
    run()
# exit
quit()
