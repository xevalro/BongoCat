from pygame import *
import pygame as pg
from threading import *
import threading
from time import *
import time

pg.init()

# Screen Settings

bgColor = (255, 255, 255)
screen = pg.display.set_mode((640, 360))
screen.fill(bgColor)
pg.display.set_caption("Bongo Cat (pygame)")
icon = pg.image.load("bongocatIcon.png").convert_alpha()
pg.display.set_icon(icon)
running = True

# Variables

origin = (0, 0)
scrnSize = (640, 360)
blink = 1
leftHand = 1
rightHand = 1
settingToggle = 0

# Images

baseImg = pg.image.load("Base.png").convert_alpha()
table = pg.image.load("Table.png").convert_alpha()
eyesOpen = pg.image.load("eyesOpen.png").convert_alpha()
eyesClosed = pg.image.load("eyesClosed.png").convert_alpha()
handUpLeft = pg.image.load("handUpLeft.png").convert_alpha()
handUpRight = pg.image.load("handUpRight.png").convert_alpha()
mouth = pg.image.load("U.png").convert_alpha()
handDownLeft = pg.image.load("handDownLeft.png").convert_alpha()
handDownRight = pg.image.load("handDownRight.png").convert_alpha()
checked = pg.image.load("checked.png").convert_alpha()
unchecked = pg.image.load("unchecked.png").convert_alpha()

# Functions

def blinkTick():
    print("Thread BlinkTick Running")
    global blink
    while True:
        blink = 1
        time.sleep(0.5)
        blink = 0
        time.sleep(3.5)

def keyCheck():
    print("keyCheck thread running")
    global leftHand, rightHand, settingToggle
    while True:
        keys=pg.key.get_pressed()
        if keys[pg.K_d]:
            leftHand = 0
        else:
            leftHand = 1

        if keys[pg.K_a]:
            rightHand = 0
        else:
            rightHand = 1

        for event in pg.event.get() :
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_ESCAPE :
                    if settingToggle == 0:
                        settingToggle = 1
                    else:
                        settingToggle = 0

# Threads 

blinkThread = Thread(target=blinkTick)
keyCheckThread = Thread(target=keyCheck)


blinkThread.start()
keyCheckThread.start()

# Start

while running:

    screen.fill(bgColor) #erases old sprites

    if settingToggle == 0:

        screen.blit(baseImg, origin)
        screen.blit(table, origin)

        # Eyes Blinking

        if blink == 0:
            screen.blit(eyesOpen, origin)
        else:
            screen.blit(eyesClosed, origin)

        # Hand Movement

        if leftHand == 0:
            screen.blit(handDownLeft, origin)
        else:
            screen.blit(handUpLeft, origin)
        
        if rightHand == 0:
            screen.blit(handDownRight, origin)
        else:
            screen.blit(handUpRight, origin)

        # mouth

        # if rightHand == 0 and leftHand == 0:
        # screen.blit(mouth, origin)

    else:
        pass

    pg.display.flip() #Updates screen
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos