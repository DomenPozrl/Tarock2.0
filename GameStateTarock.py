from TarockBasics import TarockBasics
import copy

class GameStateTarock(TarockBasics):


    #p1 -> player1 cards
    #p2 -> player2 cards
    #p3 -> player3 cards
    #ps -> players id
    def __init__(self, p1, p2, p3, ps, starting_player, duo):

        super().__init__()
        self.players = ps

        self.players2 = ps + ps
        self.player1_cards = p1
        self.player2_cards = p2
        self.player3_cards = p3
        self.player_hands = {ps[0]: self.player1_cards, ps[1]: self.player2_cards, ps[2]: self.player3_cards}
        self.player_hands_copy = copy.deepcopy(self.player_hands)
        self.stack = []
        self.stack_players = []
        self.stack_value = 0
        self.stack_color = None

        self.starting_player = starting_player
        self.second_player = self.players2[self.players2.index(starting_player) + 1]
        self.third_player = self.players2[self.players2.index(starting_player) + 2]
        self.player_order = [self.starting_player, self.second_player, self.third_player]

        self.duo = duo
        self.current_winning_card = None
        self.current_winning_player = None

        self.played_cards = dict()
        self.discard = []

        self.player1_skrt = {"heart": False, "diamond": False, "spade": False, "club": False, "tarock": False}
        self.player2_skrt = {"heart": False, "diamond": False, "spade": False, "club": False, "tarock": False}
        self.player3_skrt = {"heart": False, "diamond": False, "spade": False, "club": False, "tarock": False}


    #gets the opening card of the stack and the hand where we have to find the legal moves
    #returns all the cards we can legally play from the received hand
    def legal_moves(self, opener, hand):
        legal_cards = []
        for card in hand:
            if self.is_same_color(opener, card):
                legal_cards.append(card)

        if not legal_cards:
            for card in hand:
                if self.isTarock(card):
                    legal_cards.append(card)

        if not legal_cards:
            legal_cards = hand

        return legal_cards

    # returns true if c2 beats c1
    def winning_card_pair(self, c1, c2):
        if self.is_same_color(c1, c2):
            return c2 > c1
        elif self.isTarock(c1):
            return False
        elif self.isTarock(c2):
            return True
        else:
            return False

    #returns index of the winning card
    def winning_card(self, stack):
        #druga premaga prvo
        if self.winning_card_pair(stack[0], stack[1]):
            # tretja premaga drugo
            if self.winning_card_pair(stack[1], stack[2]):
                return 2
            else:
                return 1
        #prva premaga drugo
        else:
            #tretja premaga prvo
            if self.winning_card_pair(stack[0], stack[2]):
                return 2
            #prva premaga tretjo
            else:
                return 0

    def can_pickup_stack(self, stack, hand):

        can = []
        if len(stack) == 0:
            return hand

        karta = stack[0]
        if len(stack) == 1:
            for card in self.legal_moves(stack[0], hand):
                if self.isTarock(karta):

                    #samo tarok je lahko vecji od taroka tko da ce je karta tarok potem v legal kartah lahko poberejo samo karte k so >
                    if card > karta:
                        can.append(card)

                else:
                    #ce ni karta tarok potem mamo 3 situacije: nismo skrti (pobere samo ce card > karta), smo skrti mamo taroke (poberejo vsi taroki), smo skrti nimamo tarokov (nic ne pobere)
                    if self.is_same_color(karta, card) and card > karta:
                        can.append(card)

                    if self.isTarock(card):
                        can.append(card)
            return can

        druga_karta = stack[1]
        if len(stack) == 2:

            #najprej preveri kira ze zdej pobere
            if self.is_same_color(karta, druga_karta):
                if druga_karta > karta:
                    win_card = druga_karta
                else:
                    win_card = karta
            else:
                if self.isTarock(druga_karta):
                    win_card = druga_karta
                else:
                    win_card = karta

            for card in self.legal_moves(stack[0], hand):
                if self.isTarock(win_card):

                    #samo tarok je lahko vecji od taroka tko da ce je karta tarok potem v legal kartah lahko poberejo samo karte k so >
                    if card > win_card:
                        can.append(card)

                else:
                    #ce ni karta tarok potem mamo 3 situacije: nismo skrti (pobere samo ce card > karta), smo skrti mamo taroke (poberejo vsi taroki), smo skrti nimamo tarokov (nic ne pobere)
                    if self.is_same_color(karta, card) and card > karta:
                        can.append(card)

                    if self.isTarock(card):
                        can.append(card)

            return can


    def eval_stack(self, stack):
        stack_points = [self.id_to_points[c] for c in stack]
        if stack_points.count(0) == 0:
            return sum(stack_points) - 2
        elif stack_points.count(0) == 1:
            return sum(stack_points) - 1
        elif stack_points.count(0) == 2:
            return sum(stack_points)
        else:
            return 1

    #called after each card is played, updates the state all it can
    def update_state(self, card, player):

        #adding card to played
        self.played_cards[card] = True

        #adding to stack
        if len(self.stack) == 0:
            if self.isHeart(card):
                self.stack_color = "heart"
            elif self.isDiamond(card):
                self.stack_color = "diamond"
            elif self.isClub(card):
                self.stack_color = "club"
            elif self.isSpade(card):
                self.stack_color = "spade"
            else:
                self.stack_color = "tarock"

        self.stack.append(card)
        self.stack_players.append(player)
        self.stack_value += self.id_to_points[card]

        #setting the current_winning variables
        #if there is only one card played so far
        if len(self.stack) == 1:
            self.current_winning_card = card
            self.current_winning_player = player

        #if there are more cards played, card is current card
        if len(self.stack) >= 2:

            #if they are the same color then the bigger id wins
            #if the new card is is bigger then we change the winner otherwise we leave it
            if self.is_same_color(self.current_winning_card, card):
                if card > self.current_winning_card:
                    self.current_winning_card = card
                    self.current_winning_player = player
            #if they are not the same color we have two cases of that
            else:
                #if the second one is a tarock then the second one wins
                if self.isTarock(card):
                    self.current_winning_card = card
                    self.current_winning_player = player
                #if the second one is not a tarock then the first one wins by default so we don't need an else statement
                #because the previous player is already set as the winner

        #update skrt
        starting_card = self.stack[0]
        if not self.is_same_color(starting_card, card):
            #player je škrt te barve
            if card in self.player1_cards:
                if self.isHeart(starting_card):
                    self.player1_skrt["heart"] = True
                elif self.isDiamond(starting_card):
                    self.player1_skrt["diamond"] = True
                elif self.isClub(starting_card):
                    self.player1_skrt["club"] = True
                elif self.isSpade(starting_card):
                    self.player1_skrt["spade"] = True
                else:
                    self.player1_skrt["tarock"] = True

                #ce nista iste barve in nasa ni tarok pomeni tudi da je taroka skrt
                if not self.isTarock(card):
                    self.player1_skrt["tarock"] = True

            if card in self.player2_cards:
                if self.isHeart(starting_card):
                    self.player2_skrt["heart"] = True
                elif self.isDiamond(starting_card):
                    self.player2_skrt["diamond"] = True
                elif self.isClub(starting_card):
                    self.player2_skrt["club"] = True
                elif self.isSpade(starting_card):
                    self.player2_skrt["spade"] = True
                else:
                    self.player2_skrt["tarock"] = True

                # ce nista iste barve in nasa ni tarok pomeni tudi da je taroka skrt
                if not self.isTarock(card):
                    self.player1_skrt["tarock"] = True

            if card in self.player3_cards:
                if self.isHeart(starting_card):
                    self.player3_skrt["heart"] = True
                elif self.isDiamond(starting_card):
                    self.player3_skrt["diamond"] = True
                elif self.isClub(starting_card):
                    self.player3_skrt["club"] = True
                elif self.isSpade(starting_card):
                    self.player3_skrt["spade"] = True
                else:
                    self.player3_skrt["tarock"] = True

                # ce nista iste barve in nasa ni tarok pomeni tudi da je taroka skrt
                if not self.isTarock(card):
                    self.player1_skrt["tarock"] = True

        #add the pile to discard
        if len(self.stack) == 3:
            self.discard.append(self.stack)

            #setting up the new player order
            self.player_order = self.players + self.players
            winning_player_index = self.player_order.index(self.current_winning_player)
            self.player_order = self.player_order[winning_player_index:winning_player_index +3]

        # removing from hand
        if card in self.player1_cards:
            self.player1_cards.remove(card)
        elif card in self.player2_cards:
            self.player2_cards.remove(card)
        else:
            self.player3_cards.remove(card)

    def update_state_talon(self, talon):
        for card in talon:
            self.played_cards[card] = True
        self.discard.append(talon)


    def clear_state(self):
        self.stack = []
        self.stack_players = []
        self.stack_value = 0
        self.stack_color = None
        self.player_hands_copy = copy.deepcopy(self.player_hands)
        self.starting_player = self.current_winning_player
        self.second_player = self.players2[self.players2.index(self.starting_player) + 1]
        self.third_player = self.players2[self.players2.index(self.starting_player) + 2]
        self.current_winning_player = None
        self.current_winning_card = None