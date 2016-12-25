import numpy as np

p0 = 100.0    # radial pressure at top, Pa.
R = 1.0    # radius of the column, m.
H = 9.0    # height of the column, m.

theta_grid = np.linspace(1/2*np.pi, 3/2*np.pi, 100)
y_grid = np.linspace(0, H, 100)

with open('cfd_pressure.csv', 'w') as f:
    for y in y_grid:
        for theta in theta_grid:
            R_noise = R*(1+0.1*np.random.rand(1))
            R_noise = R_noise[0]
            f.write("{X:9.3f},{Y:9.3f},{Z:9.3f},{P:9.3f}\n".format(X=R_noise*np.cos(theta), Y=y, Z=R_noise*np.sin(theta), P=-p0*y/H))


f.close()
