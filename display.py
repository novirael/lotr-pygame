#-------------------------------------------------------------------------------
# Name:        diplay.py
# Purpose:
#
# Author:      novirael
#
# Created:     24-06-2012
# Copyright:   (c) novirael 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# libraries
import pygame
from pygame.locals import *

from images import GameTextures

# variables
color_topbottom = (51,62,62)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
color_p0 = (60,45,50)
color_p1 = (215,160, 50)

class DrawGameplay():

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""     INIT CLASS     """""""""""""""""""""""""""

   def __init__(self, var):

      # set caption
      pygame.display.set_caption("LotR: Confrontation")

      # create surfaces
      self.screen = pygame.display.set_mode( (900,800) )
      self.rozgrywka = pygame.Surface( (900, 800) )

      self.rside = pygame.Surface( (270, 630) )
      self.rside.set_alpha(130)

      self.mside = pygame.Surface( (270,440) )
      self.mside.set_alpha(130)

      self.bside = pygame.Surface( (620,150) )
      self.bside.set_alpha(170)

      self.tside = pygame.Surface( (250,350) )
      self.tside.set_alpha(150)

      self.white_rectangle = pygame.Surface( (90,75) )
      self.white_rectangle.fill(white)
      self.white_rectangle.set_alpha(130)

      self.small_rect = pygame.Surface( (40,40) )
      self.small_rect.set_alpha(130)
      self.small_rect1 = pygame.Surface( (82,40) )
      self.small_rect1.set_alpha(130)


      self.font = pygame.font.Font("PAPYRUS.ttf", 20)
      self.font1 = pygame.font.Font("PAPYRUS.ttf", 27)
      self.font2 = pygame.font.Font("PAPYRUS.ttf", 24)

      self.warnings = self.font1.render("Uwagi:", True, white)
      self.atakuje = self.font1.render("Atakuje:", True, white)
      self.broni = self.font1.render("Broni sie:", True, white)

      self.tips = self.font2.render("Wskazowki:", True, white)
      self.info = self.font2.render("Informacje:", True, white)

      self.err101 = self.font.render("> Rozstaw wszystkie piony!", True, red )
      self.err102_0 = self.font.render("> Nie mozesz stawiac figur", True, red )
      self.err102_1 = self.font.render("   w gorach i powyzej!", True, red )
      self.err103 = self.font.render("> Stawiasz na krainie wroga!", True, red )
      self.err104 = self.font.render("> Tutaj juz wiecej nie dodam!", True, red )

      self.err201 = self.font.render("> Bedzie konfrontacja!!!", True, green )
      self.err202_0 = self.font.render("> Wybierz przeciwnika!", True, green )
      self.err202_1 = self.font.render("   (Kliknij na piona)", True, green )
      self.err203 = self.font.render("> Wybrano przeciwnika.", True, green )
      self.err204_0 = self.font.render("> Cos krecisz! Nie mozesz", True, red )
      self.err204_1 = self.font.render("    sie tak ruszyc!", True, red )
      self.err205 = self.font.render("> Chcesz ominac kolejke?", True, red )

      self.err301 = self.font.render("> Ta bitwa jest z gory przesadzona!", True, green )
      self.err302 = self.font.render("> Musisz wybrac jedna swoja karte.", True, red )
      self.err303 = self.font.render("> Twoja karta zostala wybrana.", True, green )

      self.end = self.font.render("> Mozesz zakonczyc ture.", True, green)

##      self.rectangle = pygame.Surface( (180,80) )
##      self.rectangle.set_alpha(150)
##
##      self.srectangle = pygame.Surface( (150,80) )
##      self.srectangle.fill((255,0,0))
##      self.srectangle.set_alpha(150)

      self.var = var
      self.tex = GameTextures()


   """""""""""""""""""""""""""  END INIT CLASS  """""""""""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""     MENU SCREEN    """""""""""""""""""""""""""

   def menu_screen(self):         ### MENU SCREEN ###

      # blit background and menu bar
      self.screen.blit(self.tex.background_main, (0,0))
      self.screen.blit(self.mside, (600,300))

      # blit hightlighted new game button if the mouse pointer
      #    is on it else blit new game button
      if self.var.mouse_on_new_game_button:
         self.screen.blit(self.tex.b_nowa_gra[1], (610,320))
      else:
         self.screen.blit(self.tex.b_nowa_gra[0], (610,320))

      # if it is fresh open
      if self.var.last_mode != "MAIN MENU":
         # blit hightlighted return button if the mouse pointer
         #    is on it else blit return button
         if self.var.mouse_on_return_button:
            self.screen.blit(self.tex.b_powrot_do_gry[1], (610,380))
         else:
            self.screen.blit(self.tex.b_powrot_do_gry[0], (610,380))
      else:
         self.screen.blit(self.tex.b_powrot_do_gry[2], (610,380))

      # if load is possible
      if self.var.saved:
         # blit hightlighted load game button if the mouse pointer
         #    is on it else blit load game button
         if self.var.mouse_on_load_game_button:
            self.screen.blit(self.tex.b_wczytaj_gre[1], (610,440))
         else:
            self.screen.blit(self.tex.b_wczytaj_gre[0], (610,440))
      else:
         self.screen.blit(self.tex.b_wczytaj_gre[2], (610,440))

      # if it is fresh open
      if self.var.last_mode != "MAIN MENU":
         # blit hightlighted save game button if the mouse pointer
         #    is on it else blit save game button
         if self.var.mouse_on_save_game_button:
            self.screen.blit(self.tex.b_zapisz_gre[1], (610,500))
         else:
            self.screen.blit(self.tex.b_zapisz_gre[0], (610,500))
      else:
         self.screen.blit(self.tex.b_zapisz_gre[2], (610,500))

      # blit hightlighted game rules button if the mouse pointer
      #    is on it else blit game rules button
      if self.var.mouse_on_game_rules_button:
         self.screen.blit(self.tex.b_zasady_gry[1], (610,560))
      else:
         self.screen.blit(self.tex.b_zasady_gry[0], (610,560))

      # blit hightlighted about button if the mouse pointer
      #    is on it else blit about button
      if self.var.mouse_on_about_button:
         self.screen.blit(self.tex.b_informacje[1], (610,620))
      else:
         self.screen.blit(self.tex.b_informacje[0], (610,620))

      # blit hightlighted quit button if the mouse pointer
      #    is on it else blit quit button
      if self.var.mouse_on_quit_button:
         self.screen.blit(self.tex.b_wyjscie[1], (610,680))
      else:
         self.screen.blit(self.tex.b_wyjscie[0], (610,680))


   """""""""""""""""""""""""""  END MENU SCREEN """""""""""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""    ABOUT SCREEN    """""""""""""""""""""""""""

   def about_screen(self):
      self.screen.blit(self.tex.about, (0,0))
      back = self.font1.render("Powrot", True, white)
      self.screen.blit(back, (750,720))


   """"""""""""""""""""""""""" END ABOUT SCREEN """""""""""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""    RULES SCREEN    """""""""""""""""""""""""""

   def rules_screen(self):
      self.screen.blit(self.tex.rules, (0, -800 * self.var.sheet))

      self.screen.blit(self.small_rect, (850, 10) )
      up = self.font.render("UP", True, white)
      self.screen.blit(up, (852,15))

      self.screen.blit(self.small_rect, (850,750) )
      down = self.font.render("DO", True, white)
      self.screen.blit(down, (849,755))

      self.screen.blit(self.small_rect1, (760, 750) )
      back = self.font1.render("Powrot", True, white)
      self.screen.blit(back, (760,750))


   """"""""""""""""""""""""""" END RULES SCREEN """""""""""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """""""""""""""""""""""""""    TOUR SCREEN   """""""""""""""""""""""""""

   def tour_screen(self):      ### TOUR SCREEN ###

      # blit background
      if self.var.mode == "TOUR MAP":
         self.screen.blit(self.tex.background_tour, (0,0))
      else:
         self.screen.blit(self.tex.background_tour2, (0,0))

      # blit hightlighted continue button if the mouse pointer
      #    is on it else blit continue button
      if self.var.mouse_on_continue_button:
         self.screen.blit(self.tex.b_kontynuuj[1], (300,640))
      else:
         self.screen.blit(self.tex.b_kontynuuj[0], (300,640))


   """""""""""""""""""""""""""  END TOUR SCREEN """""""""""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """""""""""""""""""""""""""  VOCTORY SCREEN  """""""""""""""""""""""""""

   def victory_screen(self):
      # blit background
      if self.var.mode == "DARK VICTORY":
         self.screen.blit(self.tex.background_darkvictory, (0,0))
      elif self.var.mode == "WHITE VICTORY":
         self.screen.blit(self.tex.background_whitevictory, (0,0))
      else:
         self.screen.blit(self.tex.background_draw, (0,0))

      # blit hightlighted continue button if the mouse pointer
      #    is on it else blit continue button
      if self.var.mouse_on_continue_button:
         self.screen.blit(self.tex.b_kontynuuj[1], (300,640))
      else:
         self.screen.blit(self.tex.b_kontynuuj[0], (300,640))


   """""""""""""""""""""""  END VICTORY SCREEN  """""""""""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """""""""""""""""""""""""""    MAP SCREEN    """""""""""""""""""""""""""

   def map_screen(self):          ### MAP SCREEN ###
      # stuff is printing on rozgrywka surface only,
      #    when user is ready after player's exchange
      if self.var.ready or self.var.loaded:
         self.still_stuff()
         self.var.ready = False
         self.var.loaded = False

      # blit still stuff
      self.screen.blit(self.rozgrywka, (0,0))

      # blit hightlighted next torur button if the mouse pointer
      #    is on it else blit next tour button
      if self.var.mouse_on_tour_button:
         self.screen.blit(self.tex.b_nowa_tura[1], (640,595))
      else:
         self.screen.blit(self.tex.b_nowa_tura[0], (640,595))


      # blit hightlighted reset button if the mouse pointer
      #    is on it else blit reset button
      if self.var.live != self.var.live_backup:
         if self.var.mouse_on_reset_button:
            self.screen.blit(self.tex.b_cofnij_ruch[1], (640,645))
         else:
            self.screen.blit(self.tex.b_cofnij_ruch[0], (640,645))
      else:
         self.screen.blit(self.tex.b_cofnij_ruch[2], (640,645))

      # if any picture was selected draw selection
      if self.var.selected:
         self.selection()

      # if picture was selected or mouse pointer is on it blit information
      if self.var.mouse_on_picture or self.var.mouse_on_pawn or self.var.selected:
         if self.var.sel_black_char_no > -1:
            self.screen.blit(self.tex.opisy[0][self.var.sel_black_char_no], (640,95))
         elif self.var.sel_white_char_no > -1:
            self.screen.blit(self.tex.opisy[1][self.var.sel_white_char_no], (640,95))
      else:
         if self.var.mode == "MAP POSITIONING":
            self.screen.blit(self.tex.wskazowki[0], (640,95))
         elif self.var.mode == "MAP GAMEPLAY":
            self.screen.blit(self.tex.wskazowki[1], (640,95))

      # if there is errors on error list print it!
      if len(self.var.errors) > 0:
         self.screen.blit(self.warnings, (725,450))
         if 101 in self.var.errors and 102 in self.var.errors:
            self.screen.blit(self.err101, (645,490))
            self.screen.blit(self.err102_0, (645,515))
            self.screen.blit(self.err102_1, (645,540))
         elif 101 in self.var.errors and 104 in self.var.errors:
            self.screen.blit(self.err101, (645,490))
            self.screen.blit(self.err104, (645,515))
         elif 101 in self.var.errors and 103 in self.var.errors:
            self.screen.blit(self.err101, (645,490))
            self.screen.blit(self.err103, (645,515))
         elif 101 in self.var.errors:
            self.screen.blit(self.err101, (645,490))
         elif 102 in self.var.errors:
            self.screen.blit(self.err102_0, (645,490))
            self.screen.blit(self.err102_1, (645,515))
         elif 103 in self.var.errors:
            self.screen.blit(self.err103, (645,490))
         elif 104 in self.var.errors:
            self.screen.blit(self.err104, (645,490))
         elif 204 in self.var.errors:
            self.screen.blit(self.err204_0, (645,490))
            self.screen.blit(self.err204_1, (645,515))
         elif 201 in self.var.errors and 202 in self.var.errors:
            self.screen.blit(self.err201, (645,490))
            self.screen.blit(self.err202_0, (645,515))
            self.screen.blit(self.err202_1, (645,540))
         elif 201 in self.var.errors and 203 in self.var.errors:
            self.screen.blit(self.err201, (645,490))
            self.screen.blit(self.err203, (645,515))
            self.screen.blit(self.end, (645,540))
         elif 205 in self.var.errors:
            self.screen.blit(self.err205, (645,490))
            self.screen.blit(self.end, (645,515))

      # if pawn was raised print shandow under mouse pointer
      if self.var.raised_pawn:
         if self.var.player == 0:
            pygame.draw.circle(self.screen, color_p0, (self.var.x - 4, self.var.y - 4), 8)
         else:
            pygame.draw.circle(self.screen, color_p1, (self.var.x - 4, self.var.y - 4), 8)


      if self.var.player == 0:
         # print black pawns on map
         for i in range(len(self.var.live)):
            pos = self.var.live[i][3]
            if pos != (0,0):
               pygame.draw.circle(self.screen, color_p0, pos, 8)

         # print white pawns on map
         for i in range(len(self.var.w_live)):
            pos = self.var.w_live[i][3]
            if pos != (0,0):
               pygame.draw.circle(self.screen, color_p1, pos, 8)

      else:
         # print black pawns on map
         for i in range(len(self.var.b_live)):
            pos = self.var.b_live[i][3]
            if pos != (0,0):
               pygame.draw.circle(self.screen, color_p0, pos, 8)

         # print white pawns on map
         for i in range(len(self.var.live)):
            pos = self.var.w_live[i][3]
            if pos != (0,0):
               pygame.draw.circle(self.screen, color_p1, pos, 8)


      # print short name on map
      for i in range(len(self.var.live)):
         pos = self.var.live[i][3]
         if pos != (0,0):
            pos = self.var.live[i][3]
            s1 = self.var.live[i][1][0]
            s2 = self.var.live[i][1][1:3]
            sign = s1.upper() + s2
            s = self.font.render(sign, True, white)
            self.screen.blit(s, pos)


   """""""""""""""""""""""""""  END MAP SCREEN  """""""""""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """""""""""""""""""""     CONFRONTATION SCREEN     """""""""""""""""""""

   def confrontation_screen(self):

      # stuff is printing on rozgrywka surface only,
      #    when user is ready after player's exchange
      if self.var.ready or self.var.loaded:
         self.still_stuff()
         self.var.ready = False

      # blit still stuff and rside on the screen
      self.screen.blit(self.rozgrywka, (0,0))

      # blit hightlighted next torur button if the mouse pointer
      #    is on it else blit next tour button
      if self.var.mouse_on_tour_button:
         self.screen.blit(self.tex.b_nowa_tura[1], (325,660))
      else:
         self.screen.blit(self.tex.b_nowa_tura[0], (325,660))

      # if any picture was selected draw selection
      if self.var.selected:
         self.selection()

      # if picture was selected or mouse pointer is on it blit information
      if self.var.mouse_on_picture or self.var.selected:
         if self.var.sel_black_char_no > -1:
            self.screen.blit(self.tex.opisy_kart[0][self.var.sel_black_char_no], (450,525))
         elif self.var.sel_white_char_no > -1:
            self.screen.blit(self.tex.opisy_kart[1][self.var.sel_white_char_no], (450,525))
      else:
            self.screen.blit(self.tex.wskazowki[2], (450,525))

      # if there is errors on error list print it!
      if len(self.var.errors) > 0:
         if 301 in self.var.errors:
            self.screen.blit(self.err301, (145,535))
            self.screen.blit(self.end, (145,560))
         elif 302 in self.var.errors:
            self.screen.blit(self.err302, (145,535))
         elif 303 in self.var.errors:
            nr = str(self.var.sel_char_id + 1)
            self.screen.blit(self.err303, (145,535))
            self.screen.blit(self.end, (145,560))


   """""""""""""""""""""   END CONFRONTATION SCREEN   """""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

##      ##### TESTS #####
##
##      # w = 180
##      self.draw_rect(225,120) # mordor
##      self.draw_rect(135,200) # dagorlad
##      self.draw_rect(315,200) # gondor
##      self.draw_rect(45,280)  # mroczna puszcza
##      self.draw_rect(225,280) # fangorn
##      self.draw_rect(405,280) # rohan
##      # w = 150
##      self.draw_srect(5,360) # wysoka przelecz
##      self.draw_srect(155,360) # gory mgliste
##      self.draw_srect(305,360) # moria
##      self.draw_srect(455,360) # wrota rohanu
##      # w = 180
##      self.draw_rect(405,440) # enedwaith
##      self.draw_rect(225,440) # eregion
##      self.draw_rect(45,440)  # rhudaur
##      self.draw_rect(315,520) # cardolan
##      self.draw_rect(135,520) # arthedain
##      self.draw_rect(225,600) # shire
##
##      ### END TESTS ###
##
##   def draw_rect(self, x, y):
##      self.screen.blit(self.rectangle, (x, y))
##   def draw_srect(self, x, y):
##      self.screen.blit(self.srectangle, (x, y))


   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""" PRINT STILL STUFF ON SURFACE """""""""""""""""""""

   def still_stuff(self):

      # draw rectlanges on top and bottom
      pygame.draw.rect(self.rozgrywka, color_topbottom, Rect(0,  0,900,85))
      pygame.draw.rect(self.rozgrywka, color_topbottom, Rect(0,715,900,85))

      if self.var.mode == "MAP POSITIONING" or self.var.mode == "MAP GAMEPLAY":

         if self.var.player == 0:              # dark player mode

            # blit background and map
            self.rozgrywka.blit( self.tex.background_dark, (0,85) )
            self.rozgrywka.blit( self.tex.map_dark, (0,85) )

            # blit white characters thumbnails (at the top)
            for i in range(9):
               self.rozgrywka.blit( self.tex.miniatury[1][i], (5 + 10*i + 90*i, 5))

            # blit black characters thumbnails (at the bottom)
            for i in range(9):
               self.rozgrywka.blit( self.tex.miniatury[0][i], (5 + 10*i + 90*i, 720))

            # blit white rectangle on the thumbnails of dead white character (at the top)
            for char in self.var.w_dead:
               id = char[0]
               self.rozgrywka.blit( self.white_rectangle, (5 + 10*id + 90*id, 5))

            # blit white rectangle on the thumbnails of dead black character (at the bottom)
            for char in self.var.b_dead:
               id = char[0]
               self.rozgrywka.blit( self.white_rectangle, (5 + 10*id + 90*id, 720))

         else:                                # white player mode

            # blit background and map
            self.rozgrywka.blit( self.tex.background_white, (0,85) )
            self.rozgrywka.blit( self.tex.map_white, (0,85) )

            # blit black characters thumbnails (at the top)
            for i in range(9):
               self.rozgrywka.blit( self.tex.miniatury[0][i], (5 + 10*i + 90*i, 5))

            # blit white characters thumbnails (at the bottom)
            for i in range(9):
               self.rozgrywka.blit( self.tex.miniatury[1][i], (5 + 10*i + 90*i, 720))

           # blit white rectangle on the thumbnails of dead black character (at the top)
            for char in self.var.b_dead:
               id = char[0]
               self.rozgrywka.blit( self.white_rectangle, (5 + 10*id + 90*id, 5))

            # blit white rectangle on the thumbnails of dead white character (at the bottom)
            for char in self.var.w_dead:
               id = char[0]
               self.rozgrywka.blit( self.white_rectangle, (5 + 10*id + 90*id, 720))

         # print baner on right side
         self.rozgrywka.blit(self.rside, (630,85))

      else:

         if self.var.player == 0:              # dark player mode

            # blit background
            self.rozgrywka.blit( self.tex.background_fight, (0,85) )

            # blit white cards thumbnails (at the top)
            for i in range(9):
               self.rozgrywka.blit( self.tex.miniatury[3][i], (5 + 10*i + 90*i, 5))

            # blit black cards thumbnails (at the bottom)
            for i in range(9):
               self.rozgrywka.blit( self.tex.miniatury[2][i], (5 + 10*i + 90*i, 720))

            # blit white rectangle on the thumbnails of wasted white cards (at the top)
            for card in self.var.w_wasted_cards:
               id = card[0]
               self.rozgrywka.blit( self.white_rectangle, (5 + 10*id + 90*id, 5))

            # blit white rectangle on the thumbnails of wasted black cards (at the bottom)
            for card in self.var.b_wasted_cards:
               id = card[0]
               self.rozgrywka.blit( self.white_rectangle, (5 + 10*id + 90*id, 720))

         else:                                # white player mode

            # blit background
            self.rozgrywka.blit( self.tex.background_fight, (0,85) )

            # blit black cards thumbnails (at the top)
            for i in range(9):
               self.rozgrywka.blit( self.tex.miniatury[2][i], (5 + 10*i + 90*i, 5))

            # blit white cards thumbnails (at the bottom)
            for i in range(9):
               self.rozgrywka.blit( self.tex.miniatury[3][i], (5 + 10*i + 90*i, 720))

            # blit white rectangle on the thumbnails of wasted black cards s (at the top)
            for card in self.var.b_wasted_cards:
               id = card[0]
               self.rozgrywka.blit( self.white_rectangle, (5 + 10*id + 90*id, 5))

            # blit white rectangle on the thumbnails of wasted white cards  (at the bottom)
            for card in self.var.w_wasted_cards:
               id = card[0]
               self.rozgrywka.blit( self.white_rectangle, (5 + 10*id + 90*id, 720))

         # print baner on top side
         self.rozgrywka.blit(self.tside, (140,130))
         self.rozgrywka.blit(self.tside, (510,130))

         # print character wchih attack information
         self.rozgrywka.blit(self.atakuje, (140,95))
         no = self.var.who[-2][0]
         player = int(self.var.who[-2][1][-1])
         self.rozgrywka.blit(self.tex.opisy[player][no], (140,130))

         # print character wchih defense information
         self.rozgrywka.blit(self.broni, (510,95))
         no = self.var.who[-1][0]
         player = int(self.var.who[-1][1][-1])
         self.rozgrywka.blit(self.tex.opisy[player][no], (510,130))

         # print baner on bottom side
         self.rozgrywka.blit(self.bside, (140,500))
         self.rozgrywka.blit(self.info, (235,500))
         self.rozgrywka.blit(self.tips, (550,500))
         pygame.draw.rect(self.rozgrywka, (200,200,200), (449,515,2,120))


   """""""""""""""""""""   END OF PRINT STILL THINGS  """""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   def selection(self):
      x_dark  = 5 + 10* self.var.sel_black_char_no + 90 * self.var.sel_black_char_no
      x_white = 5 + 10* self.var.sel_white_char_no  + 90 * self.var.sel_white_char_no
      if self.var.player == 0:              # dark player mode
         if self.var.sel_black_char_no > -1:
            pygame.draw.circle(self.screen, white, (x_dark, 795), 4)
         elif self.var.sel_white_char_no > -1:
            pygame.draw.circle(self.screen, white, (x_white,  5), 4)
      else:                                 # white player mode
         if self.var.sel_black_char_no > -1:
            pygame.draw.circle(self.screen, white, (x_dark,   5), 4)
         elif self.var.sel_white_char_no > -1:
            pygame.draw.circle(self.screen, white, (x_white, 795), 4)


   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """""""""    THIS IS MAIN FUNCTION IN DRAWDISPLAY FUNCTION     """""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   def things(self):

      mode = self.var.mode

      if mode == "MAIN MENU":
         self.menu_screen()
      elif mode == "GAME RULES":
         self.rules_screen()
      elif mode == "ABOUT":
         self.about_screen()
      elif mode == "TOUR MAP" or mode == "TOUR FIGHT":
         self.tour_screen()
      elif mode == "DARK VICTORY" or mode == "WHITE VICTORY" or mode == "DRAW":
         self.victory_screen()
      elif mode == "MAP POSITIONING" or mode == "MAP GAMEPLAY":
         self.map_screen()
      elif mode == "FIGHT":
         self.confrontation_screen()


   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """""""""""""""""""""     END OF MAIN FUNCTION     """""""""""""""""""""
   """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
