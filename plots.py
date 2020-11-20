random_1_1_player = [26.2106, 31.50824587706147, 34.88135593220339]
random_1_1_random1 = [17.8118, 15.02848575712144, 13.288135593220339]
random_1_1_random2 = [18.2304, 16.08545727136432, 13.830508474576272]

lw_1_1_player = [27.1478, 32.04938271604938, 35.431372549019606]
lw_1_1_lw1 = [17.5908, 15.25925925925926, 13.843137254901961]
lw_1_1_lw2 = [17.473, 15.234567901234568, 13.470588235294118]

lb_1_1_player = [29.3991, 35.74013157894737, 39.19047619047619]
lb_1_1_lb1 = [16.0743, 13.381578947368421, 10.595238095238095]
lb_1_1_lb2 = [16.7724, 13.358552631578947, 12.761904761904763]

lbb_3_3_player = [15.5515, 17.74457429048414, 22.4]
lbb_3_3_lbb1 = [25.3189, 23.888146911519197, 20.42222222222222]
lbb_3_3_lbb2 = [21.3836, 20.89482470784641, 19.57777777777778]
# libraries
import numpy as np
import matplotlib.pyplot as plt

def plot_points_with_quality(x, y, z, labels, legend, title):
    # set width of bar
    barWidth = 0.25

    # Set position of bar on X axis
    r1 = np.arange(len(x))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    plt.bar(r1, x, color='#ec4724', width=barWidth, edgecolor='white', label=legend[0])
    plt.bar(r2, y, color='#3461a4', width=barWidth, edgecolor='white', label=legend[1])
    plt.bar(r3, z, color='#4c6fa4', width=barWidth, edgecolor='white', label=legend[2])

    # Add xticks on the middle of the group bars
    plt.xticks([r + barWidth for r in range(len(x))], labels)

    plt.title(title)
    # Create legend & Show graphic
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_points_with_quality(random_1_1_player, random_1_1_random1, random_1_1_random2, ["All cards", "Good cards", "Very good cards"], ["Q-learning Agent", "Random agent", "Random agent"], "Playing vs random agent")
    plot_points_with_quality(lw_1_1_player, lw_1_1_lw1, lw_1_1_lw2,
                             ["All cards", "Good cards", "Very good cards"],
                             ["Q-learning Agent", "LW agent", "LW agent"], "Playing vs locally worst agent")
    plot_points_with_quality(lb_1_1_player, lb_1_1_lb1, lb_1_1_lb2,
                             ["All cards", "Good cards", "Very good cards"],
                             ["Q-learning Agent", "LB agent", "LB agent"], "Playing vs locally best agent")

    plot_points_with_quality(lbb_3_3_player, lbb_3_3_lbb1, lbb_3_3_lbb2, ["All cards", "Good cards", "Very good cards"], ["Q-learning Agent", "LBB agent", "LBB agent"], "Playing vs LBB agent")