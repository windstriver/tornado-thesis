############################################################
# CASE 2: ANSYS Fluent initialiate the flow field to Rankine
############################################################
import numpy as np
from setup import *

csv2_Vr = np.genfromtxt('./input/Vr-r_Rankine.csv', delimiter=",",
                        skip_header=1)
r2 = csv2_Vr[:, 0]
Vr2 = csv2_Vr[:, 1]

csv2_sphere = np.genfromtxt('./input/sphere_Rankine.csv', delimiter=',',
                            skip_header=1)
time2 = csv2_sphere[:, 0]
u_t2 = csv2_sphere[:, 8]
u_z2 = csv2_sphere[:, 7]
