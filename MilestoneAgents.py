#class contains milestones agents like worst player, random player, local max player, global max player
from GameStateTarock import GameStateTarock
from TarockBasics import *
import random
from anytree import Node, RenderTree
class MilestoneAgents(GameStateTarock):

    def __init__(self, p1, p2, p3, ps, sp, duo):
        super().__init__(p1, p2, p3, ps, sp, duo)

    def random_agent(self, player_id):
        if self.stack:
            if player_id == self.players[0]:
                return random.choice(self.legal_moves(self.stack[0], self.player1_cards))
            elif player_id == self.players[1]:
                return random.choice(self.legal_moves(self.stack[0], self.player2_cards))
            else:
                if player_id == self.players[2]:
                    return random.choice(self.legal_moves(self.stack[0], self.player3_cards))
        else:
            if player_id == self.players[0]:
                return random.choice(self.player1_cards)
            elif player_id == self.players[1]:
                return random.choice(self.player2_cards)
            else:
                if player_id == self.players[2]:
                    return random.choice(self.player3_cards)

    #play the card that from all the possibilities produces the least amount of points for you this turn
    def locally_worst_agent(self, player_id):

        #gamestatetarock already contains stack, all hands and everything
        if len(self.stack) == 0:
            options = []
            for card1 in self.player_hands[player_id]:
                for card2 in self.legal_moves(card1, self.player_hands[self.second_player]):
                    for card3 in self.legal_moves(card1, self.player_hands[self.third_player]):
                        win_card_index = self.winning_card([card1, card2, card3])
                        #print(self.player_order)
                        win_player_id = self.player_order[win_card_index]

                        if win_player_id == player_id:
                            # this means we get points for this hand so they should be positive
                            options.append((self.eval_stack([card1, card2, card3]), card1, card2, card3))

                        elif win_player_id in self.duo and player_id in self.duo:
                            #this means we get points for this hand so they should be positive
                            options.append((self.eval_stack([card1, card2, card3]), card1, card2, card3))
                        else:
                            options.append((-1 * self.eval_stack([card1, card2, card3]), card1, card2, card3))
            for option in options:
                print(option[0], self.id_to_cards[option[1]], self.id_to_cards[option[2]], self.id_to_cards[option[3]])
            return min(options, key=lambda x: x[0])[1]
        if len(self.stack) == 1:
            options = []
            for card1 in self.legal_moves(self.stack[0], self.player_hands[player_id]):
                    for card2 in self.player_hands[self.third_player]:
                        win_card_index = self.winning_card([self.stack[0], card1, card2])
                        win_player_id = self.player_order[win_card_index]

                        if win_player_id == player_id:
                            # this means we get points for this hand so they should be positive
                            options.append((self.eval_stack([self.stack[0], card1, card2]), self.stack[0], card1, card2))

                        elif win_player_id in self.duo and player_id in self.duo:
                            # this means we get points for this hand so they should be positive
                            options.append((self.eval_stack([self.stack[0], card1, card2]), self.stack[0], card1, card2))
                        else:
                            options.append((-1 * self.eval_stack([self.stack[0], card1, card2]), self.stack[0], card1, card2))
            return min(options, key=lambda x: x[0])[2]

        if len(self.stack) == 2:
            options = []
            for card1 in self.legal_moves(self.stack[0], self.player_hands[player_id]):
                win_card_index = self.winning_card([self.stack[0], self.stack[1], card1])
                win_player_id = self.player_order[win_card_index]

                if win_player_id == player_id:
                    # this means we get points for this hand so they should be positive
                    options.append((self.eval_stack([self.stack[0], self.stack[1], card1]), self.stack[0], self.stack[1], card1))

                elif win_player_id in self.duo and player_id in self.duo:
                    # this means we get points for this hand so they should be positive
                    options.append((self.eval_stack([self.stack[0], self.stack[1], card1]), self.stack[0], self.stack[1], card1))
                else:
                    options.append((-1 * self.eval_stack([self.stack[0], self.stack[1], card1]), self.stack[0], self.stack[1], card1))
            return min(options, key=lambda x: x[0])[3]

    def locally_best_agent(self, player_id):
        # gamestatetarock already contains stack, all hands and everything
        if len(self.stack) == 0:
            options = []
            for card1 in self.player_hands[player_id]:
                for card2 in self.legal_moves(card1, self.player_hands[self.second_player]):
                    for card3 in self.legal_moves(card1, self.player_hands[self.third_player]):
                        win_card_index = self.winning_card([card1, card2, card3])
                        # print(self.player_order)
                        win_player_id = self.player_order[win_card_index]

                        if win_player_id == player_id:
                            # this means we get points for this hand so they should be positive
                            options.append((self.eval_stack([card1, card2, card3]), card1, card2, card3))

                        elif win_player_id in self.duo and player_id in self.duo:
                            # this means we get points for this hand so they should be positive
                            options.append((self.eval_stack([card1, card2, card3]), card1, card2, card3))
                        else:
                            options.append((-1 * self.eval_stack([card1, card2, card3]), card1, card2, card3))


            for option in options:
                print(option[0], self.id_to_cards[option[1]], self.id_to_cards[option[2]], self.id_to_cards[option[3]])


            return max(options, key=lambda x: x[0])[1]
        if len(self.stack) == 1:
            options = []
            for card1 in self.legal_moves(self.stack[0], self.player_hands[player_id]):
                for card2 in self.player_hands[self.third_player]:
                    win_card_index = self.winning_card([self.stack[0], card1, card2])
                    win_player_id = self.player_order[win_card_index]

                    if win_player_id == player_id:
                        # this means we get points for this hand so they should be positive
                        options.append((self.eval_stack([self.stack[0], card1, card2]), self.stack[0], card1, card2))

                    elif win_player_id in self.duo and player_id in self.duo:
                        # this means we get points for this hand so they should be positive
                        options.append((self.eval_stack([self.stack[0], card1, card2]), self.stack[0], card1, card2))
                    else:
                        options.append(
                            (-1 * self.eval_stack([self.stack[0], card1, card2]), self.stack[0], card1, card2))
            return max(options, key=lambda x: x[0])[2]

        if len(self.stack) == 2:
            options = []
            for card1 in self.legal_moves(self.stack[0], self.player_hands[player_id]):
                win_card_index = self.winning_card([self.stack[0], self.stack[1], card1])
                win_player_id = self.player_order[win_card_index]

                if win_player_id == player_id:
                    # this means we get points for this hand so they should be positive
                    options.append(
                        (self.eval_stack([self.stack[0], self.stack[1], card1]), self.stack[0], self.stack[1], card1))

                elif win_player_id in self.duo and player_id in self.duo:
                    # this means we get points for this hand so they should be positive
                    options.append(
                        (self.eval_stack([self.stack[0], self.stack[1], card1]), self.stack[0], self.stack[1], card1))
                else:
                    options.append((-1 * self.eval_stack([self.stack[0], self.stack[1], card1]), self.stack[0],
                                    self.stack[1], card1))
            return max(options, key=lambda x: x[0])[3]


if __name__ == "__main__":
    tb = TarockBasics()
    p1, p2, p3, talon = tb.deal_cards()
    ma = MilestoneAgents(p1, p2, p3, [1,2,3], 1, [1,2])

    tb.print_hand(p1)
    tb.print_hand(p2)
    tb.print_hand(p3)
