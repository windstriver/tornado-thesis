############################################################
# CASE 3: ANSYS Fluent initialiate the flow field to Rankine
############################################################
import numpy as np
from setup import *

csv3_Vr = np.genfromtxt('./input/Vr-r_full.csv', delimiter=",",
                        skip_header=1)
r3 = csv3_Vr[:, 0]
Vr3 = csv3_Vr[:, 1]

csv3_sphere = np.genfromtxt('./input/sphere_full.csv', delimiter=',',
                            skip_header=1)
time3 = csv3_sphere[:, 0]
u_t3 = csv3_sphere[:, 8]
u_z3 = csv3_sphere[:, 7]
