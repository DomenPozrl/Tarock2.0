import pickle
from get_states_GST_functions import *
from action_functions import *
from MilestoneAgents import *

#############################################################################################
########################################2_2##################################################
#############################################################################################
#Q tables
solo_first_2_2 = pickle.load(open("q_tables/solo_first_2_2.pickle", "rb"))
solo_second_2_2 = solo_first_2_2
solo_third_2_2 = solo_second_2_2
duo_first_2_2 = solo_first_2_2
duo_second_2_2 = solo_second_2_2
duo_third_2_2 = solo_second_2_2

#get states functions
solo_first_fun_2_2 = get_state_version2
solo_second_fun_2_2 = solo_first_fun_2_2
solo_third_fun_2_2 = solo_first_fun_2_2
duo_first_fun_2_2 = solo_first_fun_2_2
duo_second_fun_2_2 = solo_first_fun_2_2
duo_third_fun_2_2 = solo_first_fun_2_2


#action functions
solo_first_action_2_2 = get_actions_version2
solo_first_action_len_2_2 = len(ACTIONS_VERSION2)
solo_second_action_2_2 = solo_first_action_2_2
solo_second_action_len_2_2 = solo_first_action_len_2_2
solo_third_action_2_2 = solo_first_action_2_2
solo_third_action_len_2_2 = solo_first_action_len_2_2
duo_first_action_2_2 = solo_first_action_2_2
duo_first_action_len_2_2 = solo_first_action_len_2_2
duo_second_action_2_2 = solo_first_action_2_2
duo_second_action_len_2_2 = solo_first_action_len_2_2
duo_third_action_2_2 = solo_first_action_2_2
duo_third_action_len_2_2 = solo_first_action_len_2_2

#############################################################################################
#############################################################################################
#############################################################################################

def get_solo_first_card_2_2(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_first_fun_2_2(id, ma)

    # current vector of q table for this state
    if state1 in solo_first_2_2:
        vector = solo_first_2_2[state1]
    else:
        vector = [0 for i in range(solo_first_action_len_2_2)]
        solo_first_2_2[state1] = vector

    # get card
    rez = solo_first_action_2_2(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_second_card_2_2(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_second_fun_2_2(id, ma)

    # current vector of q table for this state
    if state1 in solo_second_2_2:
        vector = solo_second_2_2[state1]
    else:
        vector = [0 for i in range(solo_second_action_len_2_2)]
        solo_second_2_2[state1] = vector

    # get card
    rez = solo_second_action_2_2(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_third_card_2_2(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_third_fun_2_2(id, ma)

    # current vector of q table for this state
    if state1 in solo_third_2_2:
        vector = solo_third_2_2[state1]
    else:
        vector = [0 for i in range(solo_third_action_len_2_2)]
        solo_third_2_2[state1] = vector

    # get card
    rez = solo_third_action_2_2(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_first_card_2_2(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_first_fun_2_2(id, ma)

    # current vector of q table for this state
    if state1 in duo_first_2_2:
        vector = duo_first_2_2[state1]
    else:
        vector = [0 for i in range(duo_first_action_len_2_2)]
        duo_first_2_2[state1] = vector

    # get card
    rez = duo_first_action_2_2(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_second_card_2_2(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_second_fun_2_2(id, ma)

    # current vector of q table for this state
    if state1 in duo_second_2_2:
        vector = duo_second_2_2[state1]
    else:
        vector = [0 for i in range(duo_second_action_len_2_2)]
        duo_second_2_2[state1] = vector

    # get card
    rez = duo_second_action_2_2(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_third_card_2_2(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_third_fun_2_2(id, ma)

    # current vector of q table for this state
    if state1 in duo_third_2_2:
        vector = duo_third_2_2[state1]
    else:
        vector = [0 for i in range(duo_third_action_len_2_2)]
        duo_third_2_2[state1] = vector

    # get card
    rez = duo_third_action_2_2(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card