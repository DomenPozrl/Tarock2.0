from QLearning import *
from GameStateTarock import *
from get_states_GST_functions import *
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

def set_table_function_vars_version4():
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
    solo_first_fun = get_state_version4
    solo_second_fun = solo_first_fun
    solo_third_fun = solo_first_fun
    duo_first_fun = solo_first_fun
    duo_second_fun = solo_first_fun
    duo_third_fun = solo_first_fun



if __name__ == "__main__":

    qlearning = QLearning(1, 0.1, 0.2)
    num_games = 1000000
    count = 0


    #cant combine action vars1 and vars3 with table vars2
    #that is because q table for version2 has only 1 table but the previously mentioned actions have two different size vectors
    #so this is a no go

    set_table_function_vars_version4()
    set_action_vars_version2()
    #print(solo_first, solo_second, solo_third, duo_first, duo_second, duo_third)
    while count < num_games:
        print(count/num_games)

        #deal cards
        tb = TarockBasics()
        p1, p2, p3, talon = tb.deal_cards()

        #init the game state
        gst = GameStateTarock(p1, p2, p3, [1,2,3], 1, [2,3])

        #update the state according to talon cards
        gst.update_state_talon(talon)


        #play while there are still cards in p1
        while p1:

            first = gst.player_order[0]
            second = gst.player_order[1]
            third = gst.player_order[2]


            #first player plays
            if first not in gst.duo:

                #get state
                state1 = solo_first_fun(first, gst)

                #current vector of q table for this state
                if state1 in solo_first:
                    vector = solo_first[state1]
                else:
                    vector = [0 for i in range(solo_first_action_len)]
                    solo_first[state1] = vector

                #get card
                rez = solo_first_action(vector, gst.player_hands[first], gst)
                card, action_index1, num_possible_actions1 = qlearning.choose_action(rez)
                gst.update_state(card, first)
            else:
                state1 = duo_first_fun(first, gst)

                # current vector of q table for this state
                if state1 in duo_first:
                    vector = duo_first[state1]
                else:
                    vector = [0 for i in range(duo_first_action_len)]
                    duo_first[state1] = vector

                # get card
                rez = duo_first_action(vector, gst.player_hands[first], gst)
                card, action_index1, num_possible_actions1 = qlearning.choose_action(rez)
                gst.update_state(card, first)

            # second player plays
            if second not in gst.duo:

                state2 = solo_second_fun(second, gst)

                # current vector of q table for this state
                if state2 in solo_second:
                    vector = solo_second[state2]
                else:
                    vector = [0 for i in range(solo_second_action_len)]
                    solo_second[state2] = vector

                # get card
                rez = solo_second_action(vector, gst.player_hands[second], gst)
                card, action_index2, num_possible_actions2 = qlearning.choose_action(rez)
                gst.update_state(card, second)

            else:
                state2 = duo_second_fun(second, gst)

                # current vector of q table for this state
                if state2 in duo_second:
                    vector = duo_second[state2]
                else:
                    vector = [0 for i in range(duo_second_action_len)]
                    duo_second[state2] = vector

                # get card
                # print(vector, gst.player_hands[second])
                rez = duo_second_action(vector, gst.player_hands[second], gst)
                card, action_index2, num_possible_actions2 = qlearning.choose_action(rez)
                gst.update_state(card, second)

            # third player plays
            if third not in gst.duo:
                state3 = solo_third_fun(third, gst)

                # current vector of q table for this state
                if state3 in solo_third:
                    vector = solo_third[state3]
                else:
                    vector = [0 for i in range(solo_third_action_len)]
                    solo_third[state3] = vector

                # get card
                rez = solo_third_action(vector, gst.player_hands[third], gst)
                card, action_index3, num_possible_actions3 = qlearning.choose_action(rez)
                gst.update_state(card, third)

            else:
                state3 = duo_third_fun(third, gst)

                # current vector of q table for this state
                if state3 in duo_third:
                    vector = duo_third[state3]
                else:
                    vector = [0 for i in range(duo_third_action_len)]
                    duo_third[state3] = vector

                # get card
                rez = duo_third_action(vector, gst.player_hands[third], gst)
                card, action_index3, num_possible_actions3 = qlearning.choose_action(rez)
                gst.update_state(card, third)

            #zaenkrat bo reward function samo točke, ki smo jih nabrali po stacku
            points = gst.eval_stack(gst.stack)
            winner = gst.current_winning_player


            # state1, action_index1, num_possible_actions1
            if first == winner:
                if first not in gst.duo:
                    qlearning.update_table(solo_first, state1, action_index1, points*num_possible_actions1)
                else:
                    qlearning.update_table(duo_first, state1, action_index1, points * num_possible_actions1)
            else:
                if first not in gst.duo:
                    qlearning.update_table(solo_first, state1, action_index1, -1*points*num_possible_actions1)
                else:
                    if winner in gst.duo:
                        qlearning.update_table(duo_first, state1, action_index1, 0.5* points * num_possible_actions1)
                    else:
                        qlearning.update_table(duo_first, state1, action_index1, -1 * 0.5 * points * num_possible_actions1)

            # state2, action_index2, num_possible_actions2
            if second == winner:
                if second not in gst.duo:
                    qlearning.update_table(solo_second, state2, action_index2, points*num_possible_actions2)
                else:
                    qlearning.update_table(duo_second, state2, action_index2, points * num_possible_actions2)
            else:
                if second not in gst.duo:
                    qlearning.update_table(solo_second, state2, action_index2, -1 * points * num_possible_actions2)
                else:
                    if winner in gst.duo:
                        qlearning.update_table(duo_second, state2, action_index2, 0.5 * points * num_possible_actions2)
                    else:
                        qlearning.update_table(duo_second, state2, action_index2, -1 * 0.5 * points * num_possible_actions2)

            # state3, action_idnex3, num_possible_actions3
            if third == winner:
                if third not in gst.duo:
                    qlearning.update_table(solo_third, state3, action_index3, points*num_possible_actions3)
                else:
                    qlearning.update_table(duo_third, state3, action_index3, points * num_possible_actions3)
            else:
                if third not in gst.duo:
                    qlearning.update_table(solo_third, state3, action_index3, -1 * points * num_possible_actions3)
                else:
                    if winner in gst.duo:
                        qlearning.update_table(duo_third, state3, action_index3, 0.5 * points * num_possible_actions3)
                    else:
                        qlearning.update_table(duo_third, state3, action_index3, -1 * 0.5 * points * num_possible_actions3)

            gst.clear_state()


        count += 1

    qlearning.pickle_table(solo_first, "solo_first_4_2.pickle")
    #qlearning.pickle_table(solo_second, "solo_second_3_3.pickle")
    #qlearning.pickle_table(solo_third, "solo_third_3_3.pickle")
    #qlearning.pickle_table(duo_first, "duo_first_3_3.pickle")
    #qlearning.pickle_table(duo_second, "duo_second_3_3.pickle")
    #qlearning.pickle_table(duo_third, "duo_third_3_3.pickle")