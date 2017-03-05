import numpy as np
import matplotlib.pyplot as plt

inputFile = 'tornado_loads_sum.out'

data = np.genfromtxt(inputFile, skip_header=1, delimiter=',')

time = data[:, 0]
fx_tot = data[:, 1]
fy_tot = data[:, 2]

plt.plot(time, fx_tot, time, fy_tot)
plt.show()
