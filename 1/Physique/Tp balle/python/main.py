
import math
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
y0 = 0.26

measure = [["angle [°]", 30, 45, 60],
           ["crans 1 [cm]", 109.5, 112, 88],
           ["crans 2 [cm]", 227.5, 251, 215],
           ["crans 3 [cm]", 425, 454, 383]]
measure_si = [["angle [rad]", 0, 0, 0],
              ["crans 1 [m]", 0, 0, 0],
              ["crans 2 [m]", 0, 0, 0],
              ["crans 3 [m]", 0, 0, 0]]

v0 = [["v0 1 [m/s]", 0, 0, 0, 0],
      ["v0 2 [m/s]", 0, 0, 0, 0],
      ["v0 3 [m/s]", 0, 0, 0, 0]]
tf = [["tf 1 [s]", 0, 0, 0],
      ["tf 2 [s]", 0, 0, 0],
      ["tf 3 [s]", 0, 0, 0]]
fleche = [["f 1 [m]", 0, 0, 0],
          ["f 2 [m]", 0, 0, 0],
          ["f 3 [m]", 0, 0, 0]]


def calc_si():
    for i in range(3):
        measure_si[0][i+1] = measure[0][i+1] * np.pi / 180
    for i in range(3):
        for j in range(3):
            measure_si[j+1][i+1] = measure[j+1][i+1] / 100

    print(measure_si)


def calc_v0():
    for i in range(3):
        for j in range(3):
            v0[i][j+1] = math.sqrt(g * measure_si[i+1][j+1]**2 / (2 * math.cos(measure_si[0][j+1])**2 * (y0 + measure_si[i+1][j+1] * math.tan(measure_si[0][j+1]))))
    for i in range(3):
        v0[i][4] = (v0[i][1] + v0[i][2] + v0[i][3]) / 3

    print(v0)


def calc_tf():
    for i in range(3):
        for j in range(3):
            tf[i][j+1] = measure_si[i+1][j+1] / (v0[i][j+1] * math.cos(measure_si[0][j+1]))

    print(tf)


def calc_fleche():
    for i in range(3):
        for j in range(3):
            fleche[i][j+1] = y0 + (v0[i][j+1] * math.sin(measure_si[0][j+1]))**2 / (2 * g)
            
    print(fleche)


def text_data():
    with open("data.txt", "w+") as file:
        for i in range(4):
            for j in range(4):
                if isinstance(measure[i][j], str):
                    file.write("[ " + measure[i][j] + " ]")
                else:
                    file.write("[ {:01.1f} ]".format(measure[i][j]))
            file.write("\n")
        file.write("\n")

        for i in range(4):
            for j in range(4):
                if isinstance(measure_si[i][j], str):
                    file.write("[ " + measure_si[i][j] + " ]")
                else:
                    file.write("[ {:01.2f} ]".format(measure_si[i][j]))
            file.write("\n")
        file.write("\n")

        for i in range(3):
            for j in range(4):
                if isinstance(v0[i][j], str):
                    file.write("[ " + v0[i][j] + " ]")
                else:
                    file.write("[ {:01.2f} ]".format(v0[i][j]))
            file.write("\n")
        file.write("\n")

        for i in range(3):
            for j in range(4):
                if isinstance(fleche[i][j], str):
                    file.write("[ " + fleche[i][j] + " ]")
                else:
                    file.write("[ {:01.2f} ]".format(fleche[i][j]))
            file.write("\n")
        file.write("\n")

        for i in range(3):
            for j in range(4):
                if isinstance(tf[i][j], str):
                    file.write("[ " + tf[i][j] + " ]")
                else:
                    file.write("[ {:01.2f} ]".format(tf[i][j]))
            file.write("\n")


def latex_table(list_table, name):
    init_table = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    with open("table_{}.txt".format(name), "w+") as file:
        for i in range(len(list_table)):
            for j in range(len(list_table[i])-1):
                init_table[i][j] = list_table[i][j+1]
                
        for i in range(len(init_table[0])):
            for j in range(len(init_table)):
                if init_table[j][i] != 0:
                    file.write("{:01.2f} ".format(init_table[j][i]))
                    if init_table[j+1][i] != 0:
                        file.write("& ")
            file.write(" \\\\ \hline \n")


def graph():
    t = np.linspace(0, 3, 500)

    ax1 = v0[0][1]*math.cos(measure_si[0][1])*t
    ay1 = y0 + v0[0][1]*math.sin(measure_si[0][1])*t - 1/2 * g * (t**2)
    ax2 = v0[0][2]*math.cos(measure_si[0][2])*t
    ay2 = y0 + v0[0][2]*math.sin(measure_si[0][2])*t - 1/2 * g * (t**2)
    ax3 = v0[0][3]*math.cos(measure_si[0][3])*t
    ay3 = y0 + v0[0][3]*math.sin(measure_si[0][3])*t - 1/2 * g * (t**2)

    bx1 = v0[1][1]*math.cos(measure_si[0][1])*t
    by1 = y0 + v0[1][1]*math.sin(measure_si[0][1])*t - 1/2 * g * (t**2)
    bx2 = v0[1][2]*math.cos(measure_si[0][2])*t
    by2 = y0 + v0[1][2]*math.sin(measure_si[0][2])*t - 1/2 * g * (t**2)
    bx3 = v0[1][3]*math.cos(measure_si[0][3])*t
    by3 = y0 + v0[1][3]*math.sin(measure_si[0][3])*t - 1/2 * g * (t**2)

    cx1 = v0[2][1]*math.cos(measure_si[0][1])*t
    cy1 = y0 + v0[2][1]*math.sin(measure_si[0][1])*t - 1/2 * g * (t**2)
    cx2 = v0[2][2]*math.cos(measure_si[0][2])*t
    cy2 = y0 + v0[2][2]*math.sin(measure_si[0][2])*t - 1/2 * g * (t**2)
    cx3 = v0[2][3]*math.cos(measure_si[0][3])*t
    cy3 = y0 + v0[2][3]*math.sin(measure_si[0][3])*t - 1/2 * g * (t**2)

    ax = plt.figure(1).subplots()
    ax.plot(ax1, ay1, label='30[°]')
    ax.plot(ax2, ay2, label='45[°]')
    ax.plot(ax3, ay3, label='60[°]')
    ax.set_title("Cran 1")
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(0, 1.15)
    plt.ylim(0, 0.6)
    ax.legend()

    plt.savefig("graph1.png")
    plt.show()

    bx = plt.figure(2).subplots()
    bx.plot(bx1, by1, label='30[°]')
    bx.plot(bx2, by2, label='45[°]')
    bx.plot(bx3, by3, label='60[°]')
    bx.set_title("Cran 2")
    bx.set_xlabel("x [m]")
    bx.set_ylabel("y [m]")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(0, 2.55)
    plt.ylim(0, 1.2)
    bx.legend()

    plt.savefig("graph2.png")
    plt.show()

    cx = plt.figure(3).subplots()
    cx.plot(cx1, cy1, label='30[°]')
    cx.plot(cx2, cy2, label='45[°]')
    cx.plot(cx3, cy3, label='60[°]')
    cx.set_title("Cran 3")
    cx.set_xlabel("x [m]")
    cx.set_ylabel("y [m]")

    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(0, 4.6)
    plt.ylim(0, 2)
    cx.legend()

    plt.savefig("graph3.png")
    plt.show()


if __name__ == '__main__':
    print("Start...")
    print(measure)

    calc_si()
    calc_v0()
    calc_tf()
    calc_fleche()

    text_data()
    
    latex_table(measure, "measure")
    latex_table(measure_si, "measure_si")
    latex_table(v0, "v0")
    latex_table(tf, "tf")
    latex_table(fleche, "fleche")

    graph()




    

