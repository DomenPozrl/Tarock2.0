from GameStateTarock import *
import random

#okay so here is the deal
#there can be various levels of specificity when defining actions
#it can range from win current stack to win play a specific card
#i'm thinking we should define the least specific one (win current stack, pass current stack), the medium (win current stack hard, win current stack small, color, add on) and every specific card


#nevem pol je tuki takoj problem k sta odpret pa igrt efektivno cist razlicni potezi
#tko da rabs razlicne akcije
#jz bi za odpret definiru razlicne akcije pa za igrt razlicne akcije


#recimo za odpret bi mel kral, dama, caval, pob, platlc * 4 plus nizek, srednji, visok tarok


def play_king(hand):
    kralji = {8, 18, 28, 38}
    inter = list(kralji.intersection(set(hand)))
    if inter:
        return True, random.choce(inter)
    else:
        return False, None

def play_queen(hand):
    dame = {7, 17, 27, 37}
    inter = list(dame.intersection(set(hand)))
    if inter:
        return True, random.choce(inter)
    else:
        return False, None

def play_knight_jack(hand):
    knights_jacks = {6, 16, 26, 36, 5, 15, 25, 35}
    inter = list(knights_jacks.intersection(hand))
    if inter:
        return True, random.choce(inter)
    else:
        return False, None

def play_platlc(hand):
    platelci = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34]
    inter = list(platelci.intersection(hand))
    if inter:
        return True, random.choce(inter)
    else:
        return False, None

def play_tarock(hand):
    tarocks = list(range(40, 62))
    inter = list(tarocks.intersection(hand))
    if inter:
        return True, random.choce(inter)
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

    pari = reversed(sorted(list(zip(vector, conf, card, action_names))))

    for par in pari:
        if par[1]:
            return par, conf, action_names
        else:
            continue

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

    pari = reversed(sorted(list(zip(vector, conf, card, action_names))))

    for par in pari:
        if par[1]:
            return par, conf, action_names
        else:
            continue

def get_actions_version2(vector, hand, game_state: GameStateTarock):
    action_names = list(game_state.id_to_cards.keys())
    if len(game_state.stack) > 0:
        conf = [True if card in game_state.legal_moves(game_state.stack[0], hand) else False for card in action_names]
    else:
        conf = [True if card in hand else False for card in action_names]

    card = action_names

    pari = reversed(sorted(list(zip(vector, conf, card, action_names))))

    for par in pari:
        if par[1]:
            return par, conf, action_names
        else:
            continue

if __name__ == "__main__":
    tb = TarockBasics()

    p1, p2, p3, talon = tb.deal_cards()

    c = 0
    l = []
    while c < 100:
        gst = GameStateTarock(p1, p2, p3, [1,2,3], 1, [2,3])

        l.append(get_actions_version2(1, 2, gst))
        c += 1

    model = True
    for a, b in zip(l, l[1:]):
        if a != b:
            model = False
    print(model)








