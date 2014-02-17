#-------------------------------------------------------------------------------
# Name:        variables.py
# Purpose:
#
# Author:      novirael
#
# Created:     18-08-2012
# Copyright:   (c) novirael 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
'''

PLAYER:
      0  DARK SIDE
      1  WHITE SIDE

MODE :

   TOUR FIGHT
   TOUR MAP

   DARK VICTORY
   WHITE VICTORY
   DRAW

   MAIN MENU
   GAME RULES
   ABOUT

   MAP POSITIONING
   MAP GAMEPLAY

   FIGHT


'''

class MainVariables():
   def __init__(self):

      self.mode = "MAIN MENU"
      self.last_mode = "MAIN MENU"
      self.player = 1

      self.x = 0
      self.y = 0
      self.sheet = 0

      self.sel_black_char_no = -1
      self.sel_white_char_no = -1
      self.sel_char_id = -1

      self.selected = False
      self.ready = True
      self.verify = False
      self.confirm = False
      self.raised_pawn = False
      self.movement = 1
      self.fightt = 1
      self.mment = {}

      self.errors = []

      self.check_confrontation = False

      self.enemy_no = 0

      self.no_pos = 0
      self.no_abroad = 0

      self.loaded = False
      self.saved = False
      self.reset = False
      self.brak_ruchu = False

      self.who = []
      self.where = "none"

      # Gameplay
      self.mouse_on_picture = False
      self.mouse_on_pawn = False
      self.mouse_on_tour_button = False
      self.mouse_on_reset_button = False
      self.mouse_on_continue_button = False

      # Main Menu
      self.mouse_on_menu = False
      self.mouse_on_new_game_button = False
      self.mouse_on_return_button = False
      self.mouse_on_load_game_button = False
      self.mouse_on_save_game_button = False
      self.mouse_on_game_rules_button = False
      self.mouse_on_about_button = False
      self.mouse_on_quit_button = False


      self.areas = {
         "menu"       : (600, 300, 270, 440),
         "top bar"    : (  0,   0, 900,  85),
         "bottom bar" : (  0, 715, 900,  85),
         "map"        : (  0,  85, 630, 630) }

      self.buttons = {
         "tour"      : (640, 595, 250, 50),
         "tour-fight": (325, 660, 250, 50),
         "reset"     : (640, 645, 250, 50),
         "continue"  : (300, 640, 250, 50),
         "new game"  : (610, 320, 250, 50),
         "return"    : (610, 380, 250, 50),
         "load game" : (610, 440, 250, 50),
         "save game" : (610, 500, 250, 50),
         "game rules": (610, 560, 250, 50),
         "about"     : (610, 620, 250, 50),
         "quit"      : (610, 680, 250, 50) }

      self.lands_names = ["mordor", "dagorlad", "gondor", "mroczna puszcza",
         "fangorn", "rohan", "wysoka przelecz", "gory mgliste", "moria",
         "wrota rohanu", "rhudaur", "eregion", "enedwaith", "cardolan",
         "arthedain", "shire" ]

      self.land = {
         "mordor"          : (225,600,180,80),
         "dagorlad"        : (315,520,180,80),
         "gondor"          : (135,520,180,80),

         "mroczna puszcza" : (405,440,180,80),
         "fangorn"         : (225,440,180,80),
         "rohan"           : ( 45,440,180,80),

         "wysoka przelecz" : (455,360,150,80),
         "gory mgliste"    : (305,360,150,80),
         "moria"           : (155,360,150,80),
         "wrota rohanu"    : (  5,360,150,80),

         "rhudaur"         : (405,280,180,80),
         "eregion"         : (225,280,180,80),
         "enedwaith"       : ( 45,280,180,80),

         "cardolan"        : (135,200,180,80),
         "arthedain"       : (315,200,180,80),
         "shire"           : (225,120,180,80) }

      self.pawns_qu = {
         "mordor"          : [],
         "dagorlad"        : [],
         "gondor"          : [],

         "mroczna puszcza" : [],
         "fangorn"         : [],
         "rohan"           : [],

         "wysoka przelecz" : [],
         "gory mgliste"    : [],
         "moria"           : [],
         "wrota rohanu"    : [],

         "rhudaur"         : [],
         "eregion"         : [],
         "enedwaith"       : [],

         "cardolan"        : [],
         "arthedain"       : [],
         "shire"           : [] }

      self.live = [[]]
      self.dead = [[]]

      """
      9: troll0
      5: balrog0, szeloba0, czarnoksieznik0, gandalf1
      4: saruman0, aragorn1
      3: latajacy nazgul0, czarny jezdziec0, legolas1, gimli1
      2: ork0, warg0, sam1, merry1
      1: frodo1, pippin1
      0: boromir1
      """

      # being [ [player, number,  character, power, land, position]
      self.b_live = [
            [0, "balrog0",           "none", (0,0), 5 ],
            [1, "szeloba0",          "none", (0,0), 5 ],
            [2, "czarnoksieznik0",   "none", (0,0), 5 ],
            [3, "latajacy nazgul0",  "none", (0,0), 3 ],
            [4, "czarny jezdziec0",  "none", (0,0), 3 ],
            [5, "saruman0",          "none", (0,0), 4 ],
            [6, "ork0",              "none", (0,0), 2 ],
            [7, "warg0",             "none", (0,0), 2 ],
            [8, "troll0",            "none", (0,0), 9 ] ]

      self.w_live = [
            [0, "frodo1",            "none", (0,0), 1 ],
            [1, "sam1",              "none", (0,0), 2 ],
            [2, "pippin1",           "none", (0,0), 1 ],
            [3, "merry1",            "none", (0,0), 2 ],
            [4, "gandalf1",          "none", (0,0), 5 ],
            [5, "aragorn1",          "none", (0,0), 4 ],
            [6, "legolas1",          "none", (0,0), 3 ],
            [7, "gimli1",            "none", (0,0), 3 ],
            [8, "boromir1",          "none", (0,0), 0 ] ]

      self.b_dead = []
      self.w_dead = []

      self.cards = []
      self.b_cards = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6],
                      [6, "magia"], [7, "ucieczka"], [8, "oko saurona"] ]
      self.w_cards = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, "magia"],
                      [6, "odwrot"], [7, "poswiecenie"], [8, "plaszcz elfow"] ]

      self.b_wasted_cards = []
      self.w_wasted_cards = []

      self.live_backup = []
      self.pawns_qu_backup = {}
