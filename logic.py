#-------------------------------------------------------------------------------
# Name:        logic.py
# Purpose:
#
# Author:      novirael
#
# Created:     18-08-2012
# Copyright:   (c) novirael 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import copy

class Logic():

   def __init__(self, var):

      self.var = var
      self.movement = {}
      self.char = []
      self.p_lose = -2
      self.battle_played = False
      self.dark_chose = False
      self.white_chose = False
      self.cards = {"dark": -1, "white": -1}

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""""     Change player     """"""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   def rewrite_things(self, backup=False):

      if self.var.player == 0:
         self.var.live = self.var.b_live
         self.var.dead = self.var.b_dead
         if backup:
            self.var.live_backup = copy.deepcopy(self.var.b_live)

      else:
         self.var.live = self.var.w_live
         self.var.dead = self.var.w_dead
         if backup:
            self.var.live_backup = copy.deepcopy(self.var.w_live)


   def change_seat(self):

      # inc player, 0 or 1 ( dark or white side )
      self.var.player += 1
      if self.var.player > 1:
         self.var.player = 0

      self.var.sel_black_char_no = -1
      self.var.sel_white_char_no = -1
      self.var.sel_char_id = -1

      # change y pos of every pawn
      self.change_pawns_pos(self.var.b_live)
      self.change_pawns_pos(self.var.w_live)

      # replace main lists
      self.rewrite_things(True)

      # make backup pawns_qu dict
      self.var.pawns_qu_backup = copy.deepcopy(self.var.pawns_qu)

      # replace lands position
      self.lands_pos()

   def change_pawns_pos(self, pawns):

      for i in range(len(pawns)):
         x, y = pawns[i][3]

         if y == 120 + 80/4:
            y = 600 + 80*3/4
         elif y == 120 + 80/3:
            y = 600 + 80*2/3
         elif y == 120 + 80/2:
            y = 600 + 80/2
         elif y == 120 + 80*2/3:
            y = 600 + 80/3
         elif y == 120 + 80*3/4:
            y = 600 + 80/4

         elif y == 200 + 80/2:
            y = 520 + 80/2
         elif y == 280 + 80/2:
            y = 440 + 80/2
         elif y == 440 + 80/2:
            y = 280 + 80/2
         elif y == 520 + 80/2:
            y = 200 + 80/2

         elif y == 600 + 80/4:
            y = 120 + 80*3/4
         elif y == 600 + 80/3:
            y = 120 + 80*2/3
         elif y == 600 + 80/2:
            y = 120 + 80/2
         elif y == 600 + 80*2/3:
            y = 120 + 80/3
         elif y == 600 + 80*3/4:
            y = 120 + 80/4

         # 2 & 6 level
         if x == 135 + 180/2 or x == 135 + 180/3 or x == 135 + 180*2/3:
            x += 180
         elif x == 315 + 180/2 or x == 315 + 180/3 or x == 315 + 180*2/3:
            x -= 180
         # 3 & 5 level (pomijamy srodkowa kraine)
         elif x == 45 + 180/2 or x == 45 + 180/3 or x == 45 + 180*2/3:
            x += 360
         elif x == 405 + 180/2 or x == 405 + 180/3 or x == 405 + 180*2/3:
            x -= 360
         # 4 level
         elif x == 5 + 150/2:
            x += 450
         elif x == 155 + 150/2:
            x += 150
         elif x == 305 + 150/2:
            x -= 150
         elif x == 455 + 150/2:
            x -= 450

         pawns[i][3] = (x,y)

   def lands_pos(self):

      if self.var.player == 0:

         self.var.land["mordor"]          = (225,600,180,80)
         self.var.land["dagorlad"]        = (315,520,180,80)
         self.var.land["gondor"]          = (135,520,180,80)

         self.var.land["mroczna puszcza"] = (405,440,180,80)
         self.var.land["fangorn"]         = (225,440,180,80)
         self.var.land["rohan"]           = ( 45,440,180,80)

         self.var.land["wysoka przelecz"] = (455,360,150,80)
         self.var.land["gory mgliste"]    = (305,360,150,80)
         self.var.land["moria"]           = (155,360,150,80)
         self.var.land["wrota rohanu"]    = (  5,360,150,80)

         self.var.land["rhudaur"]         = (405,280,180,80)
         self.var.land["eregion"]         = (225,280,180,80)
         self.var.land["enedwaith"]       = ( 45,280,180,80)

         self.var.land["cardolan"]        = (135,200,180,80)
         self.var.land["arthedain"]       = (315,200,180,80)
         self.var.land["shire"]           = (225,120,180,80)

      else:

         self.var.land["mordor"]          = (225,120,180,80)
         self.var.land["dagorlad"]        = (135,200,180,80)
         self.var.land["gondor"]          = (315,200,180,80)

         self.var.land["mroczna puszcza"] = ( 45,280,180,80)
         self.var.land["fangorn"]         = (225,280,180,80)
         self.var.land["rohan"]           = (405,280,180,80)

         self.var.land["wysoka przelecz"] = (  5,360,150,80)
         self.var.land["gory mgliste"]    = (155,360,150,80)
         self.var.land["moria"]           = (305,360,150,80)
         self.var.land["wrota rohanu"]    = (455,360,150,80)

         self.var.land["rhudaur"]         = ( 45,440,180,80)
         self.var.land["eregion"]         = (225,440,180,80)
         self.var.land["enedwaith"]       = (405,440,180,80)

         self.var.land["cardolan"]        = (315,520,180,80)
         self.var.land["arthedain"]       = (135,520,180,80)
         self.var.land["shire"]           = (225,600,180,80)


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """""""""""""""""""""""" End of changing player  """"""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""      Veryfication and Confrimation      """"""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   # fucntion confirm click on continue button
   def confirmation(self):

      mode = self.var.mode

      # on victory screen
      if mode == "DARK VICTORY" or mode == "WHITE VICTORY" or mode == "DRAW":
         self.var.movement += 1
         mode = "MAP GAMEPLAY"

         # clean up after the battle
         if self.battle_played:
            self.clean_up()
            self.battle_played = False

      # on tour map screen
      if mode == "TOUR MAP":
         self.var.movement += 1
         if self.var.movement < 3:
            mode = "MAP POSITIONING"
         else:
            mode = "MAP GAMEPLAY"

      # on fight screen
      if mode == "TOUR FIGHT":
         self.var.check_confrontation = True
         mode = "FIGHT"

      self.var.mouse_on_continue_button = False
      self.var.ready = True
      self.var.mode = mode


   # fucntion verify game conditions to end tour
   def verification(self):

      if self.var.mode == "MAP POSITIONING":

         # reset assist var
         self.var.no_pos = 0
         self.var.no_abroad = 0

         for i in range(len(self.var.live)):
            # check if user positioned all 9 pawns
            if self.var.live[i][2] != "none":
               self.var.no_pos += 1
            # check if pawn is below mountains
            x, y = self.var.live[i][3]
            if y > 85 and y < 440:
               self.var.no_abroad += 1

         # add or remove form error list eror 101
         if self.var.no_pos < 9:
            if not 101 in self.var.errors:
               self.var.errors.append(101)
         else:
            if 101 in self.var.errors:
               self.var.errors.remove(101)

         # add or remove form error list eror 102
         if self.var.no_abroad > 0:
            if not 102 in self.var.errors:
               self.var.errors.append(102)
         else:
            if 102 in self.var.errors:
               self.var.errors.remove(102)

         # remove from error list error 103
         if 103 in self.var.errors:
            self.var.errors.remove(103)

         # remove from error list error 104
         if 104 in self.var.errors:
            self.var.errors.remove(104)

         # if there is no errors allow to end tour
         if len(self.var.errors) == 0:
            self.mouse_on_tour_button = False
            self.var.mode = "TOUR MAP"

      elif self.var.mode == "MAP GAMEPLAY":

         # if move was correct allow to next tour
         if self.analyze_move():

            self.var.errors = []
            self.mouse_on_tour_button = False

            if len(self.var.who) > 0:
               self.var.mode = "TOUR FIGHT"
               self.var.fightt = 1
            else:
               self.var.mode = "TOUR MAP"

         # if move is incorrect inform about it
         else:
            # except player wants to left his turn
            if not self.var.brak_ruchu:
               if not 204 in self.var.errors:
                  self.var.errors.append(204)

         if self.var.brak_ruchu:
            # add to error list eror 205 (brak ruchu)
            if not 205 in self.var.errors:
               self.var.errors.append(205)
         else:
            # remove from error list eror 205 (brak ruchu)
            if 205 in self.var.errors:
               self.var.errors.remove(205)

      elif self.var.mode == "FIGHT":

         self.mouse_on_tour_button = False
         if self.battle_played and self.var.fightt != 1:
            if self.p_lose == -1:
               self.var.mode = "DRAW"
            elif self.p_lose == 1:
               self.var.mode = "DARK VICTORY"
            elif self.p_lose == 0:
               self.var.mode = "WHITE VICTORY"
         else:
            self.var.fightt += 1
            self.var.mode = "TOUR FIGHT"


   # function analyze pawns move
   # return True if move was correct else return False
   def analyze_move(self):

      self.char = []
      self.movement = {}

      # check how many pawns and who has moved and sort movement by character
      for char_before in self.var.live_backup:
         for char_after in self.var.live:
            if char_before[0] == char_after[0] and char_before[2] != char_after[2]:
               self.char.append(char_before[1])
               self.movement[char_before[1]] = []
               self.movement[char_before[1]].extend([char_before[2], char_after[2]])

      # make dictionary of good and bad move of pawns
      move = { "dobrze" : [], "zle" : [] }
      for c in self.char:
         begin, end = self.movement[c][0], self.movement[c][1]
         if begin != end:
            correct_end = self.correct_movement(c, begin)
            if end in correct_end:
               move["dobrze"].append(c)
            else:
               move["zle"].append(c)

      # condition for complete MAP GAMEPLAY tour
      if len(move["dobrze"]) == 1 and len(move["zle"]) == 0:
         return True

      elif len(move["dobrze"]) == 0 and len(move["zle"]) == 0:
         if self.var.brak_ruchu:
            self.var.brak_ruchu = False
            return True
         else:
            self.var.brak_ruchu = True

      return False

   # depends of pawn type and its previous position
   # return list of lands where pawn can move
   def correct_movement(self, character, from_where):
      to_where = []

      # if there will be confrontation
      if len(self.var.who) > 0:

         # if Aragorn
         if character == "aragorn1":
            if from_where == "shire":
               to_where.extend(["arthedain", "cardolan"])
            elif from_where == "arthedain":
               to_where.extend(["shire", "cardolan", "eregion", "rhudaur"])
            elif from_where == "cardolan":
               to_where.extend(["shire", "arthedain", "eregion", "enedwaith"])
            elif from_where == "rhudaur":
               to_where.extend(["arthedain", "eregion", "gory mgliste", "wysoka przelecz"])
            elif from_where == "eregion":
               to_where.extend(["arthedain", "rhudaur", "gory mgliste", "moria", "enedwaith", "cardolan"])
            elif from_where == "enedwaith":
               to_where.extend(["wrota rohamu", "moria", "eregion", "cardolan"])
            elif from_where == "wrota rohamu":
               to_where.extend(["rohan", "enedwaith"])
            elif from_where == "moria":
               to_where.extend(["eregion", "enedwaith", "fangorn", "rohan"])
            elif from_where == "gory mgliste":
               to_where.extend(["rhudaur", "eregion", "fangorn", "mroczna puszcza"])
            elif from_where == "wysoka przelecz":
               to_where.extend(["rhudaur", "mroczna puszcza"])
            elif from_where == "mroczna puszcza":
               to_where.extend(["dagorlad", "fangorn", "gory mgliste", "wysoka przelecz"])
            elif from_where == "fangorn":
               to_where.extend(["dagorlad", "gondor", "rohan", "moria" "gory mgliste", "mroczna puszcza"])
            elif from_where == "rohan":
               to_where.extend(["gondor", "fangorn", "moria", "wrota rohanu"])
            elif from_where == "gondor":
               to_where.extend(["rohan", "fangorn", "dagorlad", "mordor"])
            elif from_where == "dagorlad":
               to_where.extend(["mroczna puszcza", "fangorn", "gondor", "mordor" ])
            elif from_where == "mordor":
               to_where.extend(["gondor", "dagorlad"])

         # if Czarnoksieznik z Angmaru
         elif character == "czarnoksieznik0":
            if from_where == "shire":
               to_where.extend([])
            elif from_where == "arthedain":
               to_where.extend(["cardolan"])
            elif from_where == "cardolan":
               to_where.extend(["arthedain"])
            elif from_where == "rhudaur":
               to_where.extend(["eregion"])
            elif from_where == "eregion":
               to_where.extend(["rhudaur", "enedwaith"])
            elif from_where == "enedwaith":
               to_where.extend(["eregion"])
            elif from_where == "mroczna puszcza":
               to_where.extend(["fangorn"])
            elif from_where == "fangorn":
               to_where.extend(["rohan", "mroczna puszcza"])
            elif from_where == "rohan":
               to_where.extend(["fangorn"])
            elif from_where == "gondor":
               to_where.extend(["dagorlad"])
            elif from_where == "dagorlad":
               to_where.extend(["gondor"])
            elif from_where == "mordor":
               to_where.extend([])

         # if Latajacy Nazgul or Czarny Jezdziec
         elif character == "latajacy nazgul0" or character == "czarny jezdziec0":
               to_where.extend(["mordor", "dagorlad", "gondor", "mroczna puszcza",
                  "fangorn", "rohan", "wysoka przelecz", "gory mgliste", "moria",
                  "wrota rohanu", "rhudaur", "eregion", "enedwaith", "cardolan",
                  "arthedain", "shire" ])
               # latajacy nazgul, moze atakowac gdy stoi tylko jedna figura przeciwnika
               # czarny jezdziec, moze atakowac gdy po drodze nie ma przeszkod

      # classic move ( 1x forward )
      # dark side
      if character[-1] == "0":
         if from_where == "mordor":
            to_where.extend(["gondor", "dagorlad"])
         elif from_where == "gondor":
            to_where.extend(["rohan", "fangorn"])
         elif from_where == "dagorlad":
            to_where.extend(["fangorn", "mroczna puszcza"])
         elif from_where == "rohan":
            to_where.extend(["wrota rohanu", "moria"])
         elif from_where == "fangorn":
            to_where.extend(["moria", "gory mgliste"])
         elif from_where == "mroczna puszcza":
            to_where.extend(["gory mgliste", "wysoka przelecz"])
         elif from_where == "wrota rohanu":
            to_where.extend(["enedwaith"])
         elif from_where == "moria" :
            to_where.extend(["enedwaith", "eregion"])
         elif from_where == "gory mgliste":
            to_where.extend(["eregion", "rhudaur"])
         elif from_where == "wysoka przelecz":
            to_where.extend(["rhudaur"])
         elif from_where == "enedwaith":
            to_where.extend(["cardolan"])
         elif from_where == "eregion":
            to_where.extend(["cardolan", "arthedain"])
         elif from_where == "rhudaur":
            to_where.extend(["arthedain"])
         elif from_where == "cardolan":
            to_where.extend(["shire"])
         elif from_where == "arthedain":
            to_where.extend(["shire"])
         elif from_where == "shire":
            to_where.extend([])

      # white side
      elif character[-1] == "1":
         if from_where == "mordor":
            to_where.extend([])
         elif from_where == "gondor":
            to_where.extend(["mordor"])
         elif from_where == "dagorlad":
            to_where.extend(["mordor"])
         elif from_where == "rohan":
            to_where.extend(["gondor"])
         elif from_where == "fangorn":
            to_where.extend(["dagorlad", "gondor", "rohan"]) # rohan skrot rzeka
         elif from_where == "mroczna puszcza":
            to_where.extend(["dagorlad", "fangorn"]) # fangorn skrot rzeka
         elif from_where == "wrota rohanu":
            to_where.extend(["rohan"])
         elif from_where == "moria" :
            to_where.extend(["fangorn", "rohan"])
         elif from_where == "gory mgliste":
            to_where.extend(["mroczna puszcza", "fangorn"])
         elif from_where == "wysoka przelecz":
            to_where.extend(["mroczna puszcza"])
         elif from_where == "enedwaith":
            to_where.extend(["moria", "wrota rohanu"])
         elif from_where == "eregion":
            to_where.extend(["gory mgliste", "moria", "fangorn"]) #fangorn skrot kopalnia nie mozna wtedy uciec...!!!! BARLOG!!
         elif from_where == "rhudaur":
            to_where.extend(["wysoka przelecz", "gory mgliste"])
         elif from_where == "cardolan":
            to_where.extend(["eregion", "enedwaith"])
         elif from_where == "arthedain":
            to_where.extend(["rhudaur", "eregion"])
         elif from_where == "shire":
            to_where.extend(["arthedain", "cardolan"])

      return to_where


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""   End of Veryfication and Confrimation  """"""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""""   Confrontation   """"""""""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   # main confrontation function
   def confrontation(self):

      if self.var.mode == "MAP GAMEPLAY":

         if len(self.var.who) == 0:
            # check where is confrontation and who will fight
            for land_name in self.var.lands_names:

               bin, who = [], []

               # find land where is char white and dark, by character names
               for pawn in self.var.pawns_qu[land_name]:
                  if not pawn[-1] in bin:
                     bin.append(int(pawn[-1]))
                     who.append(pawn)

                  if 0 in bin and 1 in bin:

                     # find characters in b_live and w_lives
                     for char in who:
                        for char0 in self.var.b_live:
                           if char0[1] == char:
                              self.var.who.append(char0)
                        for char1 in self.var.w_live:
                           if char1[1] == char:
                              self.var.who.append(char1)

                     self.var.where = land_name

            # add to error list eror 201 (bedzie konfrontacja)
            if not 201 in self.var.errors:
               self.var.errors.append(201)

            if len(self.var.who) > 2:
               # add to error list eror 202 (wybierz przeciwnika)
               if not 202 in self.var.errors:
                  self.var.errors.append(202)
            else:
               # add to error list eror 203 (wybrano przeciwnika)
               if not 203 in self.var.errors:
                  self.var.errors.append(203)

            # last two players on list will fight
            self.var.who.append(self.var.who[self.var.enemy_no])
            self.var.who.remove(self.var.who[self.var.enemy_no])

      elif self.var.mode == "FIGHT":

         if not self.battle_played:
            if self.var.who[-1][1][-1] == "0":
               name1 = self.var.who[-2][1]
               power1 = self.var.who[-2][4]
               name0 = self.var.who[-1][1]
               power0 = self.var.who[-1][4]
            elif self.var.who[-1][1][-1] == "1":
               name1 = self.var.who[-1][1]
               power1 = self.var.who[-1][4]
               name0 = self.var.who[-2][1]
               power0 = self.var.who[-2][4]

            # add to error list eror 302 (wybrano karte)
            if not 303 in self.var.errors:
               if not 302 in self.var.errors:
                  self.var.errors.append(302)
            else:
               if 302 in self.var.errors:
                  self.var.errors.remove(302)

            # check if there is clear situation
            self.battle_played = self.confrontation_rules(name0, name1, power0, power1)


   # function checks confrontation conditions
   def confrontation_rules(self, name0, name1, power0, power1):
      if self.clear_situations(name0, name1):
         return True
      elif self.cards_play(power0, power1):
         return True
      return False


   # if confrontation is enough clean to resolve
   def clear_situations(self, name0, name1):

      if name0 == "czarnoksieznik0" and name1 == "merry1":
         self.p_lose = 0
      elif name0 == "latajacy nazgul0" and name1 == "legolas1":
         self.p_lose = 0
      elif name0 == "gimli1" and name1 == "ork0":
         self.p_lose = 0
      elif name0 != "warg0" and name1 == "boromir1":
         self.p_lose = -1
      elif name0 == "ork0":
         self.p_lose = 1

      if self.p_lose != -2:
         if not 301 in self.var.errors:
            self.var.errors.append(301)
         return True

      return False


   def cards_play(self, power0, power1):

      if 303 in self.var.errors:
         if self.var.player == 0:
            self.cards["dark"] = self.var.sel_black_char_no
            self.dark_chose = True
         else:
            self.cards["white"] = self.var.sel_white_char_no
            self.white_chose = True

      print self.cards

      if self.dark_chose and self.white_chose:

         if self.cards["dark"] > -1 and self.cards["dark"] < 7:
            power0 += self.cards["dark"] + 1
         else:
            return False

         if self.cards["white"] > -1 and self.cards["white"] < 7:
            power1 += self.cards["white"] + 1
         else:
            return False

         self.dark_chose = False
         self.white_chose = False

         if power0 > power1:
            self.p_lose = 1
         elif power0 < power1:
            self.p_lose = 0
         else:
            self.p_lose = -1

         return True

      return False



   # fuction clean up after the confrontation
   def clean_up(self):

      # if confrontation lose dark side
      if self.p_lose == 0:
         if self.var.player == 0:
            char = self.var.who[-2]
         else:
            char = self.var.who[-1]
         self.var.who.remove(char)
         self.var.b_live.remove(char)
         self.var.b_dead.append(char)
         for land_name in self.var.lands_names:
            if char[1] in self.var.pawns_qu[land_name]:
               self.var.pawns_qu[land_name].remove(char[1])

      # if confrontation lose white side
      elif self.p_lose == 1:
         if self.var.player == 0:
            char = self.var.who[-2]
         else:
            char = self.var.who[-1]
         self.var.who.remove(char)
         self.var.w_live.remove(char)
         self.var.w_dead.append(char)
         for land_name in self.var.lands_names:
            if char[1] in self.var.pawns_qu[land_name]:
               self.var.pawns_qu[land_name].remove(char[1])

      # if was a draw
      elif self.p_lose == -1:
         if self.var.player == 1:
            char1 = self.var.who[-2]
            char0 = self.var.who[-1]
         else:
            char1 = self.var.who[-1]
            char0 = self.var.who[-2]

         self.var.who.remove(char0)
         self.var.who.remove(char1)
         self.var.b_live.remove(char0)
         self.var.w_live.remove(char1)
         self.var.b_dead.append(char0)
         self.var.w_dead.append(char1)
         for land_name in self.var.lands_names:
            if char0[1] in self.var.pawns_qu[land_name]:
               self.var.pawns_qu[land_name].remove(char0[1])
               self.var.pawns_qu[land_name].remove(char1[1])

      self.p_lose = -2

      # clear error list
      self.var.errors = []


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""   End of Confrontation   """""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   def reset(self):

      self.var.live = copy.deepcopy(self.var.live_backup)
      self.var.pawns_qu = copy.deepcopy(self.var.pawns_qu_backup)


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""     This is the main function in Logic class      """"""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   def game(self):

      # confirmation of change game mode by continue button
      if self.var.confirm:
         self.confirmation()
         self.var.confirm = False

      # check if player do what he have to do before end tour
      if self.var.verify:
         self.verification()
         self.var.verify = False

      # check is there is confrontation
      if self.var.check_confrontation:
         self.confrontation()
         self.var.check_confrontation = False

      # change sides
      if self.var.ready:
         self.change_seat()

      # rewrite actually selected character
      if self.var.player == 0:
         self.var.sel_char_id = self.var.sel_black_char_no
      else:
         self.var.sel_char_id = self.var.sel_white_char_no

      # if user decided to reset move in tour
      if self.var.reset:
         self.reset()
         #self.rewrite_things()
         self.var.reset = False

      # if game was loaded check land pos and rewrite live and dead var
      if self.var.loaded:
         self.lands_pos()
         self.rewrite_things()


   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
   """"""""""""""""""""""""   End of main function   """""""""""""""""""""""""
   """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

