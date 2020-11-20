from TarockBasics import *

def parse_file(filename):
    file = open(filename, "r")
    lines = file.readlines()

    sep = "--------------------------"

    data = []
    for i in range(0, len(lines), 6):
        line = lines[i]
        my_cards = lines[i+1]
        player2_cards = lines[i+2]
        player3_cards = lines[i+3]
        talon = lines[i+4]
        points = lines[i + 5]

        data.append((eval(my_cards), eval(player2_cards), eval(player3_cards), eval(talon), eval(points)))

    return data

def quality_of_cards(hand):
    #16 kart
    #8 tarokov
    #2 kralja
    #škrt ene barve
    tb = TarockBasics()
    tarocks = [tb.isTarock(x) for x in hand].count(True)
    kings = [x in [8, 18, 28, 38] for x in hand].count(True)

    heart = any([tb.isHeart(x) for x in hand])
    diamond = any([tb.isDiamond(x) for x in hand])
    spade = any([tb.isSpade(x) for x in hand])
    club = any([tb.isClub(x) for x in hand])

    skrt = 0
    if heart:
        skrt += 1
    if diamond:
        skrt += 1
    if spade:
        skrt += 1
    if club:
        skrt += 1

    return tarocks, kings, skrt

def semi_cards(hand):
    tarocks, kings, skrt = quality_of_cards(hand)
    return tarocks >= 8 and kings >= 2 and skrt >= 1

def good_cards(hand):
    tarocks, kings, skrt = quality_of_cards(hand)
    return tarocks >= 10 and kings >= 2 and skrt > 1

def godlike_cards(hand):
    tarocks, kings, skrt = quality_of_cards(hand)
    return tarocks >= 12 and kings >= 3 and skrt >= 2

if __name__ == "__main__":
    data_1_1_random = parse_file("1_1_random_random")
    data_1_1_LW = parse_file("1_1_LW_LW")
    data_1_1_LB = parse_file("1_1_LB_LB")

    data_2_2_random = parse_file("2_2_random_random")
    data_2_2_LW = parse_file("2_2_LW_LW")
    data_2_2_LB = parse_file("2_2_LB_LB")

    data_3_3_random = parse_file("3_3_random_random")
    data_3_3_LW = parse_file("3_3_LW_LW")
    data_3_3_LB = parse_file("3_3_LBB_LBB")

    tb = TarockBasics()

    #average points per strat, all together
    tocke = []

    tocke_semi = []
    tocke_good = []

    for game in data_1_1_random:
        my_cards = game[0]


        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]

        tocke.append(points)

        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)

    print("---------------------------------------------")
    print("1_1_RANDOM")
    print(sum([x[1] for x in tocke])/len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))
    print("---------------------------------------------")
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_1_1_LW:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("1_1_LW")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))
    print("---------------------------------------------")
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_1_1_LB:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("1_1_LB")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))
    print("---------------------------------------------")

    print("***********************************************************************************")
    print("***********************************************************************************")

    ###############################################################################
    ###############################################################################
    ###############################################################################

    # average points per strat, all together
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_2_2_random:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("2_2_random")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))



    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_2_2_LW:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("2_2_LW")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_2_2_LB:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("2_2_LB")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))

    ###############################################################################
    ###############################################################################
    ###############################################################################

    print("***********************************************************************************")
    print("***********************************************************************************")
    # average points per strat, all together
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_3_3_random:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("3_3_random")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))

    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_3_3_LW:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("3_3_LW")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))
    
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_3_3_LB:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)

    print("---------------------------------------------")
    print("TA JE TAPRAVA")
    print("3_3_LBB")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))

    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    data_1_1_random = parse_file("1_1_random_random")
    data_1_1_LW = parse_file("1_1_duo_LW_LW")
    data_1_1_LB = parse_file("1_1_duo_LB_LB")

    data_2_2_random = parse_file("2_2_duo_random_random")
    data_2_2_LW = parse_file("2_2_duo_LW_LW")
    data_2_2_LB = parse_file("2_2_duo_LB_LB")

    data_3_3_random = parse_file("3_3_duo_random_random")
    data_3_3_LW = parse_file("3_3_duo_LW_LW")
    data_3_3_LB = parse_file("3_3_duo_LB_LB")

    tb = TarockBasics()

    # average points per strat, all together
    tocke = []

    tocke_semi = []
    tocke_good = []

    for game in data_1_1_random:
        my_cards = game[0]

        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]

        tocke.append(points)

        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)

    print("---------------------------------------------")
    print("1_1_RANDOM")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))
    print("---------------------------------------------")
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_1_1_LW:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("1_1_LW")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))
    print("---------------------------------------------")
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_1_1_LB:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("1_1_LB")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))
    print("---------------------------------------------")

    print("***********************************************************************************")
    print("***********************************************************************************")

    ###############################################################################
    ###############################################################################
    ###############################################################################

    # average points per strat, all together
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_2_2_random:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("2_2_random")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))

    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_2_2_LW:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("2_2_LW")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_2_2_LB:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("2_2_LB")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))

    ###############################################################################
    ###############################################################################
    ###############################################################################

    print("***********************************************************************************")
    print("***********************************************************************************")
    # average points per strat, all together
    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_3_3_random:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("3_3_random")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))

    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_3_3_LW:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)
    print("---------------------------------------------")
    print("3_3_LW")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("---------------------------------------------")
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))

    tocke = []
    tocke_semi = []
    tocke_good = []
    for game in data_3_3_LB:
        my_cards = game[0]
        player2_cards = game[1]
        player3_cards = game[2]
        talon = game[3]
        points = game[4]
        tocke.append(points)
        if semi_cards(my_cards):
            tocke_semi.append(points)
        if good_cards(my_cards):
            tocke_good.append(points)

    print("---------------------------------------------")

    print("3_3_LB")
    print(sum([x[1] for x in tocke]) / len(tocke))
    print(sum([x[2] for x in tocke]) / len(tocke))
    print(sum([x[3] for x in tocke]) / len(tocke))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[2] for x in tocke_semi]) / len(tocke_semi))
    print(sum([x[3] for x in tocke_semi]) / len(tocke_semi))
    print("|||||||||||||||||||||||||||||||||||||||||||||")
    print(sum([x[1] for x in tocke_good]) / len(tocke_good))
    print(sum([x[2] for x in tocke_good]) / len(tocke_good))
    print(sum([x[3] for x in tocke_good]) / len(tocke_good))

