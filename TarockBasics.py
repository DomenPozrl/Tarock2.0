import copy
import random

class TarockBasics:

    #CLUB JE KRIZ
    def __init__(self):

        #4: "1\u2665",
        self.id_to_cards = {
            #herci
            4: "1\u2665",
            3: "2\u2665",
            2: "3\u2665",
            1: "4\u2665",
            5: "B\u2665",
            6: "C\u2665",
            7: "Q\u2665",
            8: "K\u2665",

            #kare
            14: "1\u2666",
            13: "2\u2666",
            12: "3\u2666",
            11: "4\u2666",
            15: "B\u2666",
            16: "C\u2666",
            17: "Q\u2666",
            18: "K\u2666",

            #piki
            21: "7\u2660",
            22: "8\u2660",
            23: "9\u2660",
            24: "10\u2660",
            25: "B\u2660",
            26: "C\u2660",
            27: "Q\u2660",
            28: "K\u2660",

            #krizi
            31: "7\u2663",
            32: "8\u2663",
            33: "9\u2663",
            34: "10\u2663",
            35: "B\u2663",
            36: "C\u2663",
            37: "Q\u2663",
            38: "K\u2663",

            #taroki
            40: "I",
            41: "II",
            42: "III",
            43: "IV",
            44: "V",
            45: "VI",
            46: "VII",
            47: "VIII",
            48: "IX",
            49: "X",
            50: "XI",
            51: "XII",
            52: "XIII",
            53: "XIV",
            54: "XV",
            55: "XVI",
            56: "XVII",
            57: "XVIII",
            58: "XIX",
            59: "XX",
            60: "XXI",
            61: "ŠKIS",
        }

        #8: 5,
        self.id_to_points = {
            4: 0,
            3: 0,
            2: 0,
            1: 0,
            5: 2,
            6: 3,
            7: 4,
            8: 5,
            14: 0,
            13: 0,
            12: 0,
            11: 0,
            15: 2,
            16: 3,
            17: 4,
            18: 5,
            21: 0,
            22: 0,
            23: 0,
            24: 0,
            25: 2,
            26: 3,
            27: 4,
            28: 5,
            31: 0,
            32: 0,
            33: 0,
            34: 0,
            35: 2,
            36: 3,
            37: 4,
            38: 5,
            40: 5,
            41: 0,
            42: 0,
            43: 0,
            44: 0,
            45: 0,
            46: 0,
            47: 0,
            48: 0,
            49: 0,
            50: 0,
            51: 0,
            52: 0,
            53: 0,
            54: 0,
            55: 0,
            56: 0,
            57: 0,
            58: 0,
            59: 0,
            60: 5,
            61: 5,
        }

        #"1\u2665": 4,
        self.cards_to_id = {
            "1\u2665": 4,
            "2\u2665": 3,
            "3\u2665": 2,
            "4\u2665": 1,
            "B\u2665": 5,
            "C\u2665": 6,
            "Q\u2665": 7,
            "K\u2665": 8,
            "1\u2666": 14,
            "2\u2666": 13,
            "3\u2666": 12,
            "4\u2666": 11,
            "B\u2666": 15,
            "C\u2666": 16,
            "Q\u2666": 17,
            "K\u2666": 18,
            "7\u2660": 21,
            "8\u2660":22,
            "9\u2660": 23,
            "10\u2660": 24,
            "B\u2660": 25,
            "C\u2660": 26,
            "Q\u2660": 27,
            "K\u2660": 28,
            "7\u2663": 31,
            "8\u2663": 32,
            "9\u2663": 33,
            "10\u2663": 34,
            "B\u2663": 35,
            "C\u2663": 36,
            "Q\u2663": 37,
            "K\u2663": 38,
            "I": 40,
            "II": 41,
            "III": 42,
            "IV": 43,
            "V": 44,
            "VI": 45,
            "VII": 46,
            "VIII": 47,
            "IX": 48,
            "X": 49,
            "XI": 50,
            "XII": 51,
            "XIII": 52,
            "XIV": 53,
            "XV": 54,
            "XVI": 55,
            "XVII": 56,
            "XVIII": 57,
            "XIX": 58,
            "XX": 59,
            "XXI":60,
            "ŠKIS":61,
        }

        self.kings = [8, 18, 28, 38]
        self.queens = [7, 17, 27, 37]
        self.cavals = [6, 16, 26, 36]
        self.jacks = [5, 15, 25, 35]
        self.platelci = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34]
        self.herc_platelci = [1,2,3,4]
        self.karo_platelci = [11,12,13,14]
        self.pik_platelci = [21, 22, 23, 24]
        self.kriz_platelci = [31,32,33,34]

        self.tarocks = list(range(40, 62))

    def isHeart(self, karta_id):
        return karta_id >= 1 and karta_id <= 8


    def isDiamond(self, karta_id):
        return karta_id >= 11 and karta_id <= 18


    def isSpade(self, karta_id):
        return karta_id >= 21 and karta_id <= 28

    def isClub(self, karta_id):
        return karta_id >= 31 and karta_id <= 38


    def isTarock(self, karta_id):
        return karta_id >= 40 and karta_id <= 61


    def is_same_color(self, karta1, karta2):
        return (self.isHeart(karta1) and self.isHeart(karta2)) or (
                    self.isSpade(karta1) and self.isSpade(karta2)) or (
                           self.isClub(karta1) and self.isClub(karta2)) or (
                           self.isDiamond(karta1) and self.isDiamond(karta2)) or (
                           self.isTarock(karta1) and self.isTarock(karta2))

    def deal_cards(self):

        #copy the keys of all the cards and so represent the entire deck
        cards = copy.deepcopy(list(self.id_to_cards.keys()))

        #shuffle the deck
        random.shuffle(cards)


        #dealt cards
        dealt_cards = []

        for i in range(0, len(cards), 16):
            dealt_cards.append(list(sorted(cards[i:i + 16])))


        return dealt_cards

    def print_dealt_cards(self, dealt_cards):

        for i in range(len(dealt_cards)):
            if i < 3:
                print("Hand #" + str(i + 1) + ":")
            else:
                print("Talon:")
            for card in dealt_cards[i]:
                print("    " + self.id_to_cards[card])

    def print_hand(self, hand):
        s = "| "
        for card in hand:
            s += self.id_to_cards[card] + " (" + str(card) + ")" + " |"
        print(s)
