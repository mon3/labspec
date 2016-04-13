import math
import numpy as np
import anim

m = 1.
e = 1.
omega_x = 1.
omega_y = 0.3
omega_z = 0.5
N_x = 50 #128
N_y = 50 #128
N_z = 50 #128
L = np.min([N_x/2, N_y/2, N_z/2])
N_0 = 1000
dx = 1
dy = 1
dz = 1
ksi = 0.5
alfa = 1./N_0
epsilon = 0.00001
A = 2.871


def external_potential(x, y, z, m1, omegax, omegay, omegaz, Nx, Ny, Nz):
    return ( (m1*omegax**2 * (x - Nx/2)**2)/2 + (m1*omegay**2 * (y - Ny/2)**2)/2 + (m1*omegaz**2 * (z - Nz/2)**2)/2)


def p_m(m_x, n_x1, delta_x1):
    if (m_x <= (n_x1/2)):
        return (2*np.pi*m_x)/(n_x1*delta_x1)
    else:
        return (2*np.pi*(m_x-n_x1))/(n_x1*delta_x1)


def integral_rho(rho):
    rho_reshaped = np.array(rho).reshape((N_x, N_y, N_z))
    FT_rho = np.fft.fftn(rho_reshaped)

    F_freq = np.fft.fftfreq(N_x)
    for k_x in range(N_x):
        for k_y in range(N_y):
            for k_z in range(N_z):
                if k_x==0 and k_y==0 and k_z==0:
                    FT_rho[k_x][k_y][k_z] *= 2*np.pi*L**2
                else:
                    k = math.sqrt(p_m(k_x, N_x, dx)**2 + p_m(k_y, N_y, dy)**2 + p_m(k_z, N_z, dz)**2)
                    FT_rho[k_x][k_y][k_z] *= ((4*np.pi)/(k**2)) * (1 - math.cos(k*L))

    return np.fft.ifftn(FT_rho)


def density_f(density, mi1, beta):
    counter = 0
    mi0 = 0.

    while(abs(mi1-mi0) > epsilon):
        density0 = density
        mi0 = mi1
        N = 0.
        integral = integral_rho(density0).real
        #anim.make_anim(integral, N_x, N_y, N_z)
        for i1 in range(N_x):
            for j1 in range(N_y):
                for k1 in range(N_z):
                    F = 3./(5.*A) * (mi1 - external_potential(i1, j1, k1, m, omega_x, omega_y, omega_z, N_x, N_y, N_z) - beta*integral[i1][j1][k1])

                    if F>0:
                        density[k1+N_z*j1+N_y*N_z*i1] = math.sqrt(F**3)
                    else:
                        density[k1+N_z*j1+N_y*N_z*i1] = 0
                    N += density[k1+N_z*j1+N_y*N_z*i1]


#zmodyfikowac tak,zeby zapisywalo tylko niezerowe density i odpowiednie dla niego wspolrzedne

        mi1 = mi0 - alfa*(N - N_0)
        mi1 = ksi*mi1 + (1-ksi)*mi0

        counter += 1
        print counter, N

    print N
    print mi1

    mat =np.array(density)
    np.save('data.npy', mat)
    print mat.shape
    return [density, mi1]


def main():
    density = [1.] * (N_x*N_y*N_z)
    mi1 = 7.66
    #density_f(density, mi1, 0)
    betas = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    for beta in betas:
        densityA, mi1A = density_f(density, mi1, beta)
        density = densityA
        mi1 = mi1A
        anim.make_anim(density, N_x, N_y, N_z)
    print "********* MI *********"
    print mi1





if __name__ == "__main__":
    main()