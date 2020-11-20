import pygame
from TarockBasics import *
from MilestoneAgents import *

class TarockGame:

    def __init__(self):
        self.cards = {40: '1.jpg', 49: '10.jpg', 50: '11.jpg', 51: '12.jpg', 52: '13.jpg', 53: '14.jpg', 54: '15.jpg',
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

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.w, self.h = pygame.display.get_surface().get_size()
        self.running = True
        pygame.init()
        self.play = False

    def color_background(self):
        self.screen.fill((50, 108, 32))

    def draw_hand(self, hand, x, y, backs = False):
        if hand:
            card = pygame.image.load("Karte slike/" + self.cards[hand[0]])
            card_w = card.get_width()
            card_h = card.get_height()

            new_card_width = self.w / 20
            scale_factor = new_card_width / card_w


            for karta in hand:

                if not backs:
                    card = pygame.image.load("Karte slike/" + self.cards[karta])
                else:
                    card = pygame.image.load("Karte slike/" + self.cards[100])
                card = pygame.transform.scale(card, (int(card_w * scale_factor), int(card_h * scale_factor)))
                self.screen.blit(card, (x, y))
                x += 0.8 * new_card_width

    def write_score(self, points, x, y):

        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        myfont = pygame.font.SysFont("arial", 32)
        label = myfont.render(points, 1, (255, 255, 255))
        self.screen.blit(label, (x, y))

    def run(self):

        tb = TarockBasics()

        p1, p2, p3, talon = tb.deal_cards()

        #p1, p2, p3 = [7,8], [59, 56],  [1, 61]
        ma = MilestoneAgents(p1, p2, p3, [1,2,3], 1, [2,3])

        points = {1: 0, 2: 0, 3: 0}


        while self.running:

            #color background
            self.color_background()

            #get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            pygame.draw.rect(self.screen, (150, 150, 150), (500, 1050, 120, 40))

            self.draw_hand(p1, 20, 60)
            self.draw_hand(p2, 20, 340)#, backs=True)
            self.draw_hand(p3, 20, 620)#, backs=True)

            first = ma.player_order[0]
            second = ma.player_order[1]
            third = ma.player_order[2]

            if self.play and len(ma.stack) == 0:
                card = ma.locally_worst_worst_agent(first)
                ma.update_state(card, first)
                self.play = False

            if self.play and len(ma.stack) == 1:
                card = ma.locally_worst_worst_agent(second)
                ma.update_state(card, second)
                self.play = False

            if self.play and len(ma.stack) == 2:
                card = ma.locally_worst_worst_agent(third)
                ma.update_state(card, third)
                self.play = False

            if self.play and len(ma.stack) == 3:
                wp = ma.winning_card(ma.stack)
                points[ma.player_order[wp]] += ma.eval_stack(ma.stack)
                ma.clear_state()


            self.draw_hand(ma.stack, 1800, 340)
            self.write_score(str(points), 1800, 600)
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_x > 500 and mouse_x < 620 and mouse_y > 1050 and mouse_y < 1090:
                            self.play = True
                            if not p1 and not p2 and not p3:
                                self.running = False
                    if mouse_x > 700 and mouse_x < 820 and mouse_y > 1050 and mouse_y < 1090:
                        p1, p2, p3, talon = tb.deal_cards()

                        ma = MilestoneAgents(p1, p2, p3, [1, 2, 3], 1, [2, 3])

                if event.type == pygame.QUIT:
                    self.running = False

            if not p1 and not p2 and not p3:
                pygame.draw.rect(self.screen, (255, 0, 0), (700, 1050, 120, 40))

            pygame.display.update()


if __name__ == "__main__":
    a = TarockGame()
    a.run()