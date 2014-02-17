#-------------------------------------------------------------------------------
# Name:        images.py
# Purpose:
#
# Author:      novirael
#
# Created:     17-08-2012
# Copyright:   (c) novirael 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# libraries
import pygame
from pygame.locals import *

# The function wytnij(obrazek, lista, (l,b,w,h), n ) function
#  is cutting sprites from images. It takes:
#  - obrazek as a texture with our sprites,
#  - list as empty list
#  - information where the sprite to cut out exacly is and how to cut it
#     ( l: x position, b: y position, w: with of block. h: height of block )
#  - n as int, number of iteration
# It returns: filled list of our new textures

def wytnij(obrazek, lista, (l,b,w,h), n):
   for i in range(n):
      lista.append(obrazek.subsurface( (l,b+h*i,w,h) ))
   return lista

# This class taking care of all textures in the game.

class GameTextures():
 def __init__(self):

   #######################################
   ############# LOAD IMAGES #############

   src_background0      = 'img/bg3.JPG'
   src_background1      = 'img/bg4.JPG'
   src_background2      = 'img/bg2.JPG'
   src_background_main  = 'img/main.JPG'
   src_background_tour  = 'img/tour.JPG'
   src_background_tour2 = 'img/tour-fight.JPG'
   src_background_dvic  = 'img/wygral mrok.JPG'
   src_background_wvic  = 'img/wygralo swiatlo.JPG'
   src_background_draw  = 'img/remis.JPG'
   src_mapa_mordor      = 'img/mapa_mordor.PNG'
   src_mapa_shire       = 'img/mapa_shire.PNG'
   src_miniatury        = 'img/miniatury.PNG'
   src_opisy_panel      = 'img/opisy.PNG'
   src_opisy_kart       = 'img/opisy-kart.PNG'
   src_zasady_gry       = 'img/zasady-gry.JPG'
   src_about            = 'img/about.JPG'

   ########### END LOAD IMAGES ###########
   #######################################

   #######################################################################
   ########################### CREATE TEXTURES ###########################

   # backgrounds
   self.background_dark = pygame.image.load(src_background0).convert()
   self.background_white = pygame.image.load(src_background1).convert()
   self.background_fight = pygame.image.load(src_background2).convert()
   self.background_main =  pygame.image.load(src_background_main).convert()
   self.background_tour = pygame.image.load(src_background_tour).convert()
   self.background_tour2 = pygame.image.load(src_background_tour2).convert()
   self.background_darkvictory = pygame.image.load(src_background_dvic).convert()
   self.background_whitevictory = pygame.image.load(src_background_wvic).convert()
   self.background_draw = pygame.image.load(src_background_draw).convert()

   # maps
   self.map_dark = pygame.image.load(src_mapa_mordor).convert_alpha()
   self.map_white = pygame.image.load(src_mapa_shire).convert_alpha()

   # others
   self.miniaturki = pygame.image.load(src_miniatury).convert_alpha()
   self.descriptions = pygame.image.load(src_opisy_panel).convert_alpha()
   self.card_descriptions = pygame.image.load(src_opisy_kart).convert_alpha()
   self.rules = pygame.image.load(src_zasady_gry).convert()
   self.about = pygame.image.load(src_about).convert()

   self.miniatury = [[],[],[],[]]

   # 0-8 dark characters
   wytnij(self.miniaturki, self.miniatury[0], (0,0,90,75), 9)
   # 0-8 white characters
   wytnij(self.miniaturki, self.miniatury[1], (180,0,90,75), 9)
   # 0-8 dark cards
   wytnij(self.miniaturki, self.miniatury[2], (360,0,90,75), 9)
   # 0-8 white cards
   wytnij(self.miniaturki, self.miniatury[3], (540,0,90,75), 9)

##   self.miniatury_hi = [[],[],[],[]]
##
##   # 0-8 dark characters and 9-17 hilight dark characters
##   wytnij(self.miniaturki, self.miniatury[0], (90,0,90,75), 9)
##   # 0-8 white characters and 9-17 hilight white characters
##   wytnij(self.miniaturki, self.miniatury[1], (270,0,90,75), 9)
##   # 0-8 dark cards and 9-17 hilight dark cards
##   wytnij(self.miniaturki, self.miniatury[2], (450,0,90,75), 9)
##   # 0-8 white cards and 9-17 hilight white cards
##   wytnij(self.miniaturki, self.miniatury[3], (630,0,90,75), 9)

   self.opisy = [[],[],[],[]]

   # 0-8 dark characters
   wytnij(self.descriptions, self.opisy[0], (250,0,250,350), 9)
   # 0-8 white characters
   wytnij(self.descriptions, self.opisy[1], (0,0,250,350), 9)

   self.opisy_kart = [[],[]]
   # 0-8 dark characters
   wytnij(self.card_descriptions, self.opisy_kart[0], (0,120,310,120), 6)
   wytnij(self.card_descriptions, self.opisy_kart[0], (310,0,310,120), 3)
   # 0-8 white characters
   wytnij(self.card_descriptions, self.opisy_kart[1], (0,120,310,120), 5)
   wytnij(self.card_descriptions, self.opisy_kart[1], (310,360,310,120), 4)

   self.wskazowki = []
   wytnij(self.descriptions, self.wskazowki, (500,0,250,350), 2)
   wytnij(self.card_descriptions, self.wskazowki, (0,0,310,120), 1)

   self.b_nowa_gra = []
   wytnij(self.descriptions, self.b_nowa_gra, (500,700,250,50), 3)

   self.b_powrot_do_gry = []
   wytnij(self.descriptions, self.b_powrot_do_gry, (500,850,250,50), 3)

   self.b_wczytaj_gre = []
   wytnij(self.descriptions, self.b_wczytaj_gre, (500,1000,250,50), 3)

   self.b_zapisz_gre = []
   wytnij(self.descriptions, self.b_zapisz_gre, (500,1150,250,50), 3)

   self.b_zasady_gry = []
   wytnij(self.descriptions, self.b_zasady_gry, (500,1300,250,50), 3)

   self.b_informacje = []
   wytnij(self.descriptions, self.b_informacje, (500,1450,250,50), 3)

   self.b_wyjscie = []
   wytnij(self.descriptions, self.b_wyjscie, (500,1600,250,50), 3)

   self.b_kontynuuj = []
   wytnij(self.descriptions, self.b_kontynuuj, (500,1750,250,50), 3)

   self.b_nowa_tura = []
   wytnij(self.descriptions, self.b_nowa_tura, (500,1900,250,50), 3)

   self.b_cofnij_ruch = []
   wytnij(self.descriptions, self.b_cofnij_ruch, (500,2050,250,50), 3)

   ######################### END CREATE TEXTURES #########################
   #######################################################################

