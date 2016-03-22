import math

m = 1.
e = 1.
omega_x = 1.
omega_y = 1.
omega_z = 1.
N_x = 100
N_y = 100
N_z = 100
N_0 = 100000
dx = 1
dy = 1
dz = 1
ksi = 0.5
alfa = 0.0001
epsilon = 0.00001
A = 1.



def external_potential(x, y, z, m, omegax, omegay, omegaz, Nx, Ny, Nz):
    return ( (m*omegax**2 * (x - Nx/2)**2)/2 + (m*omegay**2 * (y - Ny/2)**2)/2 + (m*omegaz**2 * (z - Nz/2)**2)/2)


def main():
    mi0 = 50.
    density = [1] * (N_x*N_y*N_z)
    counter = 0
    N = 0
    mi1 = 55.

    while(abs(mi1-mi0) > epsilon):
        mi0 = mi1
        N = 0
        for i1 in range(N_x):
            for j1 in range(N_y):
                for k1 in range(N_z):
                    F = 3./(5.*A) * (mi1 - external_potential(i1, j1, k1, m, omega_x, omega_y, omega_z, N_x, N_y, N_z))
                    if F>0:
                        density[k1+N_z*j1+N_y*N_z*i1] = math.sqrt(F**3)
                    else:
                        density[k1+N_z*j1+N_y*N_z*i1] = 0
                    N += density[k1+N_z*j1+N_y*N_z*i1]
        
        mi1 = mi0 - alfa*(N - N_0)
        mi1 = ksi*mi1 + (1-ksi)*mi0

        counter += 1
        print counter, N

    print N
    print mi1


if __name__ == "__main__":
    main()