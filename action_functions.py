from GameStateTarock import *
import random

#okay so here is the deal
#there can be various levels of specificity when defining actions
#it can range from win current stack to win play a specific card
#i'm thinking we should define the least specific one (win current stack, pass current stack), the medium (win current stack hard, win current stack small, color, add on) and every specific card


#nevem pol je tuki takoj problem k sta odpret pa igrt efektivno cist razlicni potezi
#tko da rabs razlicne akcije
#jz bi za odpret definiru razlicne akcije pa za igrt razlicne akcije

ACTIONS_VERSION1_OPEN = ["play king", "play queen", "play knight/jack", "play platlc", "play tarok"]
ACTIONS_VERSION1_PLAY = ["win current stack", "pass current stack"]
ACTIONS_VERSION2 = [4, 3, 2, 1, 5, 6, 7, 8, 14, 13, 12, 11, 15, 16, 17, 18, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]
ACTIONS_VERSION3_OPEN = ["herc kral", "herc dama", "herc kaval", "herc pob", "herc platlc", "karo kral", "karo dama", "karo kavla", "karo pob", "karo platlc", "pik kral", "pik dama", "pik kaval", "pik pob", "pik platlc", "kriz kral", "kriz dama", "kriz kaval", "kriz pob", "kriz platlc", "nizek tarok", "srednji tarok", "visok tarok"]
ACTIONS_VERSION3_PLAY = ["pass", "poberi", "stegni se"]

def play_king(hand):
    kralji = {8, 18, 28, 38}
    inter = list(kralji.intersection(set(hand)))
    if inter:
        return True, random.choice(inter)
    else:
        return False, None

def play_queen(hand):
    dame = {7, 17, 27, 37}
    inter = list(dame.intersection(set(hand)))
    if inter:
        return True, random.choice(inter)
    else:
        return False, None

def play_knight_jack(hand):
    knights_jacks = {6, 16, 26, 36, 5, 15, 25, 35}
    inter = list(knights_jacks.intersection(hand))
    if inter:
        return True, random.choice(inter)
    else:
        return False, None

def play_platlc(hand):
    platelci = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34]
    inter = list(set(platelci).intersection(hand))
    if inter:
        return True, random.choice(inter)
    else:
        return False, None

def play_tarock(hand):
    tarocks = list(range(40, 62))
    inter = list(set(tarocks).intersection(hand))
    if inter:
        return True, random.choice(inter)
    else:
        return False, None

def get_actions_version1_open(vector, hand, game_state: GameStateTarock):
    action_names = ["play king", "play queen", "play knight/jack", "play platlc", "play tarok"]
    conf1, king = play_king(hand)
    conf2, queen = play_queen(hand)
    conf3, kjack = play_knight_jack(hand)
    conf4, platlc = play_platlc(hand)
    conf5, tarock = play_tarock(hand)

    conf = [conf1, conf2, conf3, conf4, conf5]
    card = [king, queen, kjack, platlc, tarock]
    return list(zip(vector, conf, card, action_names))

def get_actions_version1_play(vector, hand, game_state: GameStateTarock):
    #win current stack
    #pass current stack

    action_names = ["win current stack", "pass current stack"]
    can_pickup_set = set(game_state.can_pickup_stack(game_state.stack, hand))
    legal_cards_set = set(game_state.legal_moves(game_state.stack[0], hand))
    can_pass_set = legal_cards_set.difference(can_pickup_set)

    can_pickup = True if len(can_pickup_set) >= 1 else False
    can_pass = True if len(can_pass_set) >= 1 else False

    if can_pickup:
        pickup = random.choice(list(can_pickup_set))
    else:
        pickup = None

    if can_pass:
        pass_card = random.choice(list(can_pass_set))
    else:
        pass_card = None

    conf = [can_pickup, can_pass]
    card = [pickup, pass_card]

    return list(zip(vector, conf, card, action_names))

def get_actions_version2(vector, hand, game_state: GameStateTarock):
    action_names = list(game_state.id_to_cards.keys())
    if len(game_state.stack) > 0:
        conf = [True if card in game_state.legal_moves(game_state.stack[0], hand) else False for card in action_names]
    else:
        conf = [True if card in hand else False for card in action_names]

    card = action_names

    return list(zip(vector, conf, card, action_names))

#recimo za odpret bi mel kral, dama, caval, pob, platlc * 4 plus nizek, srednji, visok tarok
def get_actions_version3_open(vector, hand, game_state: GameStateTarock):
    action_names = ["herc kral", "herc dama", "herc kaval", "herc pob", "herc platlc", "karo kral", "karo dama", "karo kavla", "karo pob", "karo platlc", "pik kral", "pik dama", "pik kaval", "pik pob", "pik platlc", "kriz kral", "kriz dama", "kriz kaval", "kriz pob", "kriz platlc", "nizek tarok", "srednji tarok", "visok tarok"]

    #herci
    conf1 = True if 8 in hand else False
    card1 = 8 if conf1 else None
    conf2 = True if 7 in hand else False
    card2 = 7 if conf2 else None
    conf3 = True if 6 in hand else False
    card3 = 6 if conf3 else None
    conf4 = True if 5 in hand else False
    card4 = 5 if conf4 else None
    conf5 = True if len(set(game_state.herc_platelci).intersection(set(hand))) >= 1 else False
    card5 = list(set(game_state.herc_platelci).intersection(set(hand)))[0] if conf5 else None

    #kare
    conf11 = True if 18 in hand else False
    card11 = 18 if conf11 else None
    conf12 = True if 17 in hand else False
    card12 = 17 if conf12 else None
    conf13 = True if 16 in hand else False
    card13 = 16 if conf13 else None
    conf14 = True if 15 in hand else False
    card14 = 15 if conf14 else None
    conf15 = True if len(set(game_state.karo_platelci).intersection(set(hand))) >= 1 else False
    card15 = list(set(game_state.karo_platelci).intersection(set(hand)))[0] if conf15 else None

    #piki
    conf21 = True if 28 in hand else False
    card21 = 28 if conf21 else None
    conf22 = True if 27 in hand else False
    card22 = 27 if conf22 else None
    conf23 = True if 26 in hand else False
    card23 = 26 if conf23 else None
    conf24 = True if 25 in hand else False
    card24 = 25 if conf24 else None
    conf25 = True if len(set(game_state.pik_platelci).intersection(set(hand))) >= 1 else False
    card25 = list(set(game_state.pik_platelci).intersection(set(hand)))[0] if conf25 else None

    #krizi
    conf31 = True if 38 in hand else False
    card31 = 38 if conf31 else None
    conf32 = True if 37 in hand else False
    card32 = 37 if conf32 else None
    conf33 = True if 36 in hand else False
    card33 = 36 if conf33 else None
    conf34 = True if 35 in hand else False
    card34 = 35 if conf34 else None
    conf35 = True if len(set(game_state.kriz_platelci).intersection(set(hand))) >= 1 else False
    card35 = list(set(game_state.kriz_platelci).intersection(set(hand)))[0] if conf35 else None

    # nizki taroki
    if len({40, 41, 42, 43, 44, 45, 46, 47}.intersection(set(hand))) >= 1:
        conf41 = True
    else:
        conf41 = False

    # srednji taroki
    if len({48, 49, 50, 51, 52, 53}.intersection(set(hand))) >= 1:
        conf42 = True
    else:
        conf42 = False

    # visoki taroki
    if len({54, 55, 56, 57, 58, 59, 60, 61}.intersection(set(hand))) >= 1:
        conf43 = True
    else:
        conf43 = False

    card41 = list({40, 41, 42, 43, 44, 45, 46, 47}.intersection(set(hand)))[0] if conf41 else None
    card42 = list({48, 49, 50, 51, 52, 53}.intersection(set(hand)))[0] if conf42 else None
    card43 = list({54, 55, 56, 57, 58, 59, 60, 61}.intersection(set(hand)))[0] if conf43 else None

    conf = [conf1, conf2, conf3, conf4, conf5,
            conf11, conf12, conf13, conf14, conf15,
            conf21, conf22, conf23, conf24, conf25,
            conf31, conf32, conf33, conf34, conf35,
            conf41, conf42, conf43]

    card = [card1, card2, card3, card4, card5,
            card11, card12, card13, card14, card15,
            card21, card22, card23, card24, card25,
            card31, card32, card33, card34, card35,
            card41, card42, card43]

    return list(zip(vector, conf, card, action_names))

#okej dejmo sm torej pass, poberi, stegni
def get_actions_version3_play(vector, hand, game_state: GameStateTarock):

    #pass naj je najnizja karta
    #poberi je najnizja k pobere
    #stegni se je najvisja k pobere

    action_names = ["pass", "poberi", "stegni se"]

    can = game_state.can_pickup_stack(game_state.stack, hand)

    conf1 = True
    conf2 = True if len(can) >= 1 else False
    conf3 = True if len(can) > 1 else False

    card1 = list(sorted(game_state.legal_moves(game_state.stack[0], hand)))[0]
    card2 = list(sorted(can))[0] if conf2 else None
    card3 = list(sorted(can))[-1] if conf3 else None

    conf = [conf1, conf2, conf3]
    card = [card1, card2, card3]

    return list(zip(vector, conf, card, action_names))

if __name__ == "__main__":
    cnt = 0
    while cnt < 100000:
        print(cnt/100000)
        tb = TarockBasics()

        p1, p2, p3, talon = tb.deal_cards()

        gst = GameStateTarock(p1, p2, p3, [1,2,3], 1, [2,3])

        #test version1
        """while p1:

            hand1 = gst.player_hands[gst.player_order[0]]
            hand2 = gst.player_hands[gst.player_order[1]]
            hand3 = gst.player_hands[gst.player_order[2]]

            vector1 = [random.uniform(0, 1) for x in range(len(ACTIONS_VERSION1_OPEN))]
            vector2 = [random.uniform(0, 1) for x in range(len(ACTIONS_VERSION1_PLAY))]
            vector3 = [random.uniform(0, 1) for x in range(len(ACTIONS_VERSION1_PLAY))]

            a, conf1 = get_actions_version1_open(vector1, hand1, gst)
            gst.update_state(a[2], gst.player_order[0])
            b, conf2 = get_actions_version1_play(vector2, hand2, gst)
            gst.update_state(b[2], gst.player_order[1])
            c, conf3 = get_actions_version1_play(vector3, hand3, gst)
            gst.update_state(c[2], gst.player_order[2])
            gst.clear_state()"""

        #test version2
        """while p1:
            hand1 = gst.player_hands[gst.player_order[0]]
            hand2 = gst.player_hands[gst.player_order[1]]
            hand3 = gst.player_hands[gst.player_order[2]]

            vector1 = [random.uniform(0, 1) for x in range(len(ACTIONS_VERSION2))]
            vector2 = [random.uniform(0, 1) for x in range(len(ACTIONS_VERSION2))]
            vector3 = [random.uniform(0, 1) for x in range(len(ACTIONS_VERSION2))]

            a, conf1 = get_actions_version2(vector1, hand1, gst)
            gst.update_state(a[2], gst.player_order[0])
            b, conf2 = get_actions_version2(vector2, hand2, gst)
            gst.update_state(b[2], gst.player_order[1])
            c, conf3 = get_actions_version2(vector3, hand3, gst)
            gst.update_state(c[2], gst.player_order[2])
            gst.clear_state()"""

        # test version3
        while p1:
            hand1 = gst.player_hands[gst.player_order[0]]
            hand2 = gst.player_hands[gst.player_order[1]]
            hand3 = gst.player_hands[gst.player_order[2]]

            vector1 = [random.uniform(0, 1) for x in range(len(ACTIONS_VERSION3_OPEN))]
            vector2 = [random.uniform(0, 1) for x in range(len(ACTIONS_VERSION3_PLAY))]
            vector3 = [random.uniform(0, 1) for x in range(len(ACTIONS_VERSION3_PLAY))]

            a, conf1 = get_actions_version3_open(vector1, hand1, gst)
            gst.update_state(a[2], gst.player_order[0])
            b, conf2 = get_actions_version3_play(vector2, hand2, gst)
            gst.update_state(b[2], gst.player_order[1])
            c, conf3 = get_actions_version3_play(vector3, hand3, gst)
            gst.update_state(c[2], gst.player_order[2])
            gst.clear_state()

        cnt += 1




