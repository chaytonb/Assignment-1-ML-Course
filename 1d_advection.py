import numpy as np

def main():
    N = 200 # Number of grid points (Eulerian grid)
    h = 1 / (N-1)  # periodic
    a = 1  # "wind speed"

    D = np.zeros((N, N))  # Difference operator in discrete space
    for i in range(N-1):
        D[i, i+1] = 1
        D[i+1, i] = -1
    D[-1, 0] = 1
    D[0, -1] = -1
    D /= 2*h

    x = np.linspace(0, 1, N)

    z = np.cos(x * 2*np.pi)  # Initial condition

    predicted = lambda z: D@(a*z)  # Single timestep

    dt = 1/(2*N)  # CFL condition??

    k1 = D
    k2 = D@(np.eye(N) + dt/2*k1)
    k3 = D@(np.eye(N) + dt/2*k2)
    k4 = D@(np.eye(N) + dt*k3)

    k = dt/6*(k1 + 2*k2 + 2*k3 + k4)

    T = int(50 / dt)

    zz = z.copy()
    for i in range(T):
        zz += k@(a*zz)

    print(D)

    import matplotlib.pyplot as plt
    
    plt.plot(x, z, label="$z_0$")
    plt.plot(x, zz, label="$z_t$")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()