# CASE study of a sphere in tornado wind field

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

# Simulated tornado parameters
V_R = 82.3     # maximum tangential velocity (m/s)
R = 117.6       # core radius (m)

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
r0 = 300
z0 = 20        # hegith (m)
theta0 = 0
