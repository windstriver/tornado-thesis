# CASE study of a sphere in tornado wind field
# Assumptions:
#     tornado model: Rankine vortex model;
#     vertical veloctiy of the sphere dose not affect its drag;
#     drag coefficient of the sphere is constant 0.5.
import numpy as np
import matplotlib.pyplot as plt

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
    return z0 - 1 / 2 * g * t ^ 2

# the property of the sphere when hit the ground (z=0 m)
t_g = np.sqrt(2 * z0 / g)
theta_g = theta(t_g)
x = r0 * np.cos(theta_g)
y = r0 * np.sin(theta_g)
u_t_g = u_t(t_g)
u_z_g = u_z(t_g)

print(t_g)
print(x)
print(y)
print(u_t_g)
print(u_z_g)

time = np.linspace(0, t_g, num=100)
u_t_hist = u_t(time)
plt.plot(time, u_t_hist)
plt.title('Tangential velocity of the sphere')
plt.xlabel('$t / \mathrm{s}$')
plt.ylabel('$u_t (\mathrm{m/s})$')
plt.show()
