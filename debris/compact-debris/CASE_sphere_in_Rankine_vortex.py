# CASE study of a sphere in tornado wind field
# Assumptions:
#     tornado model: Rankine vortex model;
#     vertical veloctiy of the sphere dose not affect its drag;
#     drag coefficient of the sphere is constant 0.5.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas
from matplotlib.figure import Figure
# Rankine vortex model


def V_r(r, V_R, R):
    '''
    Rankine vortex model of tornado.
    Parameters:
        r:    the radius.
        V_R:  the maximum tangential velocity of the tornado.
        R:    the core radius of the tornado where the maximum
              tangential velocity occures.
    Return:
        tangential velocity at radius r.'''
    if r < R:
        return r / R * V_R
    else:
        return R / r * V_R

# Group A tornado parameters
V_R = 84.9     # maximum tangential velocity (m/s)
R = 45.7       # core radius (m)

# Sphere parameters
d = 8e-3       # diameter (m)
rho_m = 2.0e3  # density (kg/m^3)
l = 2 / 3 * d      # ratio of the volume to the surface area

# Air property
rho_a = 1.225  # density (kg/m^3)
# mu = 1.8e-5    # viscosity (kg/(m-s))
g = 9.8        # gravity (m/s^2)

# Drag coefficient
C_D = 0.5

k = rho_a * C_D / (2 * rho_m * l)

# Initial condition
r0 = R
z0 = 10        # hegith (m)
theta0 = 0


def u_t(t):
    '''
    Calculate the tangential veloctiy of the sphere.
    '''
    U = V_r(r0, V_R, R)
    return (k * U * U * t) / (1 + k * U * t)


def u_z(t):
    '''
    Calculate the vertical veloctiy of the sphere.
    '''
    return -g * t


def theta(t):
    '''
    Calculate the theta of the sphere.
    '''
    U = V_r(r0, V_R, R)
    return theta0 + U / r0 * (t - 1 / (k * U)) * np.log(1 + k * U * t)


def z(t):
    '''
    Calculate the z of the sphere.
    '''
    return z0 - 1 / 2 * g * t * t

# Effect of vertical air resistence
dt = 0.01
imax = 2000
u_t2 = np.zeros((imax, ))
u_z2 = np.zeros((imax, ))
theta2 = np.zeros((imax, ))
z2 = np.zeros((imax, ))
z2[0] = z0

U = V_r(r0, V_R, R)

for i in range(imax):
    a_t = k * (U - u_t2[i]) * np.sqrt((U - u_t2[i])**2 + u_z2[i]**2)
    a_z = k * (-u_z2[i]) * np.sqrt((U - u_t2[i])**2 + u_z2[i]**2) - g
    u_t2[i + 1] = u_t2[i] + a_t * dt
    u_z2[i + 1] = u_z2[i] + a_z * dt
    theta2[i + 1] = theta2[i] + u_t2[i] * dt / r0 + \
        a_t * dt**2 / (2 * r0)
    z2[i + 1] = z2[i] + u_z2[i] * dt + a_z * dt**2 / 2
    if z2[i + 1] < 0:
        imax = i
        t_g2 = dt * i
        break


# the property of the sphere when hit the ground (z=0 m)
t_g = np.sqrt(2 * z0 / g)
theta_g = theta(t_g)
x = r0 * np.cos(theta_g)
y = r0 * np.sin(theta_g)
u_t_g = u_t(t_g)
u_z_g = u_z(t_g)

time = np.linspace(0, t_g, num=100)
u_t_hist = u_t(time)
u_z_hist = u_z(time)
theta_hist = theta(time)
x_hist = r0 * np.cos(theta_hist)
y_hist = r0 * np.sin(theta_hist)
z_hist = z(time)

time2 = np.arange(0, t_g2 + dt, dt)
u_t2 = u_t2[:imax + 1]
u_z2 = u_z2[:imax + 1]

fig = Figure(tight_layout=True)
canvas = FigureCanvas(fig)
ax1 = fig.add_subplot(1, 2, 1)
line_no_uz, = ax1.plot(time, u_t_hist, label=r'Case 1')
line_uz, = ax1.plot(time2, u_t2, '--', label=r'Case 2')
ax1.set_xlabel(r'$t / \mathrm{s}$')
ax1.set_ylabel(r'$u_t (\mathrm{m/s})$')
ax1.legend(handles=[line_no_uz, line_uz], loc='upper left')

ax2 = fig.add_subplot(1, 2, 2)
line2_no_uz, = ax2.plot(time, u_z_hist, label=r'Case 1')
line2_uz, = ax2.plot(time2, u_z2, '--', label=r'Case 2')
ax2.set_xlabel(r'$t / \mathrm{s}$')
ax2.set_ylabel(r'$u_z (\mathrm{m/s})$')
ax2.legend(handles=[line2_no_uz, line2_uz])

fig.savefig('velocity_history.pdf')

print(t_g, t_g2)
print(u_t(t_g), u_t2[imax])
print(u_z(t_g), u_z2[imax])
