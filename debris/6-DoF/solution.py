import numpy as np
import setup as s


def T(Theta):
    A = np.array([[np.cos(Theta[1]) * np.cos(Theta[2]),
                   np.cos(Theta[1]) * np.sin(Theta[2]),
                   -np.sin(Theta[1])],
                  [np.sin(Theta[0]) * np.sin(Theta[1]) * np.cos(Theta[2]) -
                      np.cos(Theta[0]) * np.sin(Theta[2]),
                      np.sin(Theta[0]) * np.sin(Theta[1]) * np.sin(Theta[2]) +
                      np.cos(Theta[0]) * np.cos(Theta[2]),
                      np.sin(Theta[0]) * np.cos(Theta[1])],
                  [np.sin(Theta[0]) * np.sin(Theta[2]) +
                      np.cos(Theta[0]) * np.sin(Theta[1]) * np.cos(Theta[2]),
                      np.cos(Theta[0]) * np.sin(Theta[1]) * np.sin(Theta[2]) -
                      np.sin(Theta[0]) * np.cos(Theta[2]),
                      np.cos(Theta[0]) * np.cos(Theta[1])]])
    return A

dt = 0.01
ITER_MAX = 10000
X = np.zeros((3, ITER_MAX))
V = np.zeros((3, ITER_MAX))
Theta = np.zeros((3, ITER_MAX))
Omega = np.zeros((3, ITER_MAX))

# Initial condition
X[:, 0] = s.X0
V[:, 0] = s.V0
Theta[:, 0] = s.Theta0
Omega[:, 0] = s.Omega0


# Little time step method
Ug = np.zeros((3, ))
Up = np.zeros((3, ))
C_F = np.zeros((3, ))
C_EM = np.zeros((3, ))
C_DM = np.zeros((3, ))
A = np.zeros((3, ))
Alpha = np.zeros((3, ))
M_E = np.zeros((3, ))
M_D = np.zeros((3, ))
Lp = np.zeros((3, ))
J = np.array([[s.Ixx, 0, 0], [0, s.Iyy, 0], [0, 0, s.Izz]])

for i in np.arange(1, ITER_MAX):
    Ug = s.w(X[:, i - 1], (i - 1) * dt) - V[:, i - 1]
    Up = np.dot(T(Theta[:, i - 1]), Ug)
    Up_norm = np.linalg.norm(Up)
    epsilon = np.arcsin(Up[0] / Up_norm)
    gamma = np.arctan(Up[1] / (Up[2]+0.1))

    C_F = s.c_f(epsilon, gamma)
    C_EM = s.c_em(epsilon, gamma)
    C_DM = s.C_DM

    A = 1 / (2 * s.m) * s.rho_a * Up_norm**2 * np.array(
        [C_F[0] * s.Ly * s.Lz,
         C_F[1] * s.Lx * s.Lz,
         C_F[2] * s.Lx * s.Ly]) + s.g * np.array([0, -1, 0])
    M_E = 1 / 2 * s. rho_a * Up_norm**2 * np.array(
        [C_EM[0] * (s.Lz * s.Lx * s.Lz + s.Ly * s.Lx * s.Ly),
         C_EM[1] * (s.Lz * s.Ly * s.Lz + s.Lx * s.Lx * s.Ly),
         C_EM[1] * (s.Lx * s.Lx * s.Lz + s.Ly * s.Ly * s.Lz)])
    M_D = 1 / 2 * s.rho_a * np.array([
        (Up_norm + 1 / 2 * np.abs(Omega[0, i - 1])) *
        C_DM[0] * Omega[0, i - 1] * np.sqrt(s.Ly**2 + s.Lz**2) *
        (s.Ly * s.Lx * s.Ly + s.Lz * s.Lx * s.Lz),
        (Up_norm + 1 / 2 * np.abs(Omega[0, i - 1])) *
        C_DM[1] * Omega[1, i - 1] * np.sqrt(s.Lx**2 + s.Lz**2) *
        (s.Lx * s.Lx * s.Ly + s.Lz * s.Ly * s.Lz),
        C_DM[2] * Omega[2, i - 1] * np.sqrt(s.Lx**2 + s.Ly**2) *
        (s.Lx * s.Lx * s.Lz + s.Ly * s.Ly * s.Lz)])
    Lp = np.dot(J, Omega[:, i - 1])
    Alpha = M_E + M_D - np.array([
        Omega[1, i - 1] * Lp[2] - Omega[2, i - 1] * Lp[1],
        -Omega[0, i - 1] * Lp[2] + Omega[2, i - 1] * Lp[0],
        Omega[0, i - 1] * Lp[1] - Omega[1, i - 1] * Lp[0]])

    V[:, i] = V[:, i - 1] + A * dt
    Omega[:, i] = Omega[:, i - 1] + np.linalg.inv(J).dot(Alpha) * dt
    X[:, i] = X[:, i - 1] + (V[:, i - 1] + V[:, i]) / 2 * dt
    Theta[:, i] = Theta[:, i - 1] + np.linalg.inv(
        np.array([[1, np.sin(Theta[2, i - 1]), 0],
                  [0, np.cos(Theta[0, i - 1]) * np.cos(Theta[2, i - 1]),
                   np.sin(Theta[0, i - 1])],
                  [0, -np.sin(Theta[0, i - 1]) * np.cos(Theta[2, i - 1]),
                   np.cos(Theta[0, i - 1])]])).dot(Omega[:, i - 1]) * dt

print(X[1, :])
