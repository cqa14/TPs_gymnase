
import math

import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

VnT = [[0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12],
       [74, 75, 75.5, 75.5, 76, 76, 76.5, 76.5, 76.5, 76.5, 77.5, 80, 82, 90, 92, 93, 93.5, 94, 95, 96, 96, 97, 97, 97]]

if __name__ == '__main__':
    print("Start...")

    with open("VnT.txt", "w+") as file:
        for i in range(len(VnT[0])):
            if i in [0, 2, 4, 6, 8, 9, 11, 13, 15, 17, 18, 20, 22]:
                file.write("\\rowcolor{lightgray}")

            file.write("{:01.1f} & {:01.1f} \\\\  \n".format(VnT[0][i], VnT[1][i]))


    z = np.polyfit(VnT[0], VnT[1], 8)
    t = np.linspace(-0.5, 12.5, 100)
    p = np.poly1d(z)
    ax = plt.figure(1).subplots()
    ax.plot(VnT[0], VnT[1], 'o', label='Mesures')
    ax.plot(t, p(t), label='Courbe de tendance')
    #ax.set_title("Variation de la température en fonction du volume du distillat")
    ax.set_xlabel("V [mL]")
    ax.set_ylabel("T [°C]")
    plt.xlim(0, 12)
    plt.ylim(72, 100)
    ax.legend()

    plt.savefig("graph.png")
    plt.show()
