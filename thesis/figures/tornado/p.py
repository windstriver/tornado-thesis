import numpy as np
import matplotlib.pylab as plt

r0 = 0.4
h0 = 0.4
z0 = 0.025
V0 = 0.34
u0 = 7/8*V0*np.power(h0/z0, 1/7)
p0=-6.64

data = np.genfromtxt('./p-data/p_z=0.03m.xy', skip_header=4, skip_footer=1)
data2 = np.genfromtxt('./p-data/p_z=0.1m.xy', skip_header=4, skip_footer=1)
data3 = np.genfromtxt('./p-data/p_z=0.2m.xy', skip_header=4, skip_footer=1)

r = data[:, 0]/r0
p = data[:, 1]/p0
r2 = data2[:, 0]/r0
p2 = data2[:, 1]/p0
r3 = data3[:, 0]/r0
p3 = data3[:, 1]/p0

np.savetxt('./p-data/p.csv', np.column_stack((r, p, r2, p2, r3, p3)), fmt='%10.5f', delimiter='   ')

# plt.plot(r, Vt, '-o')
# plt.show()
