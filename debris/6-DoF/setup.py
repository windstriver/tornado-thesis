import numpy as np


# Wind field
def w(x, t):
    W = np.array([30, 0, 0])
    return W


# Air property
rho_a = 1.225
g = 9.8

# Debris property
Lx = 0.1
Ly = 1.06
Lz = 2.12
m = 0.809
Ixx = m * (Ly**2 + Lz**2) / 12
Iyy = m * (Lz**2 + Lx**2) / 12
Izz = m * (Lx**2 + Ly**2) / 12

# Initial condition
V0 = np.zeros((3, ))
X0 = np.zeros((3, ))
Theta0 = np.array([np.pi / 6, np.pi / 9, np.pi / 6])
Omega0 = np.zeros((3, ))


# Normal coefficient for plate
def c_n(epsilon, gamma):
    AR = (Lz * np.abs(np.cos(gamma)) + Ly * np.abs(np.sin(gamma)))**2 / \
        (Ly * Lz)
    return 2 * np.pi * epsilon / (1 + 2 / AR)


# Force coefficient for plate
def c_f(epsilon, gamma):
    return np.array([c_n(epsilon, gamma), 0, 0])


# Pressure center location
def cop(epsilon, gamma):
    CoP = np.zeros((2, ))
    c = (Ly * Lz) / (Ly * np.abs(np.sin(gamma)) +
                     Lz * np.abs(np.cos(gamma)))
    sin_xi = np.sin(gamma) / (Lz / Ly)
    cos_xi = np.cos(gamma) / (Lz / Ly)
    CoP[0] = c / 4 * (np.pi / 2 - np.abs(epsilon)) / (np.pi / 2) * sin_xi
    CoP[1] = c / 4 * (np.pi / 2 - np.abs(epsilon)) / (np.pi / 2) * cos_xi
    return CoP


# Momentrum coefficient for plate
def c_em(epsilon, gamma):
    C_N = c_n(epsilon, gamma)
    CoP = cop(epsilon, gamma)
    return np.array([0, 1 / 2 * CoP[1] / Lx * C_N, -1 / 2 * CoP[0] / Lx * C_N])


# Damping moments coefficient
C_DM = np.array([-0.05, -0.185, -0.185])

print(c_f(np.pi/3, np.pi/6))