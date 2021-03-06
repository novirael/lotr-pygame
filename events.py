#-------------------------------------------------------------------------------
# Name:        events.py
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
import pickle
import copy
from pygame.locals import *

class Events():

   def __init__(self, var):
      self.var = var
      self.crtl_pressed = False

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""   Inteligent positioning    """"""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   # function takes care all pawns is on right position on the map
   def inteligent_positioning(self, land_name):

      # get pos and size of land
      x, y, w, h = self.var.land[land_name]

      # depends of number pawns on land position it

      if len(self.var.pawns_qu[land_name]) == 1:
         A = ( x + w/2, y + h/2 )
         self.insert(land_name, [A])

      elif len(self.var.pawns_qu[land_name]) == 2:
         A = ( x + w/3,   y + h/2 )
         B = ( x + w*2/3, y + h/2 )
         self.insert(land_name, [A, B])

      elif len(self.var.pawns_qu[land_name]) == 3:
         A = ( x + w/2,   y + h*2/3 )
         B = ( x + w/4,   y + h/3   )
         C = ( x + w*3/4, y + h/3   )
         self.insert(land_name, [A, B, C])

      elif len(self.var.pawns_qu[land_name]) == 4:
         A = ( x + w/5,   y + h/4   )
         B = ( x + w*4/5, y + h/4   )
         C = ( x + w*2/5, y + h*3/4 )
         D = ( x + w*3/5, y + h*3/4 )
         self.insert(land_name, [A, B, C, D])


   # function checks, is raised pawn was somewhere on map,
   # if yes then delete last position
   def quantum(self):
      for i in range(len(self.var.live)):
         if self.var.live[i][0] == self.var.sel_char_id:
            if self.var.live[i][2] != "none":
               if self.var.live[i][1] in self.var.pawns_qu[self.var.live[i][2]]:
                  self.var.pawns_qu[self.var.live[i][2]].remove(self.var.live[i][1])


   # function saves pawn position and name of land on map by character id
   def insert(self, land_name, pos):
      for i in range(len(self.var.live)):
         for j in range(len(self.var.pawns_qu[land_name])):
            if self.var.live[i][1] == self.var.pawns_qu[land_name][j]:
               self.var.live[i][2] = land_name
               self.var.live[i][3] = pos[j]


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""    End of inteligent positioning     """""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """""" This functions check if mouse pointer is on the current items """"""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   # function checks location of mouse pointer on given rectangle
   def rec_area(self, (x,y,w,h)):
      if self.x > x and self.x < x + w:
         if self.y > y and self.y < y + h:
            return True
      return False

   def on_pictures(self):

      for i in range(9):
         if self.x > 5 + 10*i + 90*i and self.x < 5 + 10*i + 90*i + 90:

            if self.y > 5 and self.y < 80:
               if self.var.player == 0:
                  self.var.sel_white_char_no = i
                  self.var.sel_black_char_no = -1
               else:
                  self.var.sel_black_char_no = i
                  self.var.sel_white_char_no = -1
               return True

            elif self.y > 720 and self.y < 795:
               if self.var.player == 0:
                  self.var.sel_black_char_no = i
                  self.var.sel_white_char_no = -1
               else:
                  self.var.sel_white_char_no = i
                  self.var.sel_black_char_no = -1
               return True

      return False


   def on_button(self, name):
      return self.rec_area(self.var.buttons[name])

   def on_area(self, name):
      return self.rec_area(self.var.areas[name])

   def in_land(self, name):
      return self.rec_area(self.var.land[name])

   def on_pawn(self):
      for i in range(len(self.var.live)):
         if self.var.live[i][3] != (0,0):
            x, y = self.var.live[i][3]
            if self.rec_area( (x-8, y-8, 16, 16) ):
               if self.var.player == 0:
                  self.var.sel_black_char_no = i
               else:
                  self.var.sel_white_char_no = i
               return True
      return False


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""   End of verifications   """""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""   Possible pawn movement    """"""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   # function checks if there is enemy on current land
   def enemy_on(self, land_name):
      if self.var.player == 0:
         for i in range(len(self.var.w_live)):
            if self.var.w_live[i][2] == land_name:
               return True
      else:
         for i in range(len(self.var.b_live)):
            if self.var.b_live[i][2] == land_name:
               return True
      return False

   # function checks pawn possible move
   def possible_move(self, land_name, pawns_qu):

      if 104 in self.var.errors:
         self.var.errors.remove(104)
      if 204 in self.var.errors:
         self.var.errors.remove(204)

      # check if on land is any enemy
      if self.enemy_on(land_name):

         if self.var.mode == "MAP POSITIONING":

            # add to error list eror 103
            if not 103 in self.var.errors:
               self.var.errors.append(103)
               if 104 in self.var.errors:
                  self.var.errors.remove(104)
         else:

            # insert current char to current land and his new position
            self.var.pawns_qu[land_name].append(self.var.live[self.var.sel_char_id][1])
            for i in range(len(self.var.live)):
               if self.var.live[i][1] == self.var.live[self.var.sel_char_id][1]:
                  self.var.live[i][2] = land_name
                  x, y, w, h = self.var.land[land_name]
                  x = x + w/2
                  y = y + h/2
                  self.var.live[i][3] = (x,y)

            self.var.check_confrontation = True

      # if not do your job
      else:

         # there is no confrontation anymore
         self.var.check_confrontation = False
         self.var.where = "none"
         self.var.who = []

         # on mountains can stay max 1 pawn
         if land_name == "wysoka przelecz" or land_name =="gory mgliste" or land_name == "moria" or land_name =="wrota rohanu":
            if pawns_qu == 0:
               self.var.pawns_qu[land_name].append(self.var.live[self.var.sel_char_id][1])
               self.inteligent_positioning(land_name)
               #print 'dodalem ' + str(self.var.live[self.var.sel_char_id][1]) + ' do ' + land_name
            else:
               # add to error list eror 104
               if not 104 in self.var.errors:
                  self.var.errors.append(104)
                  if 103 in self.var.errors:
                     self.var.errors.remove(103)
               #print 'nie moge wiecej dodac do ' + land_name

          # on mordor or shire can stay max 4 pawns
         elif land_name == "mordor" or land_name == "shire":
            if pawns_qu <= 3:
               self.var.pawns_qu[land_name].append(self.var.live[self.var.sel_char_id][1])
               self.inteligent_positioning(land_name)
               #print 'dodalem ' + str(self.var.live[self.var.sel_char_id][1]) + ' do ' + land_name
            else:
               # add to error list eror 104
               if not 104 in self.var.errors:
                  self.var.errors.append(104)
                  if 103 in self.var.errors:
                     self.var.errors.remove(103)
               #print 'nie moge wiecej dodac do ' + land_name

         # on the other lands can stay max 2 pawns
         else:
            if pawns_qu == 0 or pawns_qu == 1:
               self.var.pawns_qu[land_name].append(self.var.live[self.var.sel_char_id][1])
               self.inteligent_positioning(land_name)
               #print 'dodalem ' + str(self.var.live[self.var.sel_char_id][1]) + ' do ' + land_name
            else:
               # add to error list eror 104
               if not 104 in self.var.errors:
                  self.var.errors.append(104)
                  if 103 in self.var.errors:
                     self.var.errors.remove(103)
               #print 'nie moge wiecej dodac do ' + land_name

         if not 104 in self.var.errors:
         # remove from error list eror 201 (bedzie konfrontacja)
            if 201 in self.var.errors:
               self.var.errors.remove(201)
            # remove from error list eror 202 (wybierz przeciwnika)
            if 202 in self.var.errors:
               self.var.errors.remove(202)
            # remove from error list eror 203 (wybrano przeciwnika)
            if 203 in self.var.errors:
               self.var.errors.remove(203)
         # remove from error list eror 104 (stawiasz wiecej niz mozesz) if is confrontation
         if 201 in self.var.errors:
            if 104 in self.var.errors:
               self.var.errors.remove(104)


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""   End of pawn's movement    """"""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""     This is the main function in Events class     """"""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   # main function in Events class
   def get(self):

      for event in pygame.event.get():

         if event.type == QUIT:
            self.quit()

         """"""""""""""""""""""""""""     KEYDOWN     """""""""""""""""""""""""""
         if event.type == KEYUP or event.type == KEYDOWN:  # CHECK KEYBOARD #
            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_ESCAPE]:
               if self.var.mode == "MAIN MENU" or self.var.mode == "ABOUT" or self.var.mode == "GAME RULES":
                  self.var.mode = self.var.last_mode
               else:
                  self.var.last_mode = self.var.mode
                  self.var.mode = "MAIN MENU"

            if event.key == K_LCTRL or event.key == K_RCTRL:
               if self.var.mouse_on_picture:
                  if self.on_area("bottom bar"):
                     self.crtl_pressed = True

         """"""""""""""""""""""""""""   END KEYDOWN   """""""""""""""""""""""""""

         """"""""""""""""""""""""""""   MOUSEMOTION   """""""""""""""""""""""""""
         if event.type == MOUSEMOTION:                   # CHECK MOUSE MOVE #
            # get mouse x,y
            self.x, self.y = pygame.mouse.get_pos()

            if self.var.mode == "MAIN MENU":
               # check if mouse is in menu area, then if mouse is on buttons
               if self.on_area("menu"):
                  self.var.mouse_on_new_game_button   = self.on_button("new game")
                  self.var.mouse_on_return_button     = self.on_button("return")
                  self.var.mouse_on_load_game_button  = self.on_button("load game")
                  self.var.mouse_on_save_game_button  = self.on_button("save game")
                  self.var.mouse_on_game_rules_button = self.on_button("game rules")
                  self.var.mouse_on_about_button      = self.on_button("about")
                  self.var.mouse_on_quit_button       = self.on_button("quit")


            elif self.var.mode == "MAP POSITIONING" or self.var.mode == "MAP GAMEPLAY":

               # check if mouse is on pictures
               if self.on_area("top bar") or self.on_area("bottom bar"):
                  if not self.var.selected:
                     self.var.mouse_on_picture = self.on_pictures()
               else:
                  if not self.var.raised_pawn:
                     self.var.mouse_on_picture = False

               # check is mouse is on pawns
               if self.on_area("map"):
                  if not self.var.raised_pawn:
                     self.var.mouse_on_pawn = self.on_pawn()
                  else:
                     self.var.mouse_on_pawn = False

               # check if mouse is on tour button
               self.var.mouse_on_tour_button = self.on_button("tour")

               # check if mouse is on reset button
               if self.var.live != self.var.live_backup:
                  self.var.mouse_on_reset_button = self.on_button("reset")

               # send mouse x,y pos
               self.var.x, self.var.y = self.x, self.y


            elif self.var.mode == "FIGHT":

               # check if mouse is on pictures
               if self.on_area("top bar") or self.on_area("bottom bar"):
                  if not self.var.selected:
                     self.var.mouse_on_picture = self.on_pictures()
               else:
                  self.var.mouse_on_picture = False

               # check if mouse is on tour button
               self.var.mouse_on_tour_button = self.on_button("tour-fight")


            elif self.var.mode == "TOUR MAP" or self.var.mode == "TOUR FIGHT":
               # check if mouse is on continue button
               self.var.mouse_on_continue_button = self.on_button("continue")


            elif self.var.mode == "DARK VICTORY" or self.var.mode == "WHITE VICTORY" or self.var.mode == "DRAW":
               # check if mouse is on continue button
               self.var.mouse_on_continue_button = self.on_button("continue")

         """""""""""""""""""""""""""" END MOUSEMOTION """""""""""""""""""""""""""

         """""""""""""""""""""""""""" MOUSEBUTTONDOWN """""""""""""""""""""""""""
         if event.type == MOUSEBUTTONDOWN:            # CHECK MOUSE BUTTONS #
            print self.var.errors
            if self.var.mode == "MAIN MENU":

               # if mouse is on menu area
               if self.on_area("menu"):

                  if self.on_button("new game"):
                     self.var.mouse_on_new_game_button = False
                     self.new_game()

                  elif self.on_button("return"):
                     self.var.mouse_on_return_button = False
                     self.var.mode = self.var.last_mode

                  elif self.on_button("load game"):
                     self.var.mouse_on_load_game_button = False
                     self.load_game()

                  elif self.on_button("save game"):
                     self.var.mouse_on_save_game_button = False
                     self.save_game()

                  elif self.on_button("game rules"):
                     self.var.mouse_on_game_rules_button = False
                     self.var.mode = "GAME RULES"

                  elif self.on_button("about"):
                     self.var.mouse_on_about_button = False
                     self.var.mode = "ABOUT"

                  elif self.on_button("quit"):
                     self.var.mouse_on_quit_button = False
                     self.quit()


            elif self.var.mode == "MAP POSITIONING" or self.var.mode == "MAP GAMEPLAY":
               print self.var.who
               # if user click on map area, check where exacly is
               if self.on_area("map"):

                  # if on land is confrontation and is more then one enemy, choose
                  if len(self.var.who) > 2:

                     if self.in_land(self.var.where):

                        for j in range(1, len(self.var.who)):
                           x, y = self.var.who[j][3]
                           if self.rec_area( (x-8, y-8, 16, 16) ):
                              self.var.enemy_no = j
                              print self.var.errors
                              # add to error list eror 203 (wybrano przeciwnika)
                              if not 203 in self.var.errors:
                                 self.var.errors.append(203)
                              # remove from error list eror 202 (wybierz przeciwnika)
                              if 202 in self.var.errors:
                                 self.var.errors.remove(202)

                  # check is user click on pawn
                  if self.var.mouse_on_pawn:
                     self.var.selected = True
                     self.var.raised_pawn = True

                  if self.var.raised_pawn and not self.var.mouse_on_pawn:

                     # check all the lands looking for choosed land
                     for i in range(len(self.var.lands_names)):

                        # what is the current land name
                        land_name = self.var.lands_names[i]
                        # how many pawns is on the current land
                        pawns_qu = len(self.var.pawns_qu[land_name])

                        # check current land looking for choosed land
                        if self.in_land(land_name):

                           # if user moved pawn already used, edit pawns_qu
                           self.quantum()

                           # check if land is not full and enemy is not on it
                           self.possible_move(land_name, pawns_qu)

                        # if current land is not choose
                        else:
                           self.var.selected = False
                           self.var.raised_pawn = False

                  # remove selection from picture
                  if not self.var.mouse_on_pawn:
                     self.var.selected = False


               # if user click on top or bottom bar
               elif self.on_area("top bar") or self.on_area("bottom bar"):

                  # if user uses crtl, raise pawn
                  if self.crtl_pressed:
                     self.var.raised_pawn = True
                     self.crtl_pressed = False

                  # if user click on picture turn on selection
                  if self.on_pictures():
                     self.var.selected = True
                  else:
                     self.var.mouse_on_picture = False

               # if user clicked on different place
               else:
                  self.var.mouse_on_picture = False

               # if mouse is on torur button
               if self.on_button("tour"):
                  self.var.verify = True

               # if mouse is on reset button
               if self.on_button("reset"):
                  self.var.reset = True


            elif self.var.mode == "FIGHT":
               if not 302 in self.var.errors:
                  self.var.errors.append(302)

               # if user click on top or bottom bar
               if self.on_area("top bar") or self.on_area("bottom bar"):

                  # if user click on picture turn on selection
                  if self.on_pictures():
                     self.var.selected = True
                     self.var.check_confrontation = True
                     # add to error list eror 303 (wybrano karte)
                     if not 303 in self.var.errors:
                        self.var.errors.append(303)
                     # remove from error list eror 302 (wybierz karte)
                     if 302 in self.var.errors:
                        self.var.errors.remove(302)

                  else:
                     self.var.mouse_on_picture = False
                     # remove from error list eror 303 (wybrano karte)
                     if 303 in self.var.errors:
                        self.var.errors.remove(303)

               # if user clicked on different place
               else:
                  self.var.mouse_on_picture = False
                  self.var.selected = False
                  # remove from error list eror 303 (wybrano karte)
                  if 303 in self.var.errors:
                     self.var.errors.remove(303)

               # if mouse is on torur button
               if self.on_button("tour-fight"):
                  self.var.verify = True

               # if mouse is on reset button
               if self.on_button("reset"):
                  self.var.reset = True


            elif self.var.mode == "TOUR MAP" or self.var.mode == "TOUR FIGHT" :

               # if mouse is on continue button
               if self.on_button("continue"):
                  self.var.confirm = True


            elif self.var.mode == "DARK VICTORY" or self.var.mode == "WHITE VICTORY" or self.var.mode == "DRAW":

               # if mouse is on continue button
               if self.on_button("continue"):
                  self.var.confirm = True


            elif self.var.mode == "GAME RULES":

               # if mouse is on down button
               if self.rec_area((850,750,40,40)):
                  if self.var.sheet < 7:
                     self.var.sheet += 1
               # if mouse is on up button
               elif self.rec_area((850,10,40,40)):
                  if self.var.sheet > 0:
                     self.var.sheet -= 1
               # if mouse is on return button
               elif self.rec_area((760,750,82,40)):
                  self.var.mode = "MAIN MENU"


            elif self.var.mode == "ABOUT":

               # if mouse is on return button
               if self.rec_area((750,720,82,44)):
                  self.var.mode = "MAIN MENU"

         """""""""""""""""""""""     END MOUSEBUTTONDOWN    """""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""   End of main function   """""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""    Main menu functions    """"""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   # if choosed new game, then reset settings
   def new_game(self):

      self.var.mode = "MAP POSITIONING"
      self.var.last_mode = "MAIN MENU"

      self.var.player = 1
      self.sel_black_char_no = -1
      self.sel_white_char_no = -1

      self.var.selected = False
      self.var.ready = True
      self.var.raised_pawn = False

      self.var.movement = 1
      self.var.fightt = 1
      self.var.errors = []

      for name in self.var.lands_names:
         self.var.pawns_qu[name] = []

      for char in self.var.b_live:
         char[2] = "none"
         char[3] = (0,0)

      for char in self.var.w_live:
         char[2] = "none"
         char[3] = (0,0)

      self.var.b_dead = []
      self.var.w_dead = []

      self.cards = []
      self.b_cards = []
      self.w_cards = []

      self.b_wasted_cards = []
      self.w_wasted_cards = []

      self.live_backup = []
      self.pawns_qu_backup = {}


   # if choosed load game, then open pickle file
   def load_game(self):

      if self.var.saved:
         save = pickle.load(open('save'))

         self.var.mode              = save[0]
         self.var.last_mode         = save[1]
         self.var.player            = save[2]
         self.var.sel_black_char_no = save[3]
         self.var.sel_white_char_no = save[4]
         self.var.b_live            = save[5]
         self.var.w_live            = save[6]
         self.var.b_dead            = save[7]
         self.var.w_dead            = save[8]
         self.var.pawns_qu          = save[9]
         self.var.selected          = save[10]
         self.var.ready             = save[11]
         self.var.raised_pawn       = save[12]
         self.var.sel_char_id       = save[13]
         self.var.movement          = save[14]
         self.var.who               = save[15]
         self.var.where             = save[16]
         self.var.live_backup       = save[17]
         self.var.pawns_qu_backup   = save[18]
         self.b_cards               = save[19]
         self.w_cards               = save[20]
         self.b_wasted_cards        = save[21]
         self.w_wasted_cards        = save[22]

         self.var.sel_char_id = -1
         self.var.loaded = True


   # if choosed save game, then save important variables
   def save_game(self):

      save = [self.var.mode, self.var.last_mode, self.var.player, self.var.sel_black_char_no,
            self.var.sel_white_char_no, self.var.b_live, self.var.w_live, self.var.b_dead,
            self.var.w_dead, self.var.pawns_qu, self.var.selected, self.var.ready,
            self.var.raised_pawn, self.var.sel_char_id, self.var.movement,
            self.var.who, self.var.where, self.var.live_backup, self.var.pawns_qu_backup,
            self.b_cards, self.w_cards, self.b_wasted_cards, self.w_wasted_cards ]

      pickle.dump(save, open('save','w'))
      self.var.saved = True


   # if choosed quit, then quit the game
   def quit(self):

      pygame.display.quit()
      exit()

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""    End of main menu functions     """"""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
