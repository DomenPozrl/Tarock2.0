import pickle
from get_states_GST_functions import *
from action_functions import *

#############################################################################################
#######################################1_1###################################################
#############################################################################################
#Q tables
solo_first_1_1 = pickle.load(open("q_tables/solo_first_1_1.pickle", "rb"))
solo_second_1_1 = pickle.load(open("q_tables/solo_second_1_1.pickle", "rb"))
solo_third_1_1 = solo_second_1_1
duo_first_1_1 = solo_first_1_1
duo_second_1_1 = solo_second_1_1
duo_third_1_1 = solo_second_1_1

#get states functions
solo_first_fun_1_1 = get_state_version1_open
solo_second_fun_1_1 = get_state_version1_play
solo_third_fun_1_1 = solo_second_fun_1_1
duo_first_fun_1_1 = solo_first_fun_1_1
duo_second_fun_1_1 = solo_second_fun_1_1
duo_third_fun_1_1 = solo_second_fun_1_1


#action functions
solo_first_action_1_1 = get_actions_version1_open
solo_first_action_len_1_1 = len(ACTIONS_VERSION1_OPEN)
solo_second_action_1_1 = get_actions_version1_play
solo_second_action_len_1_1 = len(ACTIONS_VERSION1_PLAY)
solo_third_action_1_1 = solo_second_action_1_1
solo_third_action_len_1_1 = solo_second_action_len_1_1
duo_first_action_1_1 = solo_first_action_1_1
duo_first_action_len_1_1 = solo_first_action_len_1_1
duo_second_action_1_1 = solo_second_action_1_1
duo_second_action_len_1_1 = solo_second_action_len_1_1
duo_third_action_1_1 = solo_second_action_1_1
duo_third_action_len_1_1 = solo_second_action_len_1_1

#############################################################################################
#############################################################################################
#############################################################################################

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