import numpy as np

output = 'Vt.csv'
output2 = 'Vr.csv'

Rcm = 120
Vtmax = 80

def Vr(r):
    if r < Rcm:
        return r/Rcm*Vtmax
    else:
        return Rcm/r*Vtmax

r_points = 600
z_points = 300
r_array = np.linspace(0, 600, r_points, endpoint=False)
z_array = np.linspace(0, 300, z_points, endpoint=False)

velocity = np.zeros((r_points+1, z_points+1))
velocity[0,1:] = z_array
velocity[1:,0] = r_array

for i in range(r_points):
    for j in range(z_points):
        velocity[i+1,j+1] = Vr(r_array[i])

velocity2 = np.zeros((r_points+1, z_points+1))
velocity2[0,1:] = z_array
velocity2[1:,0] = r_array

np.savetxt(output, velocity, fmt='%.3e', delimiter=',')
np.savetxt(output2, velocity2, fmt='%.3e', delimiter=',')
