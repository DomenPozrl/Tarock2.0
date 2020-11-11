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
            options_dict = dict()

            for option in options:
                points, c1, c2, c3 = option

                if c1 not in options_dict:
                    options_dict[c1] = [points]
                else:
                    options_dict[c1].append(points)

            options_dict = {c1: sum(options_dict[c1])/len(options_dict[c1]) for c1 in options_dict}
            options_avg = [(c1, options_dict[c1]) for c1 in options_dict]

            options_avg = list(sorted(options_avg, key=lambda x: x[1]))
            return options_avg[0][0]


        if len(self.stack) == 1:
            options = []
            for card1 in self.legal_moves(self.stack[0], self.player_hands[player_id]):
                    for card2 in self.legal_moves(self.stack[0], self.player_hands[self.third_player]):
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

            options_dict = dict()

            for option in options:
                points, c1, c2, c3 = option

                if c2 not in options_dict:
                    options_dict[c2] = [points]
                else:
                    options_dict[c2].append(points)

            options_dict = {c2: sum(options_dict[c2]) / len(options_dict[c2]) for c2 in options_dict}
            options_avg = [(c2, options_dict[c2]) for c2 in options_dict]

            options_avg = list(sorted(options_avg, key=lambda x: x[1]))
            return options_avg[0][0]

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

            options_dict = dict()

            for option in options:
                points, c1, c2, c3 = option

                if c3 not in options_dict:
                    options_dict[c3] = [points]
                else:
                    options_dict[c3].append(points)

            options_dict = {c3: sum(options_dict[c3]) / len(options_dict[c3]) for c3 in options_dict}
            options_avg = [(c3, options_dict[c3]) for c3 in options_dict]

            options_avg = list(sorted(options_avg, key=lambda x: x[1]))
            return options_avg[0][0]

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

            options_dict = dict()

            for option in options:
                points, c1, c2, c3 = option

                if c1 not in options_dict:
                    options_dict[c1] = [points]
                else:
                    options_dict[c1].append(points)

            options_dict = {c1: sum(options_dict[c1]) / len(options_dict[c1]) for c1 in options_dict}
            options_avg = [(c1, options_dict[c1]) for c1 in options_dict]

            options_avg = list(sorted(options_avg, key=lambda x: x[1]))
            return options_avg[-1][0]


        if len(self.stack) == 1:
            options = []
            for card1 in self.legal_moves(self.stack[0], self.player_hands[player_id]):
                for card2 in self.legal_moves(self.stack[0], self.player_hands[self.third_player]):
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

            options_dict = dict()

            for option in options:
                points, c1, c2, c3 = option

                if c2 not in options_dict:
                    options_dict[c2] = [points]
                else:
                    options_dict[c2].append(points)

            options_dict = {c2: sum(options_dict[c2]) / len(options_dict[c2]) for c2 in options_dict}
            options_avg = [(c2, options_dict[c2]) for c2 in options_dict]

            options_avg = list(sorted(options_avg, key=lambda x: x[1]))
            return options_avg[-1][0]


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

            options_dict = dict()

            for option in options:
                points, c1, c2, c3 = option

                if c3 not in options_dict:
                    options_dict[c3] = [points]
                else:
                    options_dict[c3].append(points)

            options_dict = {c3: sum(options_dict[c3]) / len(options_dict[c3]) for c3 in options_dict}
            options_avg = [(c3, options_dict[c3]) for c3 in options_dict]

            options_avg = list(sorted(options_avg, key=lambda x: x[1]))
            return options_avg[-1][0]


if __name__ == "__main__":
    tb = TarockBasics()
    p1, p2, p3, talon = tb.deal_cards()
    ma = MilestoneAgents(p1, p2, p3, [1,2,3], 1, [1,2])

    tb.print_hand(p1)
    tb.print_hand(p2)
    tb.print_hand(p3)

    ma.update_state(p1[0], 1)
    print(ma.stack)
    y = ma.locally_best_agent(2)
    ma.update_state(y, 2)
    print(ma.stack)
    x = ma.locally_best_agent(3)
    ma.update_state(x, 3)
    print(ma.stack)
