############################################################
# CASE 4: time step integral from analytical solution
############################################################
import numpy as np
import setup

dt = 0.01
imax = 2000
u_t = np.zeros((imax, ))
u_z = np.zeros((imax, ))
theta = np.zeros((imax, ))
z = np.zeros((imax, ))
z[0] = setup.z0

U = 38.3

for i in range(imax):
    a_t = setup.k * (U - u_t[i]) * np.sqrt((U - u_t[i])**2 + u_z[i]**2)
    a_z = setup.k * (-u_z[i]) * np.sqrt((U - u_t[i])**2 + u_z[i]**2) - setup.g
    u_t[i + 1] = u_t[i] + a_t * dt
    u_z[i + 1] = u_z[i] + a_z * dt
    theta[i + 1] = theta[i] + u_t[i] * dt / setup.r0 + \
        a_t * dt**2 / (2 * setup.r0)
    z[i + 1] = z[i] + u_z[i] * dt + a_z * dt**2 / 2
    if z[i + 1] < 0:
        imax = i
        t_g = dt * i
        break

time = np.arange(0, t_g + dt, dt)
u_t = u_t[:imax + 1]
u_z = u_z[:imax + 1]
