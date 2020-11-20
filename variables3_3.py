import pickle
from get_states_GST_functions import *
from action_functions import *
from MilestoneAgents import *

#############################################################################################
########################################3_3##################################################
#############################################################################################
#Q tables
solo_first_3_3 = pickle.load(open("q_tables/solo_first_3_3.pickle", "rb"))
solo_second_3_3 = pickle.load(open("q_tables/solo_second_3_3.pickle", "rb"))
solo_third_3_3 = pickle.load(open("q_tables/solo_third_3_3.pickle", "rb"))
duo_first_3_3 = pickle.load(open("q_tables/duo_first_3_3.pickle", "rb"))
duo_second_3_3 = pickle.load(open("q_tables/duo_second_3_3.pickle", "rb"))
duo_third_3_3 = pickle.load(open("q_tables/duo_third_3_3.pickle", "rb"))

#get states functions
solo_first_fun_3_3 = get_state_version3_solo_open
solo_second_fun_3_3 = get_state_version3_solo_second
solo_third_fun_3_3 = get_state_version3_solo_third
duo_first_fun_3_3 = get_state_version3_duo_open
duo_second_fun_3_3 = get_state_version3_duo_second
duo_third_fun_3_3 = get_state_version3_duo_third


#action functions
solo_first_action_3_3 = get_actions_version3_open
solo_first_action_len_3_3 = len(ACTIONS_VERSION3_OPEN)
solo_second_action_3_3 = get_actions_version3_play
solo_second_action_len_3_3 = len(ACTIONS_VERSION3_PLAY)
solo_third_action_3_3 = solo_second_action_3_3
solo_third_action_len_3_3 = solo_second_action_len_3_3
duo_first_action_3_3 = solo_first_action_3_3
duo_first_action_len_3_3 = solo_first_action_len_3_3
duo_second_action_3_3 = solo_second_action_3_3
duo_second_action_len_3_3 = solo_second_action_len_3_3
duo_third_action_3_3 = solo_second_action_3_3
duo_third_action_len_3_3 = solo_second_action_len_3_3

#############################################################################################
#############################################################################################
#############################################################################################

def get_solo_first_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_first_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in solo_first_3_3:
        vector = solo_first_3_3[state1]
    else:
        vector = [0 for i in range(solo_first_action_len_3_3)]
        solo_first_3_3[state1] = vector

    # get card
    rez = solo_first_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_second_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_second_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in solo_second_3_3:
        vector = solo_second_3_3[state1]
    else:
        vector = [0 for i in range(solo_second_action_len_3_3)]
        solo_second_3_3[state1] = vector

    # get card
    rez = solo_second_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_third_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_third_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in solo_third_3_3:
        vector = solo_third_3_3[state1]
    else:
        vector = [0 for i in range(solo_third_action_len_3_3)]
        solo_third_3_3[state1] = vector

    # get card
    rez = solo_third_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_first_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_first_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in duo_first_3_3:
        vector = duo_first_3_3[state1]
    else:
        vector = [0 for i in range(duo_first_action_len_3_3)]
        duo_first_3_3[state1] = vector

    # get card
    rez = duo_first_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_second_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_second_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in duo_second_3_3:
        vector = duo_second_3_3[state1]
    else:
        vector = [0 for i in range(duo_second_action_len_3_3)]
        duo_second_3_3[state1] = vector

    # get card
    rez = duo_second_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_third_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_third_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in duo_third_3_3:
        vector = duo_third_3_3[state1]
    else:
        vector = [0 for i in range(duo_third_action_len_3_3)]
        duo_third_3_3[state1] = vector

    # get card
    rez = duo_third_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card