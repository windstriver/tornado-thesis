import numpy as np
import matplotlib.pylab as plt

r0 = 0.4
h0 = 0.4
z0 = 0.025
V0 = 0.34
u0 = 7/8*V0*np.power(h0/z0, 1/7)

data = np.genfromtxt('./Vt-data/Vt_z=0.03m.xy', skip_header=4, skip_footer=1)
data2 = np.genfromtxt('./Vt-data/Vt_z=0.1m.xy', skip_header=4, skip_footer=1)
data3 = np.genfromtxt('./Vt-data/Vt_z=0.2m.xy', skip_header=4, skip_footer=1)

r = data[:, 0]/r0
Vt = data[:, 1]/u0
r2 = data2[:, 0]/r0
Vt2 = data2[:, 1]/u0
r3 = data3[:, 0]/r0
Vt3 = data3[:, 1]/u0

np.savetxt('./Vt-data/Vt.csv', np.column_stack((r, Vt, r2, Vt2, r3, Vt3)), fmt='%10.5f', delimiter='   ')

# plt.plot(r, Vt, '-o')
# plt.show()
# 