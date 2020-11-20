from MilestoneAgents import *
from TarockBasics import *
from GameStateTarock import *


if __name__ == "__main__":

    tb = TarockBasics()

    p1, p2, p3, talon = tb.deal_cards()

    ma = MilestoneAgents(p1, p2, p3, [1,2,3], 1, [2,3])


