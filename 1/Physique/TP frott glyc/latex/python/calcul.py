import numpy as np
from matplotlib import pyplot as plt


def calc_all():
    distance = 0.085
    diam_bille = [0.001, 0.0015, 0.002]
    ray_bille = []

    for bille in diam_bille:
        ray_bille.append(bille / 2)

    ti = [[4.07, 4.15, 4.11, 4.05, 4.18], [1.63, 1.83, 1.74, 1.88, 1.77], [1.15, 1.14, 1.17, 1.18, 1.14]]
    time = []
    for t in ti:
        time.append(np.mean(t))

    vit = []
    for i in range(3):
        vit.append(distance / time[i])

    g = 9.81
    rho_acier = 7850
    rho_glyc = 1260
    eta = []
    for i in range(3):
        eta.append((2 * g * ray_bille[i] ** 2 * (rho_acier - rho_glyc)) / (9 * vit[i]) * 1000)

    mean_eta = np.mean(eta)

    print(ray_bille)
    print(time)
    print(vit)
    print(eta)
    print(mean_eta)

    def simulation(vi, rayon):
        f_a = (g * (rho_acier - rho_glyc)) / rho_acier
        f_b = (9 * mean_eta / 1000) / (2 * rayon ** 2 * rho_acier)
        dt = 20000
        tf = 0.1
        tli = list(np.linspace(0, tf, dt))
        acc = []
        speed = [vi]

        for i in range(len(tli)):
            if i != 0:
                speed.append(speed[i - 1] + acc[i - 1] * tf / dt)
                acc.append(f_a - f_b * speed[i])
            else:
                acc.append(f_a - f_b * speed[i])

        return tli, speed

    #test = simulation(0, ray_bille[2])
    #plt.plot(test[0], test[1])
    #plt.xlim(0, test[0][len(test[0]) - 1])
    #plt.ylim(0, test[1][len(test[1]) - 1] + 0.005)
    #plt.savefig('test.pdf')

    def sim_th(vi, rayon):
        f_a = (g * (rho_acier - rho_glyc)) / rho_acier
        f_b = (9 * mean_eta / 1000) / (2 * rayon ** 2 * rho_acier)
        dt = 20000
        tf = 0.1
        tli = list(np.linspace(0, tf, dt))
        vitt = []
        c = vi - f_a / f_b
        for tel in tli:
            vitt.append(f_a / f_b + c * np.exp(-f_b * tel))

        return tli, vitt

    #test2 = sim_th(0, ray_bille[2])
    #plt.plot(test2[0], test2[1])
    #plt.xlim(0, test2[0][len(test2[0]) - 1])
    #plt.ylim(0, test2[1][len(test2[1]) - 1] + 0.005)
    #plt.savefig('test2.pdf')

    #sim def
    #ray1_it0 = simulation(0, ray_bille[0])
    #ray1_it01 = simulation(0.01, ray_bille[0])
    #ray1_it05 = simulation(0.03, ray_bille[0])
    #plt.plot(ray1_it0[0], ray1_it0[1], label='0 [m/s]')
    #plt.plot(ray1_it01[0], ray1_it01[1], label='0.01 [m/s]')
    #plt.plot(ray1_it05[0], ray1_it05[1], label='0.05 [m/s]')
    #plt.xlim(0, 0.02)
    #plt.ylim(0, 0.035)
    #plt.xlabel('Temps [s]')
    #plt.ylabel('Vitesse [m/s]')
    #plt.legend()
    #plt.savefig('ray1_it.pdf')

    #ray2_it0 = simulation(0, ray_bille[1])
    #ray2_it01 = simulation(0.02, ray_bille[1])
    #ray2_it05 = simulation(0.07, ray_bille[1])
    #plt.plot(ray2_it0[0], ray2_it0[1], label='0 [m/s]')
    #plt.plot(ray2_it01[0], ray2_it01[1], label='0.02 [m/s]')
    #plt.plot(ray2_it05[0], ray2_it05[1], label='0.07 [m/s]')
    #plt.xlim(0, 0.04)
    #plt.ylim(0, 0.08)
    #plt.xlabel('Temps [s]')
    #plt.ylabel('Vitesse [m/s]')
    #plt.legend()
    #plt.savefig('ray2_it.pdf')

    #ray3_it0 = simulation(0, ray_bille[2])
    #ray3_it01 = simulation(0.04, ray_bille[2])
    #ray3_it05 = simulation(0.15, ray_bille[2])
    #plt.plot(ray3_it0[0], ray3_it0[1], label='0 [m/s]')
    #plt.plot(ray3_it01[0], ray3_it01[1], label='0.04 [m/s]')
    #plt.plot(ray3_it05[0], ray3_it05[1], label='0.15 [m/s]')
    #plt.xlim(0, 0.06)
    #plt.ylim(0, 0.15)
    #plt.xlabel('Temps [s]')
    #plt.ylabel('Vitesse [m/s]')
    #plt.legend()
    #plt.savefig('ray3_it.pdf')

    #ray3_th0 = sim_th(0, ray_bille[2])
    #ray3_th01 = sim_th(0.04, ray_bille[2])
    #ray3_th05 = sim_th(0.15, ray_bille[2])
    #plt.plot(ray3_th0[0], ray3_th0[1], label='0 [m/s]')
    #plt.plot(ray3_th01[0], ray3_th01[1], label='0.04 [m/s]')
    #plt.plot(ray3_th05[0], ray3_th05[1], label='0.15 [m/s]')
    #plt.xlim(0, 0.06)
    #plt.ylim(0, 0.15)
    #plt.xlabel('Temps [s]')
    #plt.ylabel('Vitesse [m/s]')
    #plt.legend()
    #plt.savefig('ray3_th.pdf')
    
    def density(rayon):
        f_a = (g * (rho_acier - rho_glyc)) / rho_acier
        f_b = (9 * mean_eta / 1000) / (2 * rayon ** 2 * rho_acier)
        dt = 20000
        tf = 0.1
        tli = list(np.linspace(0, tf, dt))
        vitt = []
        tfin = []
        for vi in np.linspace(0, 0.15, 1000):
            c = vi - f_a / f_b
            tfin = tfin + tli
            for tel in tli:
                vitt.append(f_a / f_b + c * np.exp(-f_b * tel))

        return tfin, vitt
    
    densplot = density(ray_bille[2])
    plt.hist2d(densplot[0], densplot[1], bins=100)
    plt.xlabel('Temps [s]')
    plt.ylabel('Vitesse [m/s]')
    plt.savefig('densplot.pdf')
    print('finish...')


if __name__ == "__main__":
    calc_all()
