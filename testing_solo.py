from TarockBasics import *
from GameStateTarock import *
from MilestoneAgents import *
from get_states_GST_functions import *
from QLearning import *
from action_functions import *

#Q tables
solo_first = None
solo_second = None
solo_third = None
duo_first = None
duo_second = None
duo_third = None

#get states functions
solo_first_fun = None
solo_second_fun = None
solo_third_fun = None
duo_first_fun = None
duo_second_fun = None
duo_third_fun = None


#action functions
solo_first_action = None
solo_first_action_len = 0
solo_second_action = None
solo_second_action_len = 0
solo_third_action = None
solo_third_action_len = 0
duo_first_action = None
duo_first_action_len = 0
duo_second_action = None
duo_second_action_len = 0
duo_third_action = None
duo_third_action_len = 0

def set_table_function_vars_version1():
    #get states version1 tables
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    solo_first = dict()
    solo_second = dict()
    solo_third = solo_second
    duo_first = solo_first
    duo_second = solo_second
    duo_third = solo_third

    #get states version1 functions
    solo_first_fun = get_state_version1_open
    solo_second_fun = get_state_version1_play
    solo_third_fun = solo_second_fun
    duo_first_fun = solo_first_fun
    duo_second_fun = solo_second_fun
    duo_third_fun = solo_third_fun

def load_table_function_vars_version1(filename1, filename2):
    #get states version1 tables
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    file1 = open(filename1, "rb")
    file2 = open(filename2, "rb")

    solo_first = pickle.load(file1)
    solo_second = pickle.load(file2)
    file1.close()
    file2.close()

    solo_third = solo_second
    duo_first = solo_first
    duo_second = solo_second
    duo_third = solo_third

    #get states version1 functions
    solo_first_fun = get_state_version1_open
    solo_second_fun = get_state_version1_play
    solo_third_fun = solo_second_fun
    duo_first_fun = solo_first_fun
    duo_second_fun = solo_second_fun
    duo_third_fun = solo_third_fun

def set_table_function_vars_version2():
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    #get states version2 tables
    solo_first = dict()
    solo_second = solo_first
    solo_third = solo_first
    duo_first = solo_first
    duo_second = solo_first
    duo_third = solo_first

    #get states version2 functions
    solo_first_fun = get_state_version2
    solo_second_fun = solo_first_fun
    solo_third_fun = solo_first_fun
    duo_first_fun = solo_first_fun
    duo_second_fun = solo_first_fun
    duo_third_fun = solo_first_fun

def load_table_function_vars_version2(filename1):
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    #get states version2 tables
    file1 = open(filename1, "rb")
    solo_first = pickle.load(file1)
    file1.close()

    solo_second = solo_first
    solo_third = solo_first
    duo_first = solo_first
    duo_second = solo_first
    duo_third = solo_first

    #get states version2 functions
    solo_first_fun = get_state_version2
    solo_second_fun = solo_first_fun
    solo_third_fun = solo_first_fun
    duo_first_fun = solo_first_fun
    duo_second_fun = solo_first_fun
    duo_third_fun = solo_first_fun

def set_table_function_vars_version3():
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    #get states version3 tables
    solo_first = dict()
    solo_second = dict()
    solo_third = dict()
    duo_first = dict()
    duo_second = dict()
    duo_third = dict()

    #get states version3 functions
    solo_first_fun = get_state_version3_solo_open
    solo_second_fun = get_state_version3_solo_second
    solo_third_fun = get_state_version3_solo_third
    duo_first_fun = get_state_version3_duo_open
    duo_second_fun = get_state_version3_duo_second
    duo_third_fun = get_state_version3_duo_third


def load_table_function_vars_version3(filename1, filename2, filename3, filename4, filename5, filename6):
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    file1 = open(filename1, "rb")
    file2 = open(filename2, "rb")
    file3 = open(filename3, "rb")
    file4 = open(filename4, "rb")
    file5 = open(filename5, "rb")
    file6 = open(filename6, "rb")

    #get states version3 tables
    solo_first = pickle.load(file1)
    solo_second = pickle.load(file2)
    solo_third = pickle.load(file3)
    duo_first = pickle.load(file4)
    duo_second = pickle.load(file5)
    duo_third = pickle.load(file6)

    file1.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file6.close()

    #get states version3 functions
    solo_first_fun = get_state_version3_solo_open
    solo_second_fun = get_state_version3_solo_second
    solo_third_fun = get_state_version3_solo_third
    duo_first_fun = get_state_version3_duo_open
    duo_second_fun = get_state_version3_duo_second
    duo_third_fun = get_state_version3_duo_third

def set_action_vars_version1():
    global solo_first_action
    global solo_second_action
    global solo_third_action
    global duo_first_action
    global duo_second_action
    global duo_third_action
    global solo_first_action_len
    global solo_second_action_len
    global solo_third_action_len
    global duo_first_action_len
    global duo_second_action_len
    global duo_third_action_len

    solo_first_action = get_actions_version1_open
    solo_first_action_len = len(ACTIONS_VERSION1_OPEN)

    solo_second_action = get_actions_version1_play
    solo_second_action_len = len(ACTIONS_VERSION1_PLAY)

    solo_third_action = solo_second_action
    solo_third_action_len = solo_second_action_len


    duo_first_action = solo_first_action
    duo_first_action_len = solo_first_action_len

    duo_second_action = solo_second_action
    duo_second_action_len = solo_second_action_len

    duo_third_action = solo_third_action
    duo_third_action_len = solo_third_action_len

def set_action_vars_version2():

    global solo_first_action
    global solo_second_action
    global solo_third_action
    global duo_first_action
    global duo_second_action
    global duo_third_action
    global solo_first_action_len
    global solo_second_action_len
    global solo_third_action_len
    global duo_first_action_len
    global duo_second_action_len
    global duo_third_action_len

    solo_first_action = get_actions_version2
    solo_first_action_len = len(ACTIONS_VERSION2)

    solo_second_action = get_actions_version2
    solo_second_action_len = len(ACTIONS_VERSION2)

    solo_third_action = solo_second_action
    solo_third_action_len = solo_first_action_len


    duo_first_action = solo_first_action
    duo_first_action_len = solo_first_action_len

    duo_second_action = solo_second_action
    duo_second_action_len = solo_second_action_len

    duo_third_action = solo_third_action
    duo_third_action_len = solo_third_action_len

def set_action_vars_version3():
    global solo_first_action
    global solo_second_action
    global solo_third_action
    global duo_first_action
    global duo_second_action
    global duo_third_action
    global solo_first_action_len
    global solo_second_action_len
    global solo_third_action_len
    global duo_first_action_len
    global duo_second_action_len
    global duo_third_action_len

    solo_first_action = get_actions_version3_open
    solo_first_action_len = len(ACTIONS_VERSION3_OPEN)

    solo_second_action = get_actions_version3_play
    solo_second_action_len = len(ACTIONS_VERSION3_PLAY)

    solo_third_action = solo_second_action
    solo_third_action_len = solo_second_action_len


    duo_first_action = solo_first_action
    duo_first_action_len = solo_first_action_len

    duo_second_action = solo_second_action
    duo_second_action_len = solo_second_action_len

    duo_third_action = solo_third_action
    duo_third_action_len = solo_third_action_len


if __name__ == "__main__":

    player1 = "3_3"
    player2 = "LB"
    player3 = "LB"

    player1_id = 1
    player2_id = 2
    player3_id = 3

    if player1 == "1_1":
        load_table_function_vars_version1("q_tables/solo_first_1_1.pickle", "q_tables/solo_second_1_1.pickle")
        set_action_vars_version1()
    if player1 == "2_2":
        load_table_function_vars_version2("q_tables/solo_first_2_2.pickle")
        set_action_vars_version2()
    if player1 == "3_3":
        load_table_function_vars_version3("q_tables/solo_first_3_3.pickle", "q_tables/solo_second_3_3.pickle", "q_tables/solo_third_3_3.pickle", "q_tables/duo_first_3_3.pickle", "q_tables/duo_second_3_3.pickle", "q_tables/duo_third_3_3.pickle")
        set_action_vars_version3()

    qlearning = QLearning(1, 0.1, 0.2)
    count = 0
    number_of_games = 10000
    file = open(player1 + "_" + player2 + "_" + player3, "w")

    ss = ""
    while count < number_of_games:

        tb = TarockBasics()

        p1, p2, p3, talon = tb.deal_cards()
        ma = MilestoneAgents(p1, p2, p3, [1,2,3], 1, [2, 3])

        points_dict = {1: 0, 2: 0, 3:0}


        s = "--------------------------\n"
        s += str(p1) + "\n"
        s += str(p2) + "\n"
        s += str(p3) + "\n"
        s += str(talon) + "\n"
        while p1:

            first = ma.player_order[0]
            second = ma.player_order[1]
            third = ma.player_order[2]

            if first == player1_id:

                # get state
                state1 = solo_first_fun(first, ma)

                # current vector of q table for this state
                if state1 in solo_first:
                    vector = solo_first[state1]
                else:
                    vector = [0 for i in range(solo_first_action_len)]
                    solo_first[state1] = vector

                # get card
                rez = solo_first_action(vector, ma.player_hands[first], ma)
                card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
                ma.update_state(card, first)

                if second == player2_id:
                    if player2 == "random":
                        card = ma.random_agent(second)
                    elif player2 == "LW":
                        card = ma.locally_worst_agent(second)
                    else:
                        card = ma.locally_best_agent(second)
                    ma.update_state(card, second)
                else:
                    if player3 == "random":
                        card = ma.random_agent(second)
                    elif player3 == "LW":
                        card = ma.locally_worst_agent(second)
                    else:
                        card = ma.locally_best_agent(second)
                    ma.update_state(card, second)

                if third == player3_id:
                    if player3 == "random":
                        card = ma.random_agent(third)
                    elif player3 == "LW":
                        card = ma.locally_worst_agent(third)
                    else:
                        card = ma.locally_best_agent(third)
                    ma.update_state(card, third)
                else:
                    if player2 == "random":
                        card = ma.random_agent(third)
                    elif player2 == "LW":
                        card = ma.locally_worst_agent(third)
                    else:
                        card = ma.locally_best_agent(third)
                    ma.update_state(card, third)

            elif second == player1_id:

                if first == player2_id:
                    if player2 == "random":
                        card = ma.random_agent(first)
                    elif player2 == "LW":
                        card = ma.locally_worst_agent(first)
                    else:
                        card = ma.locally_best_agent(first)
                    ma.update_state(card, first)
                else:
                    if player3 == "random":
                        card = ma.random_agent(first)
                    elif player3 == "LW":
                        card = ma.locally_worst_agent(first)
                    else:
                        card = ma.locally_best_agent(first)
                    ma.update_state(card, first)

                # get state
                state1 = solo_second_fun(second, ma)

                # current vector of q table for this state
                if state1 in solo_second:
                    vector = solo_second[state1]
                else:
                    vector = [0 for i in range(solo_second_action_len)]
                    solo_second[state1] = vector

                # get card
                rez = solo_second_action(vector, ma.player_hands[second], ma)
                card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
                ma.update_state(card, second)



                if third == player3_id:
                    if player3 == "random":
                        card = ma.random_agent(third)
                    elif player3 == "LW":
                        card = ma.locally_worst_agent(third)
                    else:
                        card = ma.locally_best_agent(third)
                    ma.update_state(card, third)
                else:
                    if player2 == "random":
                        card = ma.random_agent(third)
                    elif player2 == "LW":
                        card = ma.locally_worst_agent(third)
                    else:
                        card = ma.locally_best_agent(third)
                    ma.update_state(card, third)

            else:

                if first == player2_id:
                    if player2 == "random":
                        card = ma.random_agent(first)
                    elif player2 == "LW":
                        card = ma.locally_worst_agent(first)
                    else:
                        card = ma.locally_best_agent(first)
                    ma.update_state(card, first)
                else:
                    if player3 == "random":
                        card = ma.random_agent(first)
                    elif player3 == "LW":
                        card = ma.locally_worst_agent(first)
                    else:
                        card = ma.locally_best_agent(first)
                    ma.update_state(card, first)

                if second == player2_id:
                    if player2 == "random":
                        card = ma.random_agent(second)
                    elif player2 == "LW":
                        card = ma.locally_worst_agent(second)
                    else:
                        card = ma.locally_best_agent(second)
                    ma.update_state(card, second)
                else:
                    if player3 == "random":
                        card = ma.random_agent(second)
                    elif player3 == "LW":
                        card = ma.locally_worst_agent(second)
                    else:
                        card = ma.locally_best_agent(second)
                    ma.update_state(card, second)

                # get state
                state1 = solo_third_fun(third, ma)

                # current vector of q table for this state
                if state1 in solo_third:
                    vector = solo_third[state1]
                else:
                    vector = [0 for i in range(solo_third_action_len)]
                    solo_third[state1] = vector

                # get card
                rez = solo_third_action(vector, ma.player_hands[third], ma)
                card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
                ma.update_state(card, third)


            wp = ma.winning_card(ma.stack)
            points_dict[ma.player_order[wp]] += ma.eval_stack(ma.stack)

            ma.clear_state()


        s += str(points_dict) + "\n"
        ss += s
        count += 1

    file.write(ss)
    file.close()











