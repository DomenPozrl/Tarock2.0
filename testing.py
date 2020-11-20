from MilestoneAgents import *
from QLearning import *
from variables1_1 import *
from variables2_2 import *
from variables3_3 import *

def play_one_game(ma: MilestoneAgents, player_strats, qlearning):
    """

    :param ma: instance of MilestoneAgents class
    :param player_strats: dict which contains as keys the id of player and values the play strats
    :param qlearning: instance of class qlearning
    :return:
    """
    points_dict = {pid: 0 for pid in ma.players}
    points = []
    winner = []
    while ma.player1_cards:

        #store player ids
        first = ma.player_order[0]
        second = ma.player_order[1]
        third = ma.player_order[2]

        played = [first, second, third]
        ##################################################################

        if player_strats[first] == "1_1":
            if first not in ma.duo:
                card1 = get_solo_first_card_1_1(ma, first, qlearning)
            else:
                card1 = get_duo_first_card_1_1(ma, first, qlearning)
        elif player_strats[first] == "2_2":
            if first not in ma.duo:
                card1 = get_solo_first_card_2_2(ma, first, qlearning)
            else:
                card1 = get_duo_first_card_2_2(ma, first, qlearning)
        elif player_strats[first] == "3_3":
            if first not in ma.duo:
                card1 = get_solo_first_card_3_3(ma, first, qlearning)
            else:
                card1 = get_duo_first_card_3_3(ma, first, qlearning)
        elif player_strats[first] == "random":
            card1 = ma.random_agent(first)
        elif player_strats[first] == "LW":
            card1 = ma.locally_worst_agent(first)
        elif player_strats[first] == "LB":
            card1 = ma.locally_best_agent(first)
        elif player_strats[first] == "LBB":
            card1 = ma.locally_best_best_agent(first)
        elif player_strats[first] == "LWW":
            card1 = ma.locally_worst_worst_agent(first)
        else:
            raise NotImplemented

        ma.update_state(card1, first)

        ##################################################################

        if player_strats[second] == "1_1":
            if second not in ma.duo:
                card2 = get_solo_second_card_1_1(ma, second, qlearning)
            else:
                card2 = get_duo_second_card_1_1(ma, second, qlearning)
        elif player_strats[second] == "2_2":
            if second not in ma.duo:
                card2 = get_solo_second_card_2_2(ma, second, qlearning)
            else:
                card2 = get_duo_second_card_2_2(ma, second, qlearning)
        elif player_strats[second] == "3_3":
            if second not in ma.duo:
                card2 = get_solo_second_card_3_3(ma, second, qlearning)
            else:
                card2 = get_duo_second_card_3_3(ma, second, qlearning)
        elif player_strats[second] == "random":
            card2 = ma.random_agent(second)
        elif player_strats[second] == "LW":
            card2 = ma.locally_worst_agent(second)
        elif player_strats[second] == "LB":
            card2 = ma.locally_best_agent(second)
        elif player_strats[second] == "LBB":
            card2 = ma.locally_best_best_agent(second)
        elif player_strats[second] == "LWW":
            card2 = ma.locally_worst_worst_agent(second)
        else:

            raise NotImplemented

        ma.update_state(card2, second)

        ##################################################################

        if player_strats[third] == "1_1":
            if third not in ma.duo:
                card3 = get_solo_third_card_1_1(ma, third, qlearning)
            else:
                card3 = get_duo_third_card_1_1(ma, third, qlearning)
        elif player_strats[third] == "2_2":
            if third not in ma.duo:
                card3 = get_solo_third_card_2_2(ma, third, qlearning)
            else:
                card3 = get_duo_third_card_2_2(ma, third, qlearning)
        elif player_strats[third] == "3_3":
            if third not in ma.duo:
                card3 = get_solo_third_card_3_3(ma, third, qlearning)
            else:
                card3 = get_duo_third_card_3_3(ma, third, qlearning)
        elif player_strats[third] == "random":
            card3 = ma.random_agent(third)
        elif player_strats[third] == "LW":
            card3 = ma.locally_worst_agent(third)
        elif player_strats[third] == "LB":
            card3 = ma.locally_best_agent(third)
        elif player_strats[third] == "LBB":
            card3 = ma.locally_best_best_agent(third)
        elif player_strats[third] == "LWW":
            card3 = ma.locally_worst_worst_agent(third)
        else:
            raise NotImplemented

        ma.update_state(card3, third)

        ##################################################################
        wp = ma.winning_card(ma.stack)
        points_dict[played[wp]] += ma.eval_stack(ma.stack)
        ma.clear_state()

    return points_dict

if __name__ == "__main__":

    #player can be anything from 1_1, 2_2, 3_3, random, LW, LB, LBB
    play_modes = ["1_1", "2_2", "3_3", "random", "LW", "LB", "LWW", "LBB"]
    qlearning = QLearning(0.1, 0.1, 0.1)

    for mode1 in play_modes:
        for mode2 in play_modes:
            for mode3 in play_modes:
                print(f"Working on: {mode1} {mode2} {mode3}")
                count = 0
                file = open(mode1 + " " + mode2 + " " + mode3, "w")

                s = ""
                while count < 1000:
                    print(count/1000)

                    #init data to store into file
                    data = dict()

                    #choose solo/duo
                    solo = random.choice([1,2,3])
                    duo = [x for x in [1,2,3] if x != solo]

                    data["solo"] = str(solo)
                    data["duo"] = str(duo)

                    #deal cards and setup ma
                    tb = TarockBasics()
                    p1, p2, p3, talon = tb.deal_cards()

                    data["p1"] = copy.deepcopy(p1)
                    data["p2"] = copy.deepcopy(p2)
                    data["p3"] = copy.deepcopy(p3)
                    data["talon"] = copy.deepcopy(talon)
                    ma = MilestoneAgents(p1, p2, p3, [1,2,3], solo, duo)
                    ma.update_state_talon(talon)

                    #play one game
                    points = play_one_game(ma, {1: mode1, 2: mode2, 3: mode3}, qlearning)
                    data["points"] = points
                    data["discard"] = ma.discard



                    s += str(data) + "\n"
                    count += 1
                file.write(s)
                file.close()

