import pygame
from TarockBasics import TarockBasics
from get_states_GST_functions import *
from MilestoneAgents import *

#TODO: now the functions for drawing are implemented, now I have to implement all the state getting functions
#TODO: then implement playing the game by clicking the next button and use the displays to check if all the state getting functions are working correctly
#TODO: i guess the plays can be made by a random agent so then i just click next and check how the state change
#TODO: it would be the best if i check if all of the properties reach all the values they are suppose to

class TarockGUI:

    def __init__(self, testing_state_functions=True):
        pygame.init()

        self.id_to_cards = {
            # herci
            4: "1\u2665",
            3: "2\u2665",
            2: "3\u2665",
            1: "4\u2665",
            5: "B\u2665",
            6: "C\u2665",
            7: "Q\u2665",
            8: "K\u2665",

            # kare
            14: "1\u2666",
            13: "2\u2666",
            12: "3\u2666",
            11: "4\u2666",
            15: "B\u2666",
            16: "C\u2666",
            17: "Q\u2666",
            18: "K\u2666",

            # piki
            21: "7\u2660",
            22: "8\u2660",
            23: "9\u2660",
            24: "10\u2660",
            25: "B\u2660",
            26: "C\u2660",
            27: "Q\u2660",
            28: "K\u2660",

            # krizi
            31: "7\u2663",
            32: "8\u2663",
            33: "9\u2663",
            34: "10\u2663",
            35: "B\u2663",
            36: "C\u2663",
            37: "Q\u2663",
            38: "K\u2663",

            # taroki
            40: "I",
            41: "II",
            42: "III",
            43: "IV",
            44: "V",
            45: "VI",
            46: "VII",
            47: "VIII",
            48: "IX",
            49: "X",
            50: "XI",
            51: "XII",
            52: "XIII",
            53: "XIV",
            54: "XV",
            55: "XVI",
            56: "XVII",
            57: "XVIII",
            58: "XIX",
            59: "XX",
            60: "XXI",
            61: "ŠKIS"}

        # pictures of the cards
        self.karte = {40: '1.jpg', 49: '10.jpg', 50: '11.jpg', 51: '12.jpg', 52: '13.jpg', 53: '14.jpg', 54: '15.jpg',
                      55: '16.jpg', 56: '17.jpg', 57: '18.jpg',
                      58: '19.jpg', 41: '2.jpg', 59: '20.jpg', 60: '21.jpg', 42: '3.jpg', 43: '4.jpg', 44: '5.jpg',
                      45: '6.jpg', 46: '7.jpg', 47: '8.jpg', 48: '9.jpg',
                      4: 'herc1.jpg', 3: 'herc2.jpg', 2: 'herc3.jpg', 1: 'herc4.jpg', 6: 'herckaval.jpg',
                      8: 'herckral.jpg', 7: 'herckralica.jpg',
                      5: 'hercpob.jpg', 16: 'karakaval.jpg', 18: 'karakral.jpg', 17: 'karakralica.jpg',
                      15: 'karapob.jpg', 14: 'karo1.jpg',
                      13: 'karo2.jpg', 12: 'karo3.jpg', 11: 'karo4.jpg', 34: 'kriz10.jpg', 31: 'kriz7.jpg',
                      32: 'kriz8.jpg', 33: 'kriz9.jpg',
                      36: 'krizkaval.jpg', 38: 'krizkral.jpg', 37: 'krizkralica.jpg', 35: 'krizpob.jpg',
                      24: 'pik10.jpg', 21: 'pik7.jpg', 22: 'pik8.jpg',
                      23: 'pik9.jpg', 26: 'pikkaval.jpg', 28: 'pikkral.jpg', 27: 'pikkralica.jpg', 25: 'pikpob.jpg',
                      61: 'skis.jpg', 100: 'hrbet.jpg'}


        #set the window size according to purpose of the gui
        if testing_state_functions:
            self.screen_width = 1380
            self.screen_height = 1300
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        else:
            self.screen_width = 500
            self.screen_height = 500
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))


    def draw_cards(self, args):
        cards, starting_y = args
        num = 16

        if not cards:
            return

        starting_x = 10
        ending_x = self.screen.get_width() - 10

        card_field_width = ending_x - starting_x

        new_width = int(card_field_width / (1 + (num - 1) * 0.6))

        karta = pygame.image.load("Karte slike/" + self.karte[cards[0]])
        width = karta.get_width()

        transform_koef = new_width / width
        new_height = int(karta.get_height() * transform_koef)
        #starting_y = 10

        for card in cards:
            karta = pygame.image.load("Karte slike/" + self.karte[card])
            karta = pygame.transform.scale(karta, (new_width, new_height))
            self.screen.blit(karta, (starting_x, starting_y))
            starting_x += int(new_width * 0.6)


    def draw_box_with_text(self, x, y, label, value):
        self.screen.blit(label, (x, y))

        width = label.get_size()[0]
        height = label.get_size()[1]

        self.screen.blit(value, (x, y + height + 10))

        pygame.draw.rect(self.screen, (255, 255, 255), (x - 5, y - 5, width + 10,  height + 10), 2)

        pygame.draw.rect(self.screen, (255, 255, 255), (x - 5, y + height + 5, width + 10, height + 10), 2)

    def draw_properties(self, args):
        names, vector, starting_y, title = args
        names = [x for x, y in names]

        labels_width = self.screen_width - 20 + 100
        font_size = 25
        starting_x = 10

        #decrease the font size untill it can fit on the screen
        while labels_width > self.screen_width - 20:
            myfont = pygame.font.SysFont("arial", font_size)

            labels = []

            for name in names:
                labels.append(myfont.render(name, 1, (255, 255, 255)))

            labels_width = sum([x.get_size()[0] for x in labels]) + (len(names)*10)

            font_size -= 1



        #pygame.draw.rect(self.screen, (255, 255, 255), (10, starting_y, 10, 20), 2)
        vector = [myfont.render(str(x), 1, (255, 255, 255)) for x in vector]

        for i in range(len(labels)):
            label = labels[i]
            value = vector[i]
            self.draw_box_with_text(starting_x, starting_y, label, value)
            starting_x += 10 + label.get_size()[0]



    def run(self, draw_functions, arguments):
        running = True


        while running:
            self.screen.fill((50, 108, 32))

            for func, args in zip(draw_functions, arguments):
                func(args)

            mouse_x, mouse_y = pygame.mouse.get_pos()



            pygame.draw.rect(self.screen, (150,150,150), (500, 1050, 120, 40))
            pygame.draw.rect(self.screen, (255,0,0), (1300, 550, 120, 40))
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_x > 500 and mouse_x < 620 and mouse_y > 1050 and mouse_y < 1090:
                        running = False

                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

if __name__ == "__main__":
    tb = TarockBasics()
    p1, p2, p3, talon = tb.deal_cards()

    gst = GameStateTarock(p1, p2, p3, [1,2,3], 1, [1,3])
    gst.update_state_talon(talon)
    tb.print_hand(talon)
    msa = MilestoneAgents(p1, p2, p3, [1,2,3], 1, [1,3])
    msa.update_state_talon(talon)
    players = [1,2,3]
    duo = [1,3]
    starting_player = 1


    t = TarockGUI(testing_state_functions=True)

    #Testiranje get state version1
    """while p1:
        for player in msa.player_order:
            if player == 1:
                if msa.stack == []:
                    vec1 = get_state_version1_open(1, msa)
                    b = (GET_STATE_VERSION1_OPEN, vec1, 870, "GET_STATE_OPEN_VERSION1")
                    card = msa.random_agent(1)
                    msa.update_state(card, 1)
                    print(f"Stack after player {player} plays: {msa.stack}")
                    print(f"Current winning player: {msa.current_winning_player}")
                    t.run([t.draw_cards, t.draw_cards, t.draw_cards,  t.draw_properties], [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), b])
                    t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                          [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050),
                           b])
                else:
                    vec1 = get_state_version1_play(1, msa)
                    a = (GET_STATE_VERSION1_PLAY, vec1, 800, "GET_STATE_PLAY_VERSION1")
                    t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                          [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050),
                           a])
                    card = msa.random_agent(1)
                    msa.update_state(card, 1)
                    print(f"Stack after player {player} plays: {msa.stack}")
                    print(f"Current winning player: {msa.current_winning_player}")

                    t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                          [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050),
                           a])

            else:
                card = msa.random_agent(player)
                msa.update_state(card, player)
                print(f"Stack after player {player} plays: {msa.stack}")
                print(f"Current winning player: {msa.current_winning_player}")
                t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                      [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050)])
        print("----------------------------------------------")
        msa.clear_state()"""

    #testiranje get state version2
    """while p1:
        for player in msa.player_order:
            if player == 1:
                    vec1 = get_state_version2(1, msa)
                    b = (GET_STATE_VERSION2, vec1, 870, "GET_STATE_OPEN_VERSION2")
                    t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                          [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), b])
                    card = msa.random_agent(1)
                    msa.update_state(card, 1)
                    print(f"Stack after player {player} plays: {msa.stack}")
                    print(f"Current winning player: {msa.current_winning_player}")
                    t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                          [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050),
                           b])

            else:
                card = msa.random_agent(player)
                msa.update_state(card, player)
                print(f"Stack after player {player} plays: {msa.stack}")
                print(f"Current winning player: {msa.current_winning_player}")
                t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                      [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050)])
        print("----------------------------------------------")
        msa.clear_state()"""


    #testiranje get state version3
    while p1:
        for player in msa.player_order:
            if player == 1:
                if msa.stack == []:
                    if 1 not in duo:
                        vec1 = get_state_version3_solo_open(1, msa)
                        b = (GET_STATE_VERSION3_SOLO_OPEN, vec1, 870, "GET_STATE_OPEN_VERSION1")
                        card = msa.random_agent(1)
                        msa.update_state(card, 1)
                        print(f"Stack after player {player} plays: {msa.stack}")
                        print(f"Current winning player: {msa.current_winning_player}")
                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), b])
                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050),
                               b])
                    else:
                        vec1 = get_state_version3_duo_open(1, msa)
                        b = (GET_STATE_VERSION3_DUO_OPEN, vec1, 870, "GET_STATE_OPEN_VERSION1")
                        card = msa.random_agent(1)
                        msa.update_state(card, 1)
                        print(f"Stack after player {player} plays: {msa.stack}")
                        print(f"Current winning player: {msa.current_winning_player}")
                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), b])
                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10),
                               (msa.stack, 1050),
                               b])
                elif len(msa.stack) == 1:
                    if 1 not in duo:
                        vec1 = get_state_version3_solo_second(1, msa)
                        a = (GET_STATE_VERSION3_SOLO_SECOND, vec1, 800, "GET_STATE_PLAY_VERSION1")
                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050),
                               a])
                        card = msa.random_agent(1)
                        msa.update_state(card, 1)
                        print(f"Stack after player {player} plays: {msa.stack}")
                        print(f"Current winning player: {msa.current_winning_player}")

                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050),
                               a])
                    else:
                        vec1 = get_state_version3_duo_second(1, msa)
                        a = (GET_STATE_VERSION3_DUO_SECOND, vec1, 800, "GET_STATE_PLAY_VERSION1")
                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10),
                               (msa.stack, 1050),
                               a])
                        card = msa.random_agent(1)
                        msa.update_state(card, 1)
                        print(f"Stack after player {player} plays: {msa.stack}")
                        print(f"Current winning player: {msa.current_winning_player}")

                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10),
                               (msa.stack, 1050),
                               a])
                else:
                    if 1 not in duo:
                        vec1 = get_state_version3_solo_third(1, msa)
                        a = (GET_STATE_VERSION3_SOLO_THIRD, vec1, 800, "GET_STATE_PLAY_VERSION1")
                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050),
                               a])
                        card = msa.random_agent(1)
                        msa.update_state(card, 1)
                        print(f"Stack after player {player} plays: {msa.stack}")
                        print(f"Current winning player: {msa.current_winning_player}")

                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050),
                               a])
                    else:
                        vec1 = get_state_version3_duo_third(1, msa)
                        a = (GET_STATE_VERSION3_DUO_THIRD, vec1, 800, "GET_STATE_PLAY_VERSION1")
                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10),
                               (msa.stack, 1050),
                               a])
                        card = msa.random_agent(1)
                        msa.update_state(card, 1)
                        print(f"Stack after player {player} plays: {msa.stack}")
                        print(f"Current winning player: {msa.current_winning_player}")

                        t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                              [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10),
                               (msa.stack, 1050),
                               a])

            else:
                card = msa.random_agent(player)
                msa.update_state(card, player)
                print(f"Stack after player {player} plays: {msa.stack}")
                print(f"Current winning player: {msa.current_winning_player}")
                t.run([t.draw_cards, t.draw_cards, t.draw_cards, t.draw_cards, t.draw_properties],
                      [(list(sorted(p1)), 520), (list(sorted(p2)), 260), (list(sorted(p3)), 10), (msa.stack, 1050)])
        print("----------------------------------------------")
        msa.clear_state()

    print(msa.player1_skrt)
    print(msa.player2_skrt)
    print(msa.player3_skrt)
