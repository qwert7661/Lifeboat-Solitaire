# ================================================================================================================= #
#                                                    start of code                                                  #
# ================================================================================================================= #
import random as rng
from itertools import chain
import sys
import pygame as pg
pg.init()
pg.font.init()

print("Welcome to Lifeboat!")

# Setting up Screen, Clock & Font
screen_width = 1000
screen_height = 800
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Lifeboat")
clock = pg.time.Clock()
font = pg.font.Font(None,30)
bigfont = pg.font.Font(None,75)
# Music
music_sound = pg.mixer.Sound('Lifeboat_Assets/audio/lifeboat_music.mp3')
music_sound.play(loops = -1)



# ================================================================================================================= #
#                                                     CARD CLASS                                                    #
# ================================================================================================================= #
# Defining Card Class
class Card(pg.sprite.Sprite):
    def __init__(self, name: str, rank: int, suit: str, surf):
        super().__init__()
        self.name = name
        self.rank = rank
        self.suit = suit
        self.surf = surf
        self.surf = pg.transform.scale(self.surf,(138,200))
        self.rect = self.surf.get_rect()
        self.is_held = False

    def update_position(self,pos):
        self.rect.center = pos

# Initializing Cards Objects
if True:
    cBack = Card(name='back', rank=0, suit='none', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/card_back.png'))

    c2h = Card(name='🂲2♥', rank=2, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/2_of_hearts.png'))
    c3h = Card(name='🂳3♥', rank=3, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/3_of_hearts.png'))
    c4h = Card(name='🂴4♥', rank=4, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/4_of_hearts.png'))
    c5h = Card(name='🂵5♥', rank=5, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/5_of_hearts.png'))
    c6h = Card(name='🂶6♥', rank=6, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/6_of_hearts.png'))
    c7h = Card(name='🂷7♥', rank=7, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/7_of_hearts.png'))
    c8h = Card(name='🂸8♥', rank=8, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/8_of_hearts.png'))
    c9h = Card(name='🂹9♥', rank=9, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/9_of_hearts.png'))
    c10h = Card(name='🂺10♥', rank=10, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/10_of_hearts.png'))
    cJh = Card(name='🂻J♥', rank=11, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/jack_of_hearts2.png'))
    cQh = Card(name='🂽Q♥', rank=12, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/queen_of_hearts2.png'))
    cKh = Card(name='🂾K♥', rank=13, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/king_of_hearts2.png'))
    cAh = Card(name='🂱A♥', rank=14, suit='heart', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/ace_of_hearts.png'))

    c2d = Card(name='🃂2♦', rank=2, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/2_of_diamonds.png'))
    c3d = Card(name='🃃3♦', rank=3, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/3_of_diamonds.png'))
    c4d = Card(name='🃄4♦', rank=4, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/4_of_diamonds.png'))
    c5d = Card(name='🃅5♦', rank=5, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/5_of_diamonds.png'))
    c6d = Card(name='🃆6♦', rank=6, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/6_of_diamonds.png'))
    c7d = Card(name='🃇7♦', rank=7, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/7_of_diamonds.png'))
    c8d = Card(name='🃈8♦', rank=8, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/8_of_diamonds.png'))
    c9d = Card(name='🃉9♦', rank=9, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/9_of_diamonds.png'))
    c10d = Card(name='🃊10♦', rank=10, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/10_of_diamonds.png'))
    cJd = Card(name='🃋J♦', rank=11, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/jack_of_diamonds2.png'))
    cQd = Card(name='🃍Q♦', rank=12, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/queen_of_diamonds2.png'))
    cKd = Card(name='🃎K♦', rank=13, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/king_of_diamonds2.png'))
    cAd = Card(name='🃁A♦', rank=14, suit='diamond', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/ace_of_diamonds.png'))

    c2c = Card(name='🃒2♣', rank=2, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/2_of_clubs.png'))
    c3c = Card(name='🃓3♣', rank=3, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/3_of_clubs.png'))
    c4c = Card(name='🃔4♣', rank=4, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/4_of_clubs.png'))
    c5c = Card(name='🃕5♣', rank=5, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/5_of_clubs.png'))
    c6c = Card(name='🃖6♣', rank=6, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/6_of_clubs.png'))
    c7c = Card(name='🃗7♣', rank=7, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/7_of_clubs.png'))
    c8c = Card(name='🃘8♣', rank=8, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/8_of_clubs.png'))
    c9c = Card(name='🃙9♣', rank=9, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/9_of_clubs.png'))
    c10c = Card(name='🃚10♣', rank=10, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/10_of_clubs.png'))
    cJc = Card(name='🃛J♣', rank=11, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/jack_of_clubs2.png'))
    cQc = Card(name='🃝Q♣', rank=12, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/queen_of_clubs2.png'))
    cKc = Card(name='🃞K♣', rank=13, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/king_of_clubs2.png'))
    cAc = Card(name='🃑A♣', rank=14, suit='club', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/ace_of_clubs.png'))

    c2s = Card(name='🂢2♤', rank=2, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/2_of_spades.png'))
    c3s = Card(name='🂣3♤', rank=3, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/3_of_spades.png'))
    c4s = Card(name='🂤4♤', rank=4, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/4_of_spades.png'))
    c5s = Card(name='🂥5♤', rank=5, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/5_of_spades.png'))
    c6s = Card(name='🂦6♤', rank=6, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/6_of_spades.png'))
    c7s = Card(name='🂧7♤', rank=7, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/7_of_spades.png'))
    c8s = Card(name='🂨8♤', rank=8, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/8_of_spades.png'))
    c9s = Card(name='🂩9♤', rank=9, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/9_of_spades.png'))
    c10s = Card(name='🂪10♤', rank=10, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/10_of_spades.png'))
    cJs = Card(name='🂫J♤', rank=11, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/jack_of_spades2.png'))
    cQs = Card(name='🂭Q♤', rank=12, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/queen_of_spades2.png'))
    cKs = Card(name='🂮K♤', rank=13, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/king_of_spades2.png'))
    cAs = Card(name='🂡A♤', rank=14, suit='spade', surf=pg.image.load('Lifeboat_Assets/graphics/playing_cards/ace_of_spades.png'))

# ================================================================================================================= #
#                                                     GAME CLASS                                                    #
# ================================================================================================================= #
# Defining Game Class
class Lifeboat:
    deck = [c2h, c3h, c4h, c5h, c6h, c7h, c8h, c9h, c10h, cJh, cQh, cKh, cAh,
            c2d, c3d, c4d, c5d, c6d, c7d, c8d, c9d, c10d, cJd, cQd, cKd, cAd,
            c2c, c3c, c4c, c5c, c6c, c7c, c8c, c9c, c10c, cJc, cQc, cKc, cAc,
            c2s, c3s, c4s, c5s, c6s, c7s, c8s, c9s, c10s, cJs, cQs, cKs, cAs]
    waiting = []
    board1 = []
    board2 = []
    board3 = []
    board4 = []
    holding = None

    def pick_up_card(self,card,pos):
        self.holding = card
        pos.remove(card)
        card.is_held = True

    def put_down_card(self,card,pos):
        pos.insert(0, self.holding)
        card.is_held = False
        self.holding = None

    def validate_put_down(self,card,pos):
        if len(pos) == 0:
                self.put_down_card(card,pos)
                return True
        else:
            if card.rank == pos[0].rank or abs(card.rank - pos[0].rank) == 1:
                self.put_down_card(card,pos)
                return True
            else: return False

    def fill_line(self):
        if len(game.deck) >= 5:
            for n in range(5 - harder - len(game.waiting)):
                game.waiting.insert(0,game.deck[0])
                game.deck.pop(0)
        else:
            for n in range(5 - harder - len(game.waiting)):
                if len(game.deck) == 0:
                    break
                else:
                    game.waiting.insert(0, game.deck[0])
                    game.deck.pop(0)


# Initializing Game Object & Shuffling Deck
game = Lifeboat()
rng.shuffle(game.deck)

def restart():
    global game_active, title, win, lose, boat_is_full, stuck, not_stuck, board1_is_full, board2_is_full, board3_is_full, board4_is_full, time_tick
    game_active = True
    title = False
    win = False
    lose = False
    game.deck = [c2h, c3h, c4h, c5h, c6h, c7h, c8h, c9h, c10h, cJh, cQh, cKh, cAh,
            c2d, c3d, c4d, c5d, c6d, c7d, c8d, c9d, c10d, cJd, cQd, cKd, cAd,
            c2c, c3c, c4c, c5c, c6c, c7c, c8c, c9c, c10c, cJc, cQc, cKc, cAc,
            c2s, c3s, c4s, c5s, c6s, c7s, c8s, c9s, c10s, cJs, cQs, cKs, cAs]
    game.waiting = []
    game.board1 = []
    game.board2 = []
    game.board3 = []
    game.board4 = []
    game.holding = None
    boat_is_full = False
    stuck = False
    not_stuck = True
    boards_to_check = []
    board1_is_full = False; board2_is_full = False; board3_is_full = False; board4_is_full = False
    time_tick = 0
    time = 0
    rng.shuffle(game.deck)

# ================================================================================================================= #
#                                                STARTING VARIABLES                                                 #
# ================================================================================================================= #
if True:
    running = True
    game_active = False
    title = True
    win = False
    lose = False
    rules = False
    music_on = True
    boat_is_full = False
    stuck = False
    not_stuck = True
    auto_fill = False
    boards_to_check = []
    counter = 0
    time_tick = 0
    time = 0
    hard_mode = False
    harder = 0

    board1_is_full = False; board2_is_full = False; board3_is_full = False; board4_is_full = False

    board1_blit_minus1 = False; board1_blit_minus2 = False; board1_blit_minus3 = False; board1_blit_minus4 = False; board1_blit_minus5 = False
    board1_blit_minus6 = False; board1_blit_minus7 = False; board1_blit_minus8 = False; board1_blit_minus9 = False; board1_blit_minus10 = False
    board1_blit_minus11 = False; board1_blit_minus12 = False; board1_blit_minus13 = False; board1_blit_minus14 = False
    board2_blit_minus1 = False; board2_blit_minus2 = False; board2_blit_minus3 = False; board2_blit_minus4 = False; board2_blit_minus5 = False
    board2_blit_minus6 = False; board2_blit_minus7 = False; board2_blit_minus8 = False; board2_blit_minus9 = False; board2_blit_minus10 = False
    board2_blit_minus11 = False; board2_blit_minus12 = False; board2_blit_minus13 = False; board2_blit_minus14 = False
    board3_blit_minus1 = False; board3_blit_minus2 = False; board3_blit_minus3 = False; board3_blit_minus4 = False; board3_blit_minus5 = False
    board3_blit_minus6 = False; board3_blit_minus7 = False; board3_blit_minus8 = False; board3_blit_minus9 = False; board3_blit_minus10 = False
    board3_blit_minus11 = False; board3_blit_minus12 = False; board3_blit_minus13 = False; board3_blit_minus14 = False
    board4_blit_minus1 = False; board4_blit_minus2 = False; board4_blit_minus3 = False; board4_blit_minus4 = False; board4_blit_minus5 = False
    board4_blit_minus6 = False; board4_blit_minus7 = False; board4_blit_minus8 = False; board4_blit_minus9 = False; board4_blit_minus10 = False
    board4_blit_minus11 = False; board4_blit_minus12 = False; board4_blit_minus13 = False; board4_blit_minus14 = False

    # Card Coordinates
    deck_pos = (340,250)
    waiting_pos = (522,250)
    board1_pos = (100,50)
    board2_pos = (762,50)
    board3_pos = (100,450)
    board4_pos = (762,450)

# ================================================================================================================= #
#                                              CARD-SPACE RECTANGLES                                                #
# ================================================================================================================= #
if True:
    # Static Outlines
    deck_marker_surf = pg.Surface((148,210))
    deck_marker_rect = deck_marker_surf.get_rect(topleft = (deck_pos[0]-5, deck_pos[1]-5))
    waiting_marker_surf = pg.Surface((148,210))
    waiting_marker_rect = waiting_marker_surf.get_rect(topleft = (waiting_pos[0]-5, waiting_pos[1]-5))
    board1_marker_surf = pg.Surface((148,210))
    board1_marker_rect = board1_marker_surf.get_rect(topleft = (board1_pos[0]-5, board2_pos[1]-5))
    board2_marker_surf = pg.Surface((148,210))
    board2_marker_rect = board2_marker_surf.get_rect(topleft = (board2_pos[0]-5, board2_pos[1]-5))
    board3_marker_surf = pg.Surface((148,210))
    board3_marker_rect = board3_marker_surf.get_rect(topleft = (board3_pos[0]-5, board3_pos[1]-5))
    board4_marker_surf = pg.Surface((148,210))
    board4_marker_rect = board4_marker_surf.get_rect(topleft = (board4_pos[0]-5, board4_pos[1]-5))

    # Top-Card Rectangles
    deck_topcard_surf = pg.Surface((138,200))
    deck_topcard_rect = deck_topcard_surf.get_rect(topleft=deck_pos)
    waiting_topcard_surf = pg.Surface((138, 200))
    waiting_topcard_rect = deck_topcard_surf.get_rect(topleft=waiting_pos)
    board1_topcard_surf = pg.Surface((138,200))
    board1_topcard_rect = board1_topcard_surf.get_rect(topleft = board1_pos)
    board2_topcard_surf = pg.Surface((138, 200))
    board2_topcard_rect = board1_topcard_surf.get_rect(topleft=board2_pos)
    board3_topcard_surf = pg.Surface((138, 200))
    board3_topcard_rect = board1_topcard_surf.get_rect(topleft=board3_pos)
    board4_topcard_surf = pg.Surface((138, 200))
    board4_topcard_rect = board1_topcard_surf.get_rect(topleft=board4_pos)

# ================================================================================================================= #
#                                              BUTTONS, STATS, SCREENS                                              #
# ================================================================================================================= #
if True:
    # Stats Text
    remaining_text = font.render(f'Left to save: {len(game.deck)}',True,'White')
    waiting_text = font.render(f'Awaiting spots: {len(game.waiting)}',True,'White')
    boat1_text = font.render(f'Seats left: {15 - harder - len(game.board1)}',True,'White')
    boat2_text = font.render(f'Seats left: {15 - harder - len(game.board2)}', True, 'White')
    boat3_text = font.render(f'Seats left: {15 - harder - len(game.board3)}', True, 'White')
    boat4_text = font.render(f'Seats left: {15 - harder - len(game.board4)}', True, 'White')
    unsaved_text = font.render(f"Passenger Manifest:",True,'White')
    unsaved_card_pos = (300,690)
    stuck_text = bigfont.render(f'STUCK!',True,(149,0,49))
    fullboat_text = bigfont.render(f'FULL!',True,(149,0,49))

    # Rules button
    rules_button_text = font.render('RULES',True,'White')
    rules_button_surf = pg.Surface((100,50)); rules_button_surf.fill('Blue')
    rules_button_rect = rules_button_surf.get_rect(topleft = (360,140))

    # Restart Button
    restart_button_text = font.render('RESTART',True,'White')
    restart_button_surf = pg.Surface((120,50)); restart_button_surf.fill('Brown4')
    restart_button_rect = restart_button_surf.get_rect(topleft = (535,140))

    # Fill Waiting Button
    fill_button_text = font.render('Fill Line', True, 'White')
    fill_button_surf = pg.Surface((90,50)); fill_button_surf.fill('brown')
    fill_button_rect = fill_button_surf.get_rect(topleft = (685,325))

    # Auto Fill Button
    auto_button_text = font.render('Auto-Fill',True,'White')
    auto_button_surf = pg.Surface((100,50)); auto_button_surf.fill('brown')
    auto_button_rect = auto_button_surf.get_rect(topleft = (800,325))

    # Music On/Off Button
    music_button_surf = pg.image.load('Lifeboat_Assets/graphics/music_symbol.png')
    music_button_surf = pg.transform.scale(music_button_surf,(40,40))
    music_button_rect = music_button_surf.get_rect(topleft = (925,725))
    music_off_surf = pg.image.load('Lifeboat_Assets/graphics/cancel.png')
    music_off_surf = pg.transform.scale(music_off_surf,(20,20))
    music_off_rect = music_off_surf.get_rect(topleft = (925,725))

    # Time/Score
    time_text = bigfont.render(f"You saved everyone in {time} seconds!",True,'Yellow')

    # Hard Mode Button & Mode Button Toggle

    mode_button_text = font.render(f'Hard Mode',True,'White')
    mode_button_surf = pg.Surface((130,30)); mode_button_surf.fill('Brown')
    mode_button_rect = mode_button_surf.get_rect(bottomleft = (10,760))
    hard_win_text = bigfont.render(f'Congratulations, you beat Hard Mode!',True,'Yellow')

    # Title, Rules, Win and Lose Screens
    title_surf = pg.image.load('Lifeboat_Assets/graphics/lifeboat_title.png')
    rules_surf = pg.image.load('Lifeboat_Assets/graphics/lifeboat_rules.png')
    win_surf = pg.image.load('Lifeboat_Assets/graphics/lifeboat_win.png')
    lose_surf = pg.image.load('Lifeboat_Assets/graphics/lifeboat_lose.png')


# Game Loop
while running:
    # ============================================================================================================= #
    #                                                EVENT LOOP                                                     #
    # ============================================================================================================= #
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        else:
            # Closing the title screen
            mouse_pos = pg.mouse.get_pos()
            if title:
                if event.type == pg.MOUSEBUTTONDOWN:
                    title = False
                    game_active = True

            else:
                # Showing Boat Cards on Mouseover
                if event.type == pg.MOUSEMOTION:
                    # Warning of about to lose
                    if len(game.board1) == 15 - harder and 100<= mouse_pos[0] <= 238 and 50 <= mouse_pos[1] <= 250: boat_is_full = True
                    elif len(game.board3) == 15 - harder and 100 <= mouse_pos[0] <= 238 and 450 <= mouse_pos[1] <= 650: boat_is_full = True
                    elif len(game.board2) == 15 - harder and 762 <= mouse_pos[0] <= 900 and 50<= mouse_pos[1] <= 250: boat_is_full = True
                    elif len(game.board4) == 15 - harder and 762 <= mouse_pos[0] <= 900 and 450 <= mouse_pos[1] <= 650: boat_is_full = True
                    else: boat_is_full = False

                    # Revealing Boat Cards on Mouse-over
                    if 100 <= mouse_pos[0] <= 238:
                        # Boat 1
                        if 50 <= mouse_pos[1] < 53 and len(game.board1) > 1: board1_blit_minus1 = True
                        else: board1_blit_minus1 = False
                        if 53 <= mouse_pos[1] < 56 and len(game.board1) > 2: board1_blit_minus2 = True
                        else: board1_blit_minus2 = False
                        if 56 <= mouse_pos[1] < 59 and len(game.board1) > 3: board1_blit_minus3 = True
                        else: board1_blit_minus3 = False
                        if 59 <= mouse_pos[1] < 62 and len(game.board1) > 4: board1_blit_minus4 = True
                        else: board1_blit_minus4 = False
                        if 62 <= mouse_pos[1] < 65 and len(game.board1) > 5: board1_blit_minus5 = True
                        else: board1_blit_minus5 = False
                        if 65 <= mouse_pos[1] < 68 and len(game.board1) > 6: board1_blit_minus6 = True
                        else: board1_blit_minus6 = False
                        if 68 <= mouse_pos[1] < 71 and len(game.board1) > 7: board1_blit_minus7 = True
                        else: board1_blit_minus7 = False
                        if 71 <= mouse_pos[1] < 74 and len(game.board1) > 8: board1_blit_minus8 = True
                        else: board1_blit_minus8 = False
                        if 74 <= mouse_pos[1] < 77 and len(game.board1) > 9: board1_blit_minus9 = True
                        else: board1_blit_minus9 = False
                        if 77 <= mouse_pos[1] < 80 and len(game.board1) > 10: board1_blit_minus10 = True
                        else: board1_blit_minus10 = False
                        if 80 <= mouse_pos[1] < 83 and len(game.board1) > 11: board1_blit_minus11 = True
                        else: board1_blit_minus11 = False
                        if 83 <= mouse_pos[1] < 86 and len(game.board1) > 12: board1_blit_minus12 = True
                        else: board1_blit_minus12 = False
                        if 86 <= mouse_pos[1] < 89 and len(game.board1) > 13: board1_blit_minus13 = True
                        else: board1_blit_minus13 = False
                        if 89 <= mouse_pos[1] < 92 and len(game.board1) > 14: board1_blit_minus14 = True
                        else: board1_blit_minus14 = False
                        
                        # Boat 3
                        if 450 <= mouse_pos[1] < 453 and len(game.board3) > 1: board3_blit_minus1 = True
                        else: board3_blit_minus1 = False
                        if 453 <= mouse_pos[1] < 456 and len(game.board3) > 2: board3_blit_minus2 = True
                        else: board3_blit_minus2 = False
                        if 456 <= mouse_pos[1] < 459 and len(game.board3) > 3: board3_blit_minus3 = True
                        else: board3_blit_minus3 = False
                        if 459 <= mouse_pos[1] < 462 and len(game.board3) > 4: board3_blit_minus4 = True
                        else: board3_blit_minus4 = False
                        if 462 <= mouse_pos[1] < 465 and len(game.board3) > 5: board3_blit_minus5 = True
                        else: board3_blit_minus5 = False
                        if 465 <= mouse_pos[1] < 468 and len(game.board3) > 6: board3_blit_minus6 = True
                        else: board3_blit_minus6 = False
                        if 468 <= mouse_pos[1] < 471 and len(game.board3) > 7: board3_blit_minus7 = True
                        else: board3_blit_minus7 = False
                        if 471 <= mouse_pos[1] < 474 and len(game.board3) > 8: board3_blit_minus8 = True
                        else: board3_blit_minus8 = False
                        if 474 <= mouse_pos[1] < 477 and len(game.board3) > 9: board3_blit_minus9 = True
                        else: board3_blit_minus9 = False
                        if 477 <= mouse_pos[1] < 480 and len(game.board3) > 10: board3_blit_minus10 = True
                        else: board3_blit_minus10 = False
                        if 480 <= mouse_pos[1] < 483 and len(game.board3) > 11: board3_blit_minus11 = True
                        else: board3_blit_minus11 = False
                        if 483 <= mouse_pos[1] < 486 and len(game.board3) > 12: board3_blit_minus12 = True
                        else: board3_blit_minus12 = False
                        if 486 <= mouse_pos[1] < 489 and len(game.board3) > 13: board3_blit_minus13 = True
                        else: board3_blit_minus13 = False
                        if 489 <= mouse_pos[1] < 492 and len(game.board3) > 14: board3_blit_minus14 = True
                        else: board3_blit_minus14 = False
                    else: 
                        board1_blit_minus1 = False; board1_blit_minus2 = False; board1_blit_minus3 = False; board1_blit_minus4 = False
                        board1_blit_minus5 = False; board1_blit_minus6 = False; board1_blit_minus7 = False; board1_blit_minus8 = False
                        board1_blit_minus9 = False; board1_blit_minus10 = False; board1_blit_minus11 = False; board1_blit_minus12 = False
                        board1_blit_minus13 = False; board1_blit_minus14 = False
                        board3_blit_minus1 = False; board3_blit_minus2 = False; board3_blit_minus3 = False; board3_blit_minus4 = False
                        board3_blit_minus5 = False; board3_blit_minus6 = False; board3_blit_minus7 = False; board3_blit_minus8 = False
                        board3_blit_minus9 = False; board3_blit_minus10 = False; board3_blit_minus11 = False; board3_blit_minus12 = False
                        board3_blit_minus13 = False; board3_blit_minus14 = False

                    if 762 <= mouse_pos[0] <= 900:
                        # Board 2
                        if 50 <= mouse_pos[1] < 53 and len(game.board2) > 1: board2_blit_minus1 = True
                        else: board2_blit_minus1 = False
                        if 53 <= mouse_pos[1] < 56 and len(game.board2) > 2: board2_blit_minus2 = True
                        else: board2_blit_minus2 = False
                        if 56 <= mouse_pos[1] < 59 and len(game.board2) > 3: board2_blit_minus3 = True
                        else: board2_blit_minus3 = False
                        if 59 <= mouse_pos[1] < 62 and len(game.board2) > 4: board2_blit_minus4 = True
                        else: board2_blit_minus4 = False
                        if 62 <= mouse_pos[1] < 65 and len(game.board2) > 5: board2_blit_minus5 = True
                        else: board2_blit_minus5 = False
                        if 65 <= mouse_pos[1] < 68 and len(game.board2) > 6: board2_blit_minus6 = True
                        else: board2_blit_minus6 = False
                        if 68 <= mouse_pos[1] < 71 and len(game.board2) > 7: board2_blit_minus7 = True
                        else: board2_blit_minus7 = False
                        if 71 <= mouse_pos[1] < 74 and len(game.board2) > 8: board2_blit_minus8 = True
                        else: board2_blit_minus8 = False
                        if 74 <= mouse_pos[1] < 77 and len(game.board2) > 9: board2_blit_minus9 = True
                        else: board2_blit_minus9 = False
                        if 77 <= mouse_pos[1] < 80 and len(game.board2) > 10: board2_blit_minus10 = True
                        else: board2_blit_minus10 = False
                        if 80 <= mouse_pos[1] < 83 and len(game.board2) > 11: board2_blit_minus11 = True
                        else: board2_blit_minus11 = False
                        if 83 <= mouse_pos[1] < 86 and len(game.board2) > 12: board2_blit_minus12 = True
                        else: board2_blit_minus12 = False
                        if 86 <= mouse_pos[1] < 89 and len(game.board2) > 13: board2_blit_minus13 = True
                        else: board2_blit_minus13 = False
                        if 89 <= mouse_pos[1] < 92 and len(game.board2) > 14: board2_blit_minus14 = True
                        else: board2_blit_minus14 = False

                        # Board 4
                        if 450 <= mouse_pos[1] < 453 and len(game.board4) > 1: board4_blit_minus1 = True
                        else: board4_blit_minus1 = False
                        if 453 <= mouse_pos[1] < 456 and len(game.board4) > 2: board4_blit_minus2 = True
                        else: board4_blit_minus2 = False
                        if 456 <= mouse_pos[1] < 459 and len(game.board4) > 3: board4_blit_minus3 = True
                        else: board4_blit_minus3 = False
                        if 459 <= mouse_pos[1] < 462 and len(game.board4) > 4: board4_blit_minus4 = True
                        else: board4_blit_minus4 = False
                        if 462 <= mouse_pos[1] < 465 and len(game.board4) > 5: board4_blit_minus5 = True
                        else: board4_blit_minus5 = False
                        if 465 <= mouse_pos[1] < 468 and len(game.board4) > 6: board4_blit_minus6 = True
                        else: board4_blit_minus6 = False
                        if 468 <= mouse_pos[1] < 471 and len(game.board4) > 7: board4_blit_minus7 = True
                        else: board4_blit_minus7 = False
                        if 471 <= mouse_pos[1] < 474 and len(game.board4) > 8: board4_blit_minus8 = True
                        else: board4_blit_minus8 = False
                        if 474 <= mouse_pos[1] < 477 and len(game.board4) > 9: board4_blit_minus9 = True
                        else: board4_blit_minus9 = False
                        if 477 <= mouse_pos[1] < 480 and len(game.board4) > 10: board4_blit_minus10 = True
                        else: board4_blit_minus10 = False
                        if 480 <= mouse_pos[1] < 483 and len(game.board4) > 11: board4_blit_minus11 = True
                        else: board4_blit_minus11 = False
                        if 483 <= mouse_pos[1] < 486 and len(game.board4) > 12: board4_blit_minus12 = True
                        else: board4_blit_minus12 = False
                        if 486 <= mouse_pos[1] < 489 and len(game.board4) > 13: board4_blit_minus13 = True
                        else: board4_blit_minus13 = False
                        if 489 <= mouse_pos[1] < 492 and len(game.board4) > 14: board4_blit_minus14 = True
                        else: board4_blit_minus14 = False
                    else:
                        board2_blit_minus1 = False; board2_blit_minus2 = False; board2_blit_minus3 = False; board2_blit_minus4 = False
                        board2_blit_minus5 = False; board2_blit_minus6 = False; board2_blit_minus7 = False; board2_blit_minus8 = False
                        board2_blit_minus9 = False; board2_blit_minus10 = False; board2_blit_minus11 = False; board2_blit_minus12 = False
                        board2_blit_minus13 = False; board2_blit_minus14 = False
                        board4_blit_minus1 = False; board4_blit_minus2 = False; board4_blit_minus3 = False; board4_blit_minus4 = False
                        board4_blit_minus5 = False; board4_blit_minus6 = False; board4_blit_minus7 = False; board4_blit_minus8 = False
                        board4_blit_minus9 = False; board4_blit_minus10 = False; board4_blit_minus11 = False; board4_blit_minus12 = False
                        board4_blit_minus13 = False; board4_blit_minus14 = False
                        
                # Clicking Buttons
                if event.type == pg.MOUSEBUTTONDOWN:
                    if rules: rules = False
                    if rules_button_rect.collidepoint(mouse_pos):
                        rules = True
                    if auto_button_rect.collidepoint(mouse_pos) and not auto_fill and counter > 5:
                        counter = 0
                        auto_fill = True
                    if auto_button_rect.collidepoint(mouse_pos) and auto_fill and counter > 5:
                        counter = 0
                        auto_fill = False
                    if fill_button_rect.collidepoint(mouse_pos) and not game.holding and game.waiting != 5 - harder:
                        game.fill_line()
                    if music_button_rect.collidepoint(mouse_pos) and not music_on and counter > 5:
                        counter = 0
                        music_on = True
                        music_sound.play(-1)
                    if music_button_rect.collidepoint(mouse_pos) and music_on and counter > 5:
                        counter = 0
                        music_on = False
                        music_sound.stop()
                    if mode_button_rect.collidepoint(mouse_pos) and not title and not rules:
                        if hard_mode and counter > 5:
                            hard_mode = False
                            harder = 0
                            counter = 0
                            restart()
                        elif not hard_mode and counter > 5:
                            hard_mode = True
                            harder = 1
                            counter = 0
                            restart()
                if event.type == pg.MOUSEBUTTONUP:
                    if restart_button_rect.collidepoint(mouse_pos) and not title and not rules:
                        counter = 0
                        lose = True
                        game_active = False


                # Picking up cards
                if event.type == pg.MOUSEBUTTONDOWN and not game.holding and counter > 5:
                    counter = 0
                    if len(game.deck) > 0 and len(game.waiting) < 5 - harder:
                        if deck_topcard_rect.collidepoint(mouse_pos):
                            game.pick_up_card(game.deck[0],game.deck)
                    if len(game.waiting) > 0:
                        if waiting_topcard_rect.collidepoint(mouse_pos):
                            game.pick_up_card(game.waiting[0],game.waiting)
                        elif len(game.waiting) > 1 and 525 < mouse_pos[0] < 660:
                            if 250 < mouse_pos[1] < 279:
                                game.pick_up_card(game.waiting[-1],game.waiting)
                            if 280 < mouse_pos[1] < 309:
                                game.pick_up_card(game.waiting[-2],game.waiting)
                            if 310 < mouse_pos[1] < 339:
                                game.pick_up_card(game.waiting[-3],game.waiting)
                            if 340 < mouse_pos[1] < 369:
                                game.pick_up_card(game.waiting[-4],game.waiting)

                # Updating card position to follow the mouse
                if event.type == pg.MOUSEMOTION and game.holding:
                    game.holding.update_position(mouse_pos)

                # Placing cards down in waiting or in boats
                if event.type == pg.MOUSEBUTTONDOWN and game.holding and counter > 5:
                    counter = 0
                    if waiting_marker_rect.collidepoint(mouse_pos) or waiting_topcard_rect.collidepoint(mouse_pos):
                            game.put_down_card(game.holding,game.waiting)
                    if (board1_marker_rect.collidepoint(mouse_pos) or board1_topcard_rect.collidepoint(mouse_pos)) and not len(game.board1) == 15 - harder:
                        game.validate_put_down(game.holding,game.board1)
                    if (board2_marker_rect.collidepoint(mouse_pos) or board2_topcard_rect.collidepoint(mouse_pos)) and not len(game.board2) == 15 - harder:
                        game.validate_put_down(game.holding, game.board2)
                    if (board3_marker_rect.collidepoint(mouse_pos) or board3_topcard_rect.collidepoint(mouse_pos)) and not len(game.board3) == 15 - harder:
                        game.validate_put_down(game.holding, game.board3)
                    if (board4_marker_rect.collidepoint(mouse_pos) or board4_topcard_rect.collidepoint(mouse_pos)) and not len(game.board4) == 15 - harder:
                        game.validate_put_down(game.holding, game.board4)

            # Replaying game after win/lose
            if not game_active:
                if event.type == pg.MOUSEBUTTONDOWN:
                    restart()

# ============================================================================================================= #
#                                               BLITTING SURFACES                                               #
# ============================================================================================================= #

    if game_active and running == True:
        if not stuck:
            time_tick += 1
            time = time_tick // 60
        counter += 1
        if rules: screen.blit(rules_surf,(0,0))
        else:
            # Background
            screen.fill((69, 145, 19))

            # Blitting Board Markers
            pg.draw.rect(screen, 'White', deck_marker_rect, 6, 20)
            pg.draw.rect(screen, 'White', waiting_marker_rect, 6, 20)
            pg.draw.rect(screen,'White',board1_marker_rect,6,20)
            pg.draw.rect(screen, 'White', board2_marker_rect, 6, 20)
            pg.draw.rect(screen, 'White', board3_marker_rect, 6, 20)
            pg.draw.rect(screen, 'White', board4_marker_rect, 6, 20)

            # Blitting Deck
            y = 0
            for n in game.deck:
                screen.blit(cBack.surf, (deck_pos[0],deck_pos[1] + y))
                deck_topcard_rect.y = deck_pos[1] + y
                y += 2

            # Blitting Waiting
            y = 0; x = -1
            for n in game.waiting:
                screen.blit(game.waiting[x].surf, (waiting_pos[0],waiting_pos[1] + y))
                waiting_topcard_rect.y = waiting_pos[1] + y
                x -= 1
                y += 30

            # Blitting Lifeboats
            y = 0
            for n in game.board1:
                screen.blit(game.board1[0].surf, (board1_pos[0],board1_pos[1]+y))
                board1_topcard_rect.y = board1_pos[1] + y
                y += 3
            y = 0
            for n in game.board2:
                screen.blit(game.board2[0].surf, (board2_pos[0],board2_pos[1]+y))
                board2_topcard_rect.y = board2_pos[1] + y
                y += 3
            y = 0
            for n in game.board3:
                screen.blit(game.board3[0].surf, (board3_pos[0],board3_pos[1]+y))
                board3_topcard_rect.y = board3_pos[1] + y
                y += 3
            y = 0
            for n in game.board4:
                screen.blit(game.board4[0].surf, (board4_pos[0],board4_pos[1]+y))
                board4_topcard_rect.y = board4_pos[1] + y
                y += 3

            # Updating and Blitting Stats
            remaining_text = font.render(f'Onboard: {len(game.deck)}', True, 'White')
            waiting_text = font.render(f'In line: {len(game.waiting)}', True, 'White')
            screen.blit(remaining_text,(345,210))
            screen.blit(waiting_text,(550,210))
            pg.draw.line(screen, 'white', (500,200),(500,235),3)
            boat1_text = font.render(f'Seats left: {15 - harder - len(game.board1)}', True, 'White')
            screen.blit(boat1_text,(250,80))
            boat2_text = font.render(f'Seats left: {15 - harder - len(game.board2)}', True, 'White')
            screen.blit(boat2_text, (620, 80))
            boat3_text = font.render(f'Seats left: {15 - harder - len(game.board3)}', True, 'White')
            screen.blit(boat3_text, (250, 600))
            boat4_text = font.render(f'Seats left: {15 - harder - len(game.board4)}', True, 'White')
            screen.blit(boat4_text, (620, 600))

            # Unsaved Counter
            screen.blit(unsaved_text, (390,640))
            # Counting the number of unsaved cards
            if True:
                num_A = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 14)
                num_K = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 13)
                num_Q = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 12)
                num_J = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 11)
                num_10 = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 10)
                num_9 = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 9)
                num_8 = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 8)
                num_7 = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 7)
                num_6 = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 6)
                num_5 = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 5)
                num_4 = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 4)
                num_3 = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 3)
                num_2 = sum(1 for n in chain(game.deck, game.waiting, [game.holding] if game.holding else []) if n.rank == 2)

                unsaved_A = font.render("A " * num_A,True,'White')
                unsaved_K = font.render("K " * num_K, True, 'White')
                unsaved_Q = font.render("Q " * num_Q, True, 'White')
                unsaved_J = font.render("J " * num_J, True, 'White')
                unsaved_10 = font.render("T " * num_10, True, 'White')
                unsaved_9 = font.render("9 " * num_9, True, 'White')
                unsaved_8 = font.render("8 " * num_8, True, 'White')
                unsaved_7 = font.render("7 " * num_7, True, 'White')
                unsaved_6 = font.render("6 " * num_6, True, 'White')
                unsaved_5 = font.render("5 " * num_5, True, 'White')
                unsaved_4 = font.render("4 " * num_4, True, 'White')
                unsaved_3 = font.render("3 " * num_3, True, 'White')
                unsaved_2 = font.render("2 " * num_2, True, 'White')

                screen.blit(unsaved_A,(unsaved_card_pos[0]+150,unsaved_card_pos[1]-25))
                screen.blit(unsaved_K,(unsaved_card_pos[0],unsaved_card_pos[1]))
                screen.blit(unsaved_Q, (unsaved_card_pos[0]+100,unsaved_card_pos[1]))
                screen.blit(unsaved_J, (unsaved_card_pos[0] + 200, unsaved_card_pos[1]))
                screen.blit(unsaved_10, (unsaved_card_pos[0] + 300, unsaved_card_pos[1]))
                screen.blit(unsaved_9, (unsaved_card_pos[0] + 0, unsaved_card_pos[1]+25))
                screen.blit(unsaved_8, (unsaved_card_pos[0] + 100, unsaved_card_pos[1]+25))
                screen.blit(unsaved_7, (unsaved_card_pos[0] + 200, unsaved_card_pos[1]+25))
                screen.blit(unsaved_6, (unsaved_card_pos[0] + 300, unsaved_card_pos[1]+25))
                screen.blit(unsaved_5, (unsaved_card_pos[0] + 0, unsaved_card_pos[1] + 50))
                screen.blit(unsaved_4, (unsaved_card_pos[0] + 100, unsaved_card_pos[1] + 50))
                screen.blit(unsaved_3, (unsaved_card_pos[0] + 200, unsaved_card_pos[1] + 50))
                screen.blit(unsaved_2, (unsaved_card_pos[0] + 300, unsaved_card_pos[1] + 50))

            # Blitting Buttons
            screen.blit(rules_button_surf,rules_button_rect)
            screen.blit(rules_button_text,(rules_button_rect.x + 15,rules_button_rect.y + 15))
            screen.blit(restart_button_surf,restart_button_rect)
            screen.blit(restart_button_text,(restart_button_rect.x + 15, restart_button_rect.y + 15))
            screen.blit(fill_button_surf,fill_button_rect)
            screen.blit(fill_button_text,(fill_button_rect.x + 6,fill_button_rect.y +15))
            screen.blit(auto_button_surf,auto_button_rect)
            screen.blit(auto_button_text,(auto_button_rect.x + 6, auto_button_rect.y + 15))
            screen.blit(music_button_surf,music_button_rect)
            if not music_on:
                screen.blit(music_off_surf,music_off_rect)


            # Display STUCK!
            if len(game.board1) == 15 - harder: board1_is_full = True
            if len(game.board2) == 15 - harder: board2_is_full = True
            if len(game.board3) == 15 - harder: board3_is_full = True
            if len(game.board4) == 15 - harder: board4_is_full = True
            if len(game.board1) > 0 and len(game.board2) > 0 and len(game.board3) > 0 and len(game.board4) > 0:
                boards_to_check = [game.board1[0], game.board2[0], game.board3[0],game.board4[0]]

            if board1_is_full: boards_to_check.remove(game.board1[0])
            if board2_is_full: boards_to_check.remove(game.board2[0])
            if board3_is_full: boards_to_check.remove(game.board3[0])
            if board4_is_full: boards_to_check.remove(game.board4[0])

            if len(game.deck) == 0:
                stuck = True
                for m in (boards_to_check):
                    for n in game.waiting:
                        if abs(n.rank - m.rank) <= 1:
                            stuck = False
                    if game.holding:
                        if abs(game.holding.rank - m.rank) <= 1:
                            stuck = False
            elif len(game.waiting) == 5 - harder and 0 < len(game.board1) and 0 < len(game.board2) and 0 < len(game.board3) and 0 < len(game.board4):
                stuck = True
                for m in (boards_to_check):
                    for n in game.waiting:
                        if abs(n.rank - m.rank) <= 1:
                            stuck = False

            if stuck:
                screen.blit(stuck_text, (400, 20))

            # Display FULL!
            if boat_is_full == True:
                screen.blit(fullboat_text,(430, 70))

            # Timer
            if hard_mode: timer_text = font.render(f'Sinking in {200 - time} seconds!', True, 'White')
            else: timer_text = font.render(f'Time elapsed: {time} seconds...',True,'White')
            screen.blit(timer_text,(10,770))

            # Blit Mode Switch Button
            if hard_mode: mode_button_text = font.render(f'Hard Mode', True, 'White')
            if not hard_mode: mode_button_text = font.render(f'Easy Mode',True,'White')
            screen.blit(mode_button_surf,mode_button_rect)
            screen.blit(mode_button_text,(mode_button_rect.x + 10, mode_button_rect.y +6))

            # Blitting Held Card
            if game.holding:
                screen.blit(game.holding.surf,(mouse_pos[0]-69,mouse_pos[1]-100))

            # Blitting mouseovers
            # Board 1 mouseovers
            if True:
                if board1_blit_minus1 == True: screen.blit(game.board1[-1].surf, (board1_pos[0], board1_pos[1]))
                if board1_blit_minus2 == True: screen.blit(game.board1[-2].surf, (board1_pos[0], board1_pos[1]+3))
                if board1_blit_minus3 == True: screen.blit(game.board1[-3].surf, (board1_pos[0], board1_pos[1]+6))
                if board1_blit_minus4 == True: screen.blit(game.board1[-4].surf, (board1_pos[0], board1_pos[1]+9))
                if board1_blit_minus5 == True: screen.blit(game.board1[-5].surf, (board1_pos[0], board1_pos[1]+12))
                if board1_blit_minus6 == True: screen.blit(game.board1[-6].surf, (board1_pos[0], board1_pos[1]+15))
                if board1_blit_minus7 == True: screen.blit(game.board1[-7].surf, (board1_pos[0], board1_pos[1]+18))
                if board1_blit_minus8 == True: screen.blit(game.board1[-8].surf, (board1_pos[0], board1_pos[1]+21))
                if board1_blit_minus9 == True: screen.blit(game.board1[-9].surf, (board1_pos[0], board1_pos[1]+24))
                if board1_blit_minus10 == True: screen.blit(game.board1[-10].surf, (board1_pos[0], board1_pos[1]+27))
                if board1_blit_minus11 == True: screen.blit(game.board1[-11].surf, (board1_pos[0], board1_pos[1]+30))
                if board1_blit_minus12 == True: screen.blit(game.board1[-12].surf, (board1_pos[0], board1_pos[1]+33))
                if board1_blit_minus13 == True: screen.blit(game.board1[-13].surf, (board1_pos[0], board1_pos[1]+36))
                if board1_blit_minus14 == True: screen.blit(game.board1[-14].surf, (board1_pos[0], board1_pos[1]+39))
                
                if board2_blit_minus1 == True: screen.blit(game.board2[-1].surf, (board2_pos[0], board2_pos[1]))
                if board2_blit_minus2 == True: screen.blit(game.board2[-2].surf, (board2_pos[0], board2_pos[1]+3))
                if board2_blit_minus3 == True: screen.blit(game.board2[-3].surf, (board2_pos[0], board2_pos[1]+6))
                if board2_blit_minus4 == True: screen.blit(game.board2[-4].surf, (board2_pos[0], board2_pos[1]+9))
                if board2_blit_minus5 == True: screen.blit(game.board2[-5].surf, (board2_pos[0], board2_pos[1]+12))
                if board2_blit_minus6 == True: screen.blit(game.board2[-6].surf, (board2_pos[0], board2_pos[1]+15))
                if board2_blit_minus7 == True: screen.blit(game.board2[-7].surf, (board2_pos[0], board2_pos[1]+18))
                if board2_blit_minus8 == True: screen.blit(game.board2[-8].surf, (board2_pos[0], board2_pos[1]+21))
                if board2_blit_minus9 == True: screen.blit(game.board2[-9].surf, (board2_pos[0], board2_pos[1]+24))
                if board2_blit_minus10 == True: screen.blit(game.board2[-10].surf, (board2_pos[0], board2_pos[1]+27))
                if board2_blit_minus11 == True: screen.blit(game.board2[-11].surf, (board2_pos[0], board2_pos[1]+30))
                if board2_blit_minus12 == True: screen.blit(game.board2[-12].surf, (board2_pos[0], board2_pos[1]+33))
                if board2_blit_minus13 == True: screen.blit(game.board2[-13].surf, (board2_pos[0], board2_pos[1]+36))
                if board2_blit_minus14 == True: screen.blit(game.board2[-14].surf, (board2_pos[0], board2_pos[1]+39))
                
                if board3_blit_minus1 == True: screen.blit(game.board3[-1].surf, (board3_pos[0], board3_pos[1]))
                if board3_blit_minus2 == True: screen.blit(game.board3[-2].surf, (board3_pos[0], board3_pos[1]+3))
                if board3_blit_minus3 == True: screen.blit(game.board3[-3].surf, (board3_pos[0], board3_pos[1]+6))
                if board3_blit_minus4 == True: screen.blit(game.board3[-4].surf, (board3_pos[0], board3_pos[1]+9))
                if board3_blit_minus5 == True: screen.blit(game.board3[-5].surf, (board3_pos[0], board3_pos[1]+12))
                if board3_blit_minus6 == True: screen.blit(game.board3[-6].surf, (board3_pos[0], board3_pos[1]+15))
                if board3_blit_minus7 == True: screen.blit(game.board3[-7].surf, (board3_pos[0], board3_pos[1]+18))
                if board3_blit_minus8 == True: screen.blit(game.board3[-8].surf, (board3_pos[0], board3_pos[1]+21))
                if board3_blit_minus9 == True: screen.blit(game.board3[-9].surf, (board3_pos[0], board3_pos[1]+24))
                if board3_blit_minus10 == True: screen.blit(game.board3[-10].surf, (board3_pos[0], board3_pos[1]+27))
                if board3_blit_minus11 == True: screen.blit(game.board3[-11].surf, (board3_pos[0], board3_pos[1]+30))
                if board3_blit_minus12 == True: screen.blit(game.board3[-12].surf, (board3_pos[0], board3_pos[1]+33))
                if board3_blit_minus13 == True: screen.blit(game.board3[-13].surf, (board3_pos[0], board3_pos[1]+36))
                if board3_blit_minus14 == True: screen.blit(game.board3[-14].surf, (board3_pos[0], board3_pos[1]+39))
                
                if board4_blit_minus1 == True: screen.blit(game.board4[-1].surf, (board4_pos[0], board4_pos[1]))
                if board4_blit_minus2 == True: screen.blit(game.board4[-2].surf, (board4_pos[0], board4_pos[1]+3))
                if board4_blit_minus3 == True: screen.blit(game.board4[-3].surf, (board4_pos[0], board4_pos[1]+6))
                if board4_blit_minus4 == True: screen.blit(game.board4[-4].surf, (board4_pos[0], board4_pos[1]+9))
                if board4_blit_minus5 == True: screen.blit(game.board4[-5].surf, (board4_pos[0], board4_pos[1]+12))
                if board4_blit_minus6 == True: screen.blit(game.board4[-6].surf, (board4_pos[0], board4_pos[1]+15))
                if board4_blit_minus7 == True: screen.blit(game.board4[-7].surf, (board4_pos[0], board4_pos[1]+18))
                if board4_blit_minus8 == True: screen.blit(game.board4[-8].surf, (board4_pos[0], board4_pos[1]+21))
                if board4_blit_minus9 == True: screen.blit(game.board4[-9].surf, (board4_pos[0], board4_pos[1]+24))
                if board4_blit_minus10 == True: screen.blit(game.board4[-10].surf, (board4_pos[0], board4_pos[1]+27))
                if board4_blit_minus11 == True: screen.blit(game.board4[-11].surf, (board4_pos[0], board4_pos[1]+30))
                if board4_blit_minus12 == True: screen.blit(game.board4[-12].surf, (board4_pos[0], board4_pos[1]+33))
                if board4_blit_minus13 == True: screen.blit(game.board4[-13].surf, (board4_pos[0], board4_pos[1]+36))
                if board4_blit_minus14 == True: screen.blit(game.board4[-14].surf, (board4_pos[0], board4_pos[1]+39))

        # Auto-Fill
        if auto_fill and not game.holding and game.waiting != 5 - harder:
            game.fill_line()

    if running:
        # Updating time text
        win_text = bigfont.render(f"You saved everyone in {time} seconds!", True, 'Yellow')
        lose_text = bigfont.render(f"The ship sank in {time} seconds!", True, (30,181,173))

        # Winning
        if len(game.deck) == 0 and len(game.waiting) == 0 and not game.holding:
            game_active = False
            win = True
        # Losing
        if hard_mode and time >= 200:
            game_active = False
            lose = True

        # Blitting Screens
        if not game_active:
            if title:
                screen.blit(title_surf,(0,0))
            elif win:
                screen.blit(win_surf,(0,0))
                screen.blit(win_text,(60,700))
                if hard_mode:
                    screen.blit(hard_win_text,(20,620))

            elif lose:
                screen.blit(lose_surf,(0,0))
                screen.blit(lose_text,(150,700))
        # Updating display and limiting FPS
        pg.display.flip()
        clock.tick(60)
# ================================================================================================================= #
#                                                     end of code                                                   #
# ================================================================================================================= #
pg.quit()
sys.exit()