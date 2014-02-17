#-------------------------------------------------------------------------------
# Name:        LotR: Confrontation
# Purpose:
#
# Author:      Rafal Nowicki
#
# Created:     10-06-2012
# Copyright:   (c) novirael 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# libraries
import pygame
import pickle
from pygame.locals import *

from display import DrawGameplay
from events import Events
from variables import MainVariables
from logic import Logic

# pygame init
pygame.init()

clock = pygame.time.Clock()

var = MainVariables()
draw = DrawGameplay(var)
events = Events(var)
logic = Logic(var)

# try open save
try:
   pickle.load(open('save'))
   var.saved = True
except:
   var.saved = False

# main loop
while True:
   clock.tick(15)

   events.get()
   logic.game()
   draw.things()
   #print var.errors
   pygame.display.update()

