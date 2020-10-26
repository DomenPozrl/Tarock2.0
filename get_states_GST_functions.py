from GameStateTarock import GameStateTarock

GET_STATE_PLAY_VERSION1 = [("vrednost igranih kart", [1,2,3]), #1 = runing sum 1, 2 = running sum <= 3, 3 = running sum > 3
					("skrt igrane karte", [0,1]),
					("lahko poberes igrane karte", [0,1]),
					("player2 skrt igrane karte", [0,1]),
					("player3 skrt igrane karte", [0,1]),
					("imam se tarokov", [0,1]),
					("player2 nima vec tarokov", [0,1]),
					("player3 nima vec tarokov", [0,1])]

GET_STATE_OPEN_VERSION1 = [("imas kralja", [0,1]),
				("imas damo", [0,1]),
				("imas pob/caval", [0,1]),
				("imas platlca", [0,1]),
				("imam se tarokov", [0,1]),
				("player2 nima vec tarokov", [0,1]),
				("player3 nima vec tarokov", [0,1])]

GET_STATE_VERSION2 = [("herc kralj", [0,1,2]),
			  ("herc dama", [0,1,2]),
			  ("kara kralj", [0,1,2]),
			  ("kara dama", [0,1,2]),
			  ("pik kralj", [0,1,2]),
			  ("pik dama", [0,1,2]),
			  ("kriz kralj", [0,1,2]),
			  ("kriz dama", [0,1,2]),
			  ("mond", [0,1,2]),
			  ("skis", [0,1,2]),
			  ("pagat", [0,1,2]),
			  ("vrednost stacka", [0,1,2]),
			  ("player2 brez tarokov", [0, 1]),
			  ("player3 brez tarokov", [0, 1])]


def get_state_play_version1(current_player_id, game_state: GameStateTarock):
    """
    state_labels1 = [("vrednost igranih kart", [1,2,3]), #1 = runing sum 1, 2 = running sum <= 3, 3 = running sum > 3
					("skrt igrane karte", [0,1]),
					("lahko poberes igrane karte", [0,1]),
					("player2 skrt igrane karte", [0,1]),
					("player3 skrt igrane karte", [0,1]),
					("imam se tarokov", [0,1]),
					("player2 nima vec tarokov", [0,1]),
					("player3 nima vec tarokov", [0,1])]
    """

    state = []

    #vrednost igranih kart
    if game_state.stack_value <= 1:
        state.append(1)
    elif (game_state.stack_value <= 3) and (game_state.stack_value > 1):
        state.append(2)
    else:
        state.append(3)


    #skrt igrane karte
    if current_player_id == game_state.players[0]:
        if game_state.player1_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)
    elif current_player_id == game_state.players[1]:
        if game_state.player2_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)
    else:
        if game_state.player3_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

    #lahko poberes igrane karte
    if current_player_id == game_state.players[0]:
        if max(game_state.legal_moves(game_state.stack[0], game_state.player1_cards)) > game_state.current_winning_card:
            state.append(1)
        else:
            state.append(0)
    elif current_player_id == game_state.players[1]:
        if max(game_state.legal_moves(game_state.stack[0], game_state.player2_cards)) > game_state.current_winning_card:
            state.append(1)
        else:
            state.append(0)
    else:
        if max(game_state.legal_moves(game_state.stack[0], game_state.player3_cards)) > game_state.current_winning_card:
            state.append(1)
        else:
            state.append(0)

    #player2 skrt igrane karte
    #player3 skrt igrane karte
    if current_player_id == game_state.players[0]:
        if game_state.player2_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

    elif current_player_id == game_state.players[1]:
        if game_state.player1_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

    else:
        if game_state.player1_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player2_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

    #imam se tarokov
    if current_player_id == game_state.players[0]:
        if game_state.player1_skrt["tarock"]:
            state.append(0)
        else:
            state.append(1)
    elif current_player_id == game_state.players[1]:
        if game_state.player2_skrt["tarock"]:
            state.append(0)
        else:
            state.append(1)
    else:
        if game_state.player3_skrt["tarock"]:
            state.append(0)
        else:
            state.append(1)

    # player2 skrt tarokov
    # player3 skrt tarokov
    if current_player_id == game_state.players[0]:
        if game_state.player2_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    elif current_player_id == game_state.players[1]:
        if game_state.player1_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    else:
        if game_state.player1_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player2_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    return state


def get_state_open_version1(current_player_id, game_state: GameStateTarock):
    """
    state_labels2 = [("imas kralja", [0,1]),
				("imas damo", [0,1]),
				("imas pob/caval", [0,1]),
				("imas platlca", [0,1]),
				("imam se tarokov", [0,1]),
				("player2 nima vec tarokov", [0,1]),
				("player3 nima vec tarokov", [0,1])]

    """

    state = []

    #imas kralja
    if current_player_id == game_state.players[0]:

        if (8 in game_state.player1_cards) or (18 in game_state.player1_cards) or (28 in game_state.player1_cards) or (38 in game_state.player1_cards):
            state.append(1)
        else:
            state.append(0)
    elif current_player_id == game_state.players[1]:
        if (8 in game_state.player2_cards) or (18 in game_state.player2_cards) or (28 in game_state.player2_cards) or (38 in game_state.player2_cards):
            state.append(1)
        else:
            state.append(0)
    else:
        if (8 in game_state.player3_cards) or (18 in game_state.player3_cards) or (28 in game_state.player3_cards) or (38 in game_state.player3_cards):
            state.append(1)
        else:
            state.append(0)
    #print("imas kralja", state)

    # imas damo
    if current_player_id == game_state.players[0]:

        if (7 in game_state.player1_cards) or (17 in game_state.player1_cards) or (27 in game_state.player1_cards) or (37 in game_state.player1_cards):
            state.append(1)
        else:
            state.append(0)
    elif current_player_id == game_state.players[1]:
        if (7 in game_state.player2_cards) or (17 in game_state.player2_cards) or (27 in game_state.player2_cards) or (37 in game_state.player2_cards):
            state.append(1)
        else:
            state.append(0)
    else:
        if (7 in game_state.player3_cards) or (17 in game_state.player3_cards) or (27 in game_state.player3_cards) or (37 in game_state.player3_cards):
            state.append(1)
        else:
            state.append(0)
    #print("imas damo", state)

    #imas pob/caval
    if current_player_id == game_state.players[0]:

        if (6 in game_state.player1_cards) or (16 in game_state.player1_cards) or (26 in game_state.player1_cards) or (36 in game_state.player1_cards) or (5 in game_state.player1_cards) or (15 in game_state.player1_cards) or (25 in game_state.player1_cards) or (35 in game_state.player1_cards):
            state.append(1)
        else:
            state.append(0)
    elif current_player_id == game_state.players[1]:
        if (6 in game_state.player2_cards) or (16 in game_state.player2_cards) or (26 in game_state.player2_cards) or (36 in game_state.player2_cards) or (5 in game_state.player2_cards) or (15 in game_state.player2_cards) or (25 in game_state.player2_cards) or (35 in game_state.player2_cards):
            state.append(1)
        else:
            state.append(0)
    else:
        if (6 in game_state.player2_cards) or (16 in game_state.player3_cards) or (26 in game_state.player3_cards) or (36 in game_state.player3_cards) or (5 in game_state.player3_cards) or (15 in game_state.player3_cards) or (25 in game_state.player3_cards) or (35 in game_state.player3_cards):
            state.append(1)
        else:
            state.append(0)
    #print("imas pob/caval", state)

    #imas platlca
    if current_player_id == game_state.players[0]:

        sem = False
        for card in game_state.player1_cards:
            if card in game_state.platelci:
                sem = True
        if not sem:
            state.append(0)
        else:
            state.append(1)

    elif current_player_id == game_state.players[1]:
        sem = False
        for card in game_state.player2_cards:
            if card in game_state.platelci:
                sem = True
        if not sem:
            state.append(0)
        else:
            state.append(1)

    else:
        sem = False
        for card in game_state.player3_cards:
            if card in game_state.platelci:
                sem = True
        if not sem:
            state.append(0)
        else:
            state.append(1)

    # imas se tarokov
    if current_player_id == game_state.players[0]:
        if game_state.player1_skrt["tarock"]:
            state.append(0)
        else:
            state.append(1)

    elif current_player_id == game_state.players[1]:
        if game_state.player2_skrt["tarock"]:
            state.append(0)
        else:
            state.append(1)
    else:
        if game_state.player3_skrt["tarock"]:
            state.append(0)
        else:
            state.append(1)
    #print("imas platlc", state)
    #player2 nima vec tarokov
    #player3 nima vec tarokov
    if current_player_id == game_state.players[0]:

        if game_state.player2_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    elif current_player_id == game_state.players[1]:
        if game_state.player1_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    else:
        if game_state.player1_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player2_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)
    #print("skrt taroka player2 in player3", state)
    return state


def get_state_version2(current_player_id, game_state: GameStateTarock):
    #this state is a bit different
    #instead of binary attributes we have 3 values for each
    #0 -> ni v igri
    #1 -> imam jz
    #2 -> je v igri nimam jz
    """
    :param current_player_id: id of the player calling for the state
    :param game_state: the gamestate struct with all the information
    :return: a vector which represents the current state of the game
    """
    """
    GET_STATE_VERSION2 = [("herc kralj", [0,1,2]),
			  ("herc dama", [0,1,2]),
			  ("kara kralj", [0,1,2]),
			  ("kara dama", [0,1,2]),
			  ("pik kralj", [0,1,2]),
			  ("pik dama", [0,1,2]),
			  ("kriz kralj", [0,1,2]),
			  ("kriz dama", [0,1,2]),
			  ("mond", [0,1,2]),
			  ("skis", [0,1,2]),
			  ("pagat", [0,1,2]),
			  ("vrednost stacka", [0,1,2]),
			  ("player2 brez tarokov", [0, 1]),
			  ("player3 brez tarokov", [0, 1])]
    """

    vector = []

    #herc kralj
    if 8 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 8 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 0:
        vector.append(2)

    #herc dama
    if 7 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 7 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 1:
        vector.append(2)

    # karo kralj
    if 18 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 18 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 2:
        vector.append(2)

    # karo dama
    if 17 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 17 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 3:
        vector.append(2)

    #pik kralj
    if 28 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 28 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 4:
        vector.append(2)

    #pik dama
    if 27 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 27 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 5:
        vector.append(2)

    #kriz kralj
    if 38 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 38 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 6:
        vector.append(2)

    #kriz dama
    if 37 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 37 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 7:
        vector.append(2)

    #mond
    if 60 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 60 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 8:
        vector.append(2)

    #skis
    if 61 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 61 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 9:
        vector.append(2)

    #pagat
    if 40 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 40 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 10:
        vector.append(2)

    # vrednost igranih kart
    if game_state.stack_value <= 1:
        vector.append(1)
    elif (game_state.stack_value <= 3) and (game_state.stack_value > 1):
        vector.append(2)
    else:
        vector.append(3)

    # player2 skrt tarokov
    # player3 skrt tarokov
    if current_player_id == game_state.players[0]:
        if game_state.player2_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

        if game_state.player3_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

    elif current_player_id == game_state.players[1]:
        if game_state.player1_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

        if game_state.player3_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

    else:
        if game_state.player1_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

        if game_state.player2_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

    return vector