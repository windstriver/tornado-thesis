############################################################
# CASE 2: ANSYS Fluent initialiate the flow field to Rankine
############################################################
import numpy as np

csv_Vr = np.genfromtxt('./input/Vr_Rankine.csv', delimiter=",",
                       skip_header=1)
r = csv_Vr[:, 0]
Vr = csv_Vr[:, 1]

csv_sphere = np.genfromtxt('./input/sphere_Rankine.csv', delimiter=',',
                           skip_header=1)
time = csv_sphere[:, 0]
u_t = csv_sphere[:, 8]
u_z = csv_sphere[:, 7]
