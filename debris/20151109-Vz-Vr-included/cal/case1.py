import numpy as np
import setup as s

dt = 0.01
imax = 20000000
u_t = np.zeros((imax, ))
u_r = np.zeros((imax, ))
u_z = np.zeros((imax, ))
theta = np.zeros((imax, ))
r = np.zeros((imax, ))
z = np.zeros((imax, ))
r[0] = s.r0
theta[0] = s.theta0
z[0] = s.z0

for i in range(imax):
    V_t = s.V_t(r[i])
    V_r = s.V_r(r[i])
    V_z = s.V_z(r[i])
    VR = np.sqrt((V_t-u_t[i])**2 + (V_r-u_r[i])**2 + (V_z-u_z[i])**2)
    a_t = s.k * (V_t - u_t[i]) * VR
    a_r = s.k * (V_r - u_r[i]) * VR
    a_z = s.k * (V_z - u_z[i]) * VR - s.g
    u_t[i+1] = u_t[i] + a_t * dt
    u_r[i+1] = u_z[i] + a_r * dt
    u_z[i+1] = u_z[i] + a_z * dt
    theta[i+1] = theta[i] + u_t[i] * dt / r[i] + \
        a_t * dt**2 / (2 * r[i])
    r[i+1] = r[i] + u_r[i] * dt + a_r * dt**2 / 2
    z[i+1] = z[i] + u_z[i] * dt + a_z * dt**2 / 2
    if z[i+1] < 0:
        imax = i
        t_g = dt * i
        break

time = np.arange(0, t_g + dt, dt)
u_t = u_t[:imax+1]
u_r = u_r[:imax+1]
u_z = u_z[:imax+1]
theta = theta[:imax+1]/np.pi*180
r = r[:imax+1]
z = z[:imax+1]
print(u_r)