from pygame import *
import pygame as pg
from threading import *
import threading
from time import *
import time
import os

def load_file(file_name: str) -> str:
        return os.path.join(os.path.dirname(__file__), file_name)

pg.init()

# Screen Settings

bgColor = (255, 255, 255)
screen = pg.display.set_mode((640, 360))
screen.fill(bgColor)
pg.display.set_caption("Bongo Cat (pygame)")
icon = pg.image.load(load_file("textures/bongocatIcon.png")).convert_alpha()
pg.display.set_icon(icon)
running = True

# Variables

origin = (0, 0)
scrnSize = (640, 360)
blink = 1
leftHand = 1
rightHand = 1

# Images

baseImg = pg.image.load(load_file("textures/Base.png")).convert_alpha()
table = pg.image.load(load_file("textures/Table.png")).convert_alpha()
eyesOpen = pg.image.load(load_file("textures/eyesOpen.png")).convert_alpha()
eyesClosed = pg.image.load(load_file("textures/eyesClosed.png")).convert_alpha()
handUpLeft = pg.image.load(load_file("textures/handUpLeft.png")).convert_alpha()
handUpRight = pg.image.load(load_file("textures/handUpRight.png")).convert_alpha()
mouth = pg.image.load(load_file("textures/U.png")).convert_alpha()
handDownLeft = pg.image.load(load_file("textures/handDownLeft.png")).convert_alpha()
handDownRight = pg.image.load(load_file("textures/handDownRight.png")).convert_alpha()

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
    global leftHand
    global rightHand
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
                

# Threads 

blinkThread = Thread(target=blinkTick)
keyCheckThread = Thread(target=keyCheck)
blinkThread.setDaemon(True)
keyCheckThread.setDaemon(True)

blinkThread.start()
keyCheckThread.start()

# Start

while running:

    screen.fill(bgColor) #erases old sprites
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

#    if rightHand == 0 and leftHand == 0:
#        screen.blit(mouth, origin)

    pg.display.flip() #Updates screen
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
