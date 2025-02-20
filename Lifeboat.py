# ================================================================================================================= #
#                                                    start of code                                                  #
# ================================================================================================================= #
import random as rng
from itertools import chain
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

music_sound = pg.mixer.Sound('audio/lifeboat_music.mp3')
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
    cBack = Card(name='back', rank=0, suit='none', surf=pg.image.load('graphics/playing_cards/card_back.png'))

    c2h = Card(name='🂲2♥', rank=2, suit='heart', surf=pg.image.load('graphics/playing_cards/2_of_hearts.png'))
    c3h = Card(name='🂳3♥', rank=3, suit='heart', surf=pg.image.load('graphics/playing_cards/3_of_hearts.png'))
    c4h = Card(name='🂴4♥', rank=4, suit='heart', surf=pg.image.load('graphics/playing_cards/4_of_hearts.png'))
    c5h = Card(name='🂵5♥', rank=5, suit='heart', surf=pg.image.load('graphics/playing_cards/5_of_hearts.png'))
    c6h = Card(name='🂶6♥', rank=6, suit='heart', surf=pg.image.load('graphics/playing_cards/6_of_hearts.png'))
    c7h = Card(name='🂷7♥', rank=7, suit='heart', surf=pg.image.load('graphics/playing_cards/7_of_hearts.png'))
    c8h = Card(name='🂸8♥', rank=8, suit='heart', surf=pg.image.load('graphics/playing_cards/8_of_hearts.png'))
    c9h = Card(name='🂹9♥', rank=9, suit='heart', surf=pg.image.load('graphics/playing_cards/9_of_hearts.png'))
    c10h = Card(name='🂺10♥', rank=10, suit='heart', surf=pg.image.load('graphics/playing_cards/10_of_hearts.png'))
    cJh = Card(name='🂻J♥', rank=11, suit='heart', surf=pg.image.load('graphics/playing_cards/jack_of_hearts2.png'))
    cQh = Card(name='🂽Q♥', rank=12, suit='heart', surf=pg.image.load('graphics/playing_cards/queen_of_hearts2.png'))
    cKh = Card(name='🂾K♥', rank=13, suit='heart', surf=pg.image.load('graphics/playing_cards/king_of_hearts2.png'))
    cAh = Card(name='🂱A♥', rank=14, suit='heart', surf=pg.image.load('graphics/playing_cards/ace_of_hearts.png'))

    c2d = Card(name='🃂2♦', rank=2, suit='diamond', surf=pg.image.load('graphics/playing_cards/2_of_diamonds.png'))
    c3d = Card(name='🃃3♦', rank=3, suit='diamond', surf=pg.image.load('graphics/playing_cards/3_of_diamonds.png'))
    c4d = Card(name='🃄4♦', rank=4, suit='diamond', surf=pg.image.load('graphics/playing_cards/4_of_diamonds.png'))
    c5d = Card(name='🃅5♦', rank=5, suit='diamond', surf=pg.image.load('graphics/playing_cards/5_of_diamonds.png'))
    c6d = Card(name='🃆6♦', rank=6, suit='diamond', surf=pg.image.load('graphics/playing_cards/6_of_diamonds.png'))
    c7d = Card(name='🃇7♦', rank=7, suit='diamond', surf=pg.image.load('graphics/playing_cards/7_of_diamonds.png'))
    c8d = Card(name='🃈8♦', rank=8, suit='diamond', surf=pg.image.load('graphics/playing_cards/8_of_diamonds.png'))
    c9d = Card(name='🃉9♦', rank=9, suit='diamond', surf=pg.image.load('graphics/playing_cards/9_of_diamonds.png'))
    c10d = Card(name='🃊10♦', rank=10, suit='diamond', surf=pg.image.load('graphics/playing_cards/10_of_diamonds.png'))
    cJd = Card(name='🃋J♦', rank=11, suit='diamond', surf=pg.image.load('graphics/playing_cards/jack_of_diamonds2.png'))
    cQd = Card(name='🃍Q♦', rank=12, suit='diamond', surf=pg.image.load('graphics/playing_cards/queen_of_diamonds2.png'))
    cKd = Card(name='🃎K♦', rank=13, suit='diamond', surf=pg.image.load('graphics/playing_cards/king_of_diamonds2.png'))
    cAd = Card(name='🃁A♦', rank=14, suit='diamond', surf=pg.image.load('graphics/playing_cards/ace_of_diamonds.png'))

    c2c = Card(name='🃒2♣', rank=2, suit='club', surf=pg.image.load('graphics/playing_cards/2_of_clubs.png'))
    c3c = Card(name='🃓3♣', rank=3, suit='club', surf=pg.image.load('graphics/playing_cards/3_of_clubs.png'))
    c4c = Card(name='🃔4♣', rank=4, suit='club', surf=pg.image.load('graphics/playing_cards/4_of_clubs.png'))
    c5c = Card(name='🃕5♣', rank=5, suit='club', surf=pg.image.load('graphics/playing_cards/5_of_clubs.png'))
    c6c = Card(name='🃖6♣', rank=6, suit='club', surf=pg.image.load('graphics/playing_cards/6_of_clubs.png'))
    c7c = Card(name='🃗7♣', rank=7, suit='club', surf=pg.image.load('graphics/playing_cards/7_of_clubs.png'))
    c8c = Card(name='🃘8♣', rank=8, suit='club', surf=pg.image.load('graphics/playing_cards/8_of_clubs.png'))
    c9c = Card(name='🃙9♣', rank=9, suit='club', surf=pg.image.load('graphics/playing_cards/9_of_clubs.png'))
    c10c = Card(name='🃚10♣', rank=10, suit='club', surf=pg.image.load('graphics/playing_cards/10_of_clubs.png'))
    cJc = Card(name='🃛J♣', rank=11, suit='club', surf=pg.image.load('graphics/playing_cards/jack_of_clubs2.png'))
    cQc = Card(name='🃝Q♣', rank=12, suit='club', surf=pg.image.load('graphics/playing_cards/queen_of_clubs2.png'))
    cKc = Card(name='🃞K♣', rank=13, suit='club', surf=pg.image.load('graphics/playing_cards/king_of_clubs2.png'))
    cAc = Card(name='🃑A♣', rank=14, suit='club', surf=pg.image.load('graphics/playing_cards/ace_of_clubs.png'))

    c2s = Card(name='🂢2♤', rank=2, suit='spade', surf=pg.image.load('graphics/playing_cards/2_of_spades.png'))
    c3s = Card(name='🂣3♤', rank=3, suit='spade', surf=pg.image.load('graphics/playing_cards/3_of_spades.png'))
    c4s = Card(name='🂤4♤', rank=4, suit='spade', surf=pg.image.load('graphics/playing_cards/4_of_spades.png'))
    c5s = Card(name='🂥5♤', rank=5, suit='spade', surf=pg.image.load('graphics/playing_cards/5_of_spades.png'))
    c6s = Card(name='🂦6♤', rank=6, suit='spade', surf=pg.image.load('graphics/playing_cards/6_of_spades.png'))
    c7s = Card(name='🂧7♤', rank=7, suit='spade', surf=pg.image.load('graphics/playing_cards/7_of_spades.png'))
    c8s = Card(name='🂨8♤', rank=8, suit='spade', surf=pg.image.load('graphics/playing_cards/8_of_spades.png'))
    c9s = Card(name='🂩9♤', rank=9, suit='spade', surf=pg.image.load('graphics/playing_cards/9_of_spades.png'))
    c10s = Card(name='🂪10♤', rank=10, suit='spade', surf=pg.image.load('graphics/playing_cards/10_of_spades.png'))
    cJs = Card(name='🂫J♤', rank=11, suit='spade', surf=pg.image.load('graphics/playing_cards/jack_of_spades2.png'))
    cQs = Card(name='🂭Q♤', rank=12, suit='spade', surf=pg.image.load('graphics/playing_cards/queen_of_spades2.png'))
    cKs = Card(name='🂮K♤', rank=13, suit='spade', surf=pg.image.load('graphics/playing_cards/king_of_spades2.png'))
    cAs = Card(name='🂡A♤', rank=14, suit='spade', surf=pg.image.load('graphics/playing_cards/ace_of_spades.png'))

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
        print('fill')
        if len(game.deck) >= 5:
            for n in range(5 - len(game.waiting)):
                game.waiting.insert(0,game.deck[0])
                game.deck.pop(0)

        else:
            for n in range(5-len(game.waiting)):
                if len(game.deck) == 0:
                    break
                else:
                    game.waiting.insert(0, game.deck[0])
                    game.deck.pop(0)


# Initializing Game Object & Shuffling Deck
game = Lifeboat()
rng.shuffle(game.deck)

def restart():
    global game_active, title, win, lose
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
    rng.shuffle(game.deck)

# ================================================================================================================= #
#                                                STARTING VARIABLES                                                 #
# ================================================================================================================= #
if True:
    game_active = False
    title = True
    win = False
    lose = False
    rules = False

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
    boat1_text = font.render(f'Seats left: {15-len(game.board1)}',True,'White')
    boat2_text = font.render(f'Seats left: {15 - len(game.board2)}', True, 'White')
    boat3_text = font.render(f'Seats left: {15 - len(game.board3)}', True, 'White')
    boat4_text = font.render(f'Seats left: {15 - len(game.board4)}', True, 'White')
    unsaved_text = font.render(f"Unsaved Passengers:",True,'White')
    unsaved_card_pos = (300,690)

    # Rules button
    rules_button_text = font.render('RULES',True,'White')
    rules_button_surf = pg.Surface((100,50)); rules_button_surf.fill('Blue')
    rules_button_rect = rules_button_surf.get_rect(topleft = (355,140))

    # Restart Button
    restart_button_text = font.render('RESTART',True,'White')
    restart_button_surf = pg.Surface((120,50)); restart_button_surf.fill('Brown4')
    restart_button_rect = restart_button_surf.get_rect(topleft = (530,140))

    # Fill Waiting Button
    fill_button_text = font.render('Fill Line', True, 'White')
    fill_button_surf = pg.Surface((90,50)); fill_button_surf.fill('brown')
    fill_button_rect = fill_button_surf.get_rect(topleft = (680,325))

    # Play Again Button
    replay_text = font.render('Play again?',True,'white')
    replay_rect = replay_text.get_rect(bottomright = (900,700))

    # Title, Rules, Win and Lose Screens
    title_surf = pg.image.load('graphics/lifeboat_title.png')
    rules_surf = pg.image.load('graphics/lifeboat_rules.png')
    win_surf = pg.image.load('graphics/lifeboat_win.png')
    lose_surf = pg.image.load('graphics/lifeboat_lose.png')

# Game Loop
while True:
    # ============================================================================================================= #
    #                                                EVENT LOOP                                                     #
    # ============================================================================================================= #
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        else:
            # Closing the title screen
            if title:
                if event.type == pg.MOUSEBUTTONDOWN:
                    title = False
                    game_active = True


            if game_active:
                mouse_pos = pg.mouse.get_pos()
                # Clicking Buttons
                if event.type == pg.MOUSEBUTTONDOWN:
                    if rules: rules = False
                    if rules_button_rect.collidepoint(mouse_pos):
                        rules = True
                    if restart_button_rect.collidepoint(mouse_pos):
                        lose = True
                        game_active = False
                    if fill_button_rect.collidepoint(mouse_pos):
                        game.fill_line()

                # Picking up cards
                if event.type == pg.MOUSEBUTTONDOWN and not game.holding:
                    if len(game.deck) > 0 and len(game.waiting) < 5:
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
                if event.type == pg.MOUSEBUTTONUP and game.holding:
                    if waiting_marker_rect.collidepoint(mouse_pos) or waiting_topcard_rect.collidepoint(mouse_pos):
                            game.put_down_card(game.holding,game.waiting)
                    if board1_marker_rect.collidepoint(mouse_pos) or board1_topcard_rect.collidepoint(mouse_pos):
                        game.validate_put_down(game.holding,game.board1)
                    if board2_marker_rect.collidepoint(mouse_pos) or board2_topcard_rect.collidepoint(mouse_pos):
                        game.validate_put_down(game.holding, game.board2)
                    if board3_marker_rect.collidepoint(mouse_pos) or board3_topcard_rect.collidepoint(mouse_pos):
                        game.validate_put_down(game.holding, game.board3)
                    if board4_marker_rect.collidepoint(mouse_pos) or board4_topcard_rect.collidepoint(mouse_pos):
                        game.validate_put_down(game.holding, game.board4)

            # Replaying game after win/lose
            if not game_active:
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    if replay_rect.collidepoint(mouse_pos):
                        restart()



# ============================================================================================================= #
#                                               BLITTING SURFACES                                               #
# ============================================================================================================= #
    if game_active:
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
                y += 2
            y = 0
            for n in game.board2:
                screen.blit(game.board2[0].surf, (board2_pos[0],board2_pos[1]+y))
                board2_topcard_rect.y = board2_pos[1] + y
                y += 2
            y = 0
            for n in game.board3:
                screen.blit(game.board3[0].surf, (board3_pos[0],board3_pos[1]+y))
                board3_topcard_rect.y = board3_pos[1] + y
                y += 2
            y = 0
            for n in game.board4:
                screen.blit(game.board4[0].surf, (board4_pos[0],board4_pos[1]+y))
                board4_topcard_rect.y = board4_pos[1] + y
                y += 2

            # Updating and Blitting Stats
            remaining_text = font.render(f'Onboard: {len(game.deck)}', True, 'White')
            waiting_text = font.render(f'In line: {len(game.waiting)}', True, 'White')
            screen.blit(remaining_text,(345,210))
            screen.blit(waiting_text,(550,210))
            pg.draw.line(screen, 'white', (500,200),(500,235),3)
            boat1_text = font.render(f'Seats left: {15 - len(game.board1)}', True, 'White')
            screen.blit(boat1_text,(250,80))
            boat2_text = font.render(f'Seats left: {15 - len(game.board2)}', True, 'White')
            screen.blit(boat2_text, (620, 80))
            boat3_text = font.render(f'Seats left: {15 - len(game.board3)}', True, 'White')
            screen.blit(boat3_text, (250, 600))
            boat4_text = font.render(f'Seats left: {15 - len(game.board4)}', True, 'White')
            screen.blit(boat4_text, (620, 600))

            # Unsaved Counter
            screen.blit(unsaved_text, (390,640))
            # Counting the number of unsaved cards
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

            # Blitting Held Card
            if game.holding:
                screen.blit(game.holding.surf,(mouse_pos[0]-69,mouse_pos[1]-100))

    # Winning
    if len(game.deck) == 0 and len(game.waiting) == 0 and not game.holding:
        game_active = False
        win = True
    # Losing
    if len(game.waiting) > 5:
        game_active = False
        lose = True
    if len(game.board1) > 15 or len(game.board2) > 15 or len(game.board3) > 15 or len(game.board4) > 15:
        game_active = False
        lose = True

    # Blitting Screens
    if not game_active:
        if title: screen.blit(title_surf,(0,0))
        elif win:
            screen.blit(win_surf,(0,0))
            screen.blit(replay_text,replay_rect)
        elif lose:
            screen.blit(lose_surf,(0,0))
            screen.blit(replay_text,replay_rect)

    # Updating display and limiting FPS
    pg.display.flip()
    clock.tick(60)
# ================================================================================================================= #
#                                                     end of code                                                   #
# ================================================================================================================= #
