############################################################
# CASE 3: ANSYS Fluent full scale simulation of tornado
############################################################
import numpy as np

csv_Vr = np.genfromtxt('./input/Vr_full.csv', delimiter=",",
                       skip_header=1)
r = csv_Vr[:, 0]
Vr = csv_Vr[:, 1]

csv_sphere = np.genfromtxt('./input/sphere_full.csv', delimiter=',',
                           skip_header=1)
time = csv_sphere[:, 0]
u_t = csv_sphere[:, 8]
u_z = csv_sphere[:, 7]