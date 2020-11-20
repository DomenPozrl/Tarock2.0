#class contains milestones agents like worst player, random player, local max player, global max player
from GameStateTarock import GameStateTarock
from TarockBasics import *
import random
from anytree import Node, RenderTree


class Tree:

    def __init__(self, card, duo, parent, children, depth, ma):
        self.card = card
        self.duo = duo
        self.points = None
        self.parent = parent
        self.children = children
        self.depth = depth
        self.ma = ma


    def eval_tree_max(self, player_duo_order):
        #max depth 3
        #zacne se s praznim nodom

        tocke3 = []
        for child in self.children:
            tocke2 = []

            for child2 in child.children:

                tocke = []

                for child3 in child2.children:
                    points = self.ma.eval_stack([child.card, child2.card, child3.card])

                    #if winner is duo then we can check wether the final points are positive or negative
                    winner_is_duo = player_duo_order[self.ma.winning_card([child.card, child2.card, child3.card])]

                    if winner_is_duo != child3.duo:
                        points = -1* points

                    child3.points = points
                    tocke.append((child3, points))

                otrok3, max_tocke = max(tocke, key=lambda x: x[1])
                #child2.children = [otrok3]
                if otrok3.duo == child2.duo:
                    child2.points = max_tocke
                else:
                    child2.points = -1 * max_tocke

                tocke2.append((child2, child2.points))

            otrok2, max_tocke = max(tocke2, key=lambda x: x[1])

            #child.children = [otrok2]
            if otrok2.duo == child.duo:
                child.points = max_tocke
            else:
                child.points = -1 * max_tocke

            tocke3.append((child, child.points))

        otrok, max_tocke = max(tocke3, key=lambda x: x[1])
        self.points = max_tocke
        #self.children = [otrok]


    def get_first_card_max(self):
        prvi_node = max(self.children, key=lambda x: x.points)
        return prvi_node.card

    def get_second_card_max(self, first_card):
        correct_node = None
        for child in self.children:
            if child.card == first_card:
                correct_node = child

        #print(first_card)
        drugi_node = max(correct_node.children, key=lambda x: x.points)
        return drugi_node.card

    def get_third_card_max(self, first_card, second_card):
        correct_node = None
        for child in self.children:
            if child.card == first_card:
                for child2 in child.children:
                    if child2.card == second_card:
                        correct_node = child2

        tretji_node = max(correct_node.children, key=lambda x: x.points)
        return tretji_node.card

    def eval_tree_min(self, player_duo_order):
        # min depth 3
        # zacne se s praznim nodom

        tocke3 = []
        for child in self.children:
            tocke2 = []

            for child2 in child.children:

                tocke = []

                for child3 in child2.children:
                    points = self.ma.eval_stack([child.card, child2.card, child3.card])

                    # if winner is duo then we can check wether the final points are positive or negative
                    winner_is_duo = player_duo_order[self.ma.winning_card([child.card, child2.card, child3.card])]

                    if winner_is_duo != child3.duo:
                        points = -1 * points

                    child3.points = points
                    tocke.append((child3, points))

                otrok3, min_tocke = min(tocke, key=lambda x: x[1])
                # child2.children = [otrok3]
                if otrok3.duo == child2.duo:
                    child2.points = min_tocke
                else:
                    child2.points = -1 * min_tocke

                tocke2.append((child2, child2.points))

            otrok2, min_tocke = min(tocke2, key=lambda x: x[1])

            # child.children = [otrok2]
            if otrok2.duo == child.duo:
                child.points = min_tocke
            else:
                child.points = -1 * min_tocke

            tocke3.append((child, child.points))

        otrok, min_tocke = min(tocke3, key=lambda x: x[1])
        self.points = min_tocke
        # self.children = [otrok]

    def get_first_card_min(self):
        prvi_node = min(self.children, key=lambda x: x.points)
        return prvi_node.card

    def get_second_card_min(self, first_card):
        correct_node = None
        for child in self.children:
            if child.card == first_card:
                correct_node = child

        # print(first_card)
        drugi_node = min(correct_node.children, key=lambda x: x.points)
        return drugi_node.card

    def get_third_card_min(self, first_card, second_card):
        correct_node = None
        for child in self.children:
            if child.card == first_card:
                for child2 in child.children:
                    if child2.card == second_card:
                        correct_node = child2

        tretji_node = min(correct_node.children, key=lambda x: x.points)
        return tretji_node.card

    def print_tree(self, tree):
        print(tree)
        for child in tree.children:
            print(child)
            for child2 in child.children:
                print(child2)
                for child3 in child2.children:
                    print(child3)
    def __str__(self):
        s = ""
        for i in range(self.depth):
            s += "\t"
        s += str(self.card)
        s += " (" + str(self.points) + ")"
        return s





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

    def locally_best_best_agent(self, id):
        children = []
        player_order_duo = [True if x in self.duo else False for x in self.player_order]
        tree = Tree(-1, None, None, children, 3, self)

        first = self.player_order[0]
        second = self.player_order[1]
        third = self.player_order[2]

        for c in self.player_hands_copy[first]:
            children2 = []
            nivo1 = Tree(c, player_order_duo[0], tree, children2, 2, self)
            children.append(nivo1)
            for c2 in self.legal_moves(c, self.player_hands_copy[second]):

                children3 = []
                nivo2 = Tree(c2, player_order_duo[1], nivo1, children3, 1, self)
                children2.append(nivo2)
                for c3 in self.legal_moves(c, self.player_hands_copy[third]):
                    children3.append(Tree(c3, player_order_duo[2], nivo2, None, 0, self))
        tree.eval_tree_max(player_order_duo)

        if id == first:
            return tree.get_first_card_max()

        if id == second:
            return tree.get_second_card_max(self.stack[0])

        if id == third:
            return tree.get_third_card_max(self.stack[0], self.stack[1])

    def locally_worst_worst_agent(self, id):
        children = []
        player_order_duo = [True if x in self.duo else False for x in self.player_order]
        tree = Tree(-1, None, None, children, 3, self)

        first = self.player_order[0]
        second = self.player_order[1]
        third = self.player_order[2]

        for c in self.player_hands_copy[first]:
            children2 = []
            nivo1 = Tree(c, player_order_duo[0], tree, children2, 2, self)
            children.append(nivo1)
            for c2 in self.legal_moves(c, self.player_hands_copy[second]):

                children3 = []
                nivo2 = Tree(c2, player_order_duo[1], nivo1, children3, 1, self)
                children2.append(nivo2)

                for c3 in self.legal_moves(c, self.player_hands_copy[third]):
                    children3.append(Tree(c3, player_order_duo[2], nivo2, None, 0, self))

        tree.eval_tree_min(player_order_duo)

        if id == first:
            return tree.get_first_card_min()

        if id == second:
            return tree.get_second_card_min(self.stack[0])

        if id == third:
            return tree.get_third_card_min(self.stack[0], self.stack[1])


if __name__ == "__main__":
    tb = TarockBasics()
    p1, p2, p3, talon = [2, 7], [5, 4], [3,  6, 8], []
    ma = MilestoneAgents(p1, p2, p3, [1,2,3], 1, [1,3])

    tb.print_hand(p1)
    tb.print_hand(p2)
    tb.print_hand(p3)

    #def __init__(self, card, duo, parent, children, depth, ma):

    children = []
    tree = Tree(-1, None, None, children, 3, ma)



    for c in p1:
        children2 = []
        nivo1 = Tree(c, True, tree, children2, 2, ma)
        children.append(nivo1)
        for c2 in p2:

            children3 = []
            nivo2 = Tree(c2, True, nivo1, children3, 1, ma)
            children2.append(nivo2)

            for c3 in p3:
                children3.append(Tree(c3, False, nivo2, None, 0, ma))


    tree.print_tree(tree)
    tree.eval_tree_max([True, True, False])
    x = tree.get_first_card()
    y = tree.get_second_card(x)
    z = tree.get_third_card(x, y)
    print("------------------------------")
    tree.print_tree(tree)
    print(x, y, z)