import numpy as np

import matplotlib
matplotlib.use("pgf")
pgf_with_custom_preamble = {
    # "font.size": 18,
    "pgf.rcfonts": False,
    "text.usetex": True,
    "pgf.preamble": [
        # math setup:
        r"\usepackage{unicode-math}",

        # fonts setup:
        r"\setmainfont{WenQuanYi Zen Hei}",
        r"\setsansfont{WenQuanYi Zen Hei}",
        r"\setmonofont{WenQuanYi Zen Hei Mono}",
    ],
}
matplotlib.rcParams.update(pgf_with_custom_preamble)

import matplotlib.pyplot as plt


inputFile = 'tornado_loads_sum.out'

data = np.genfromtxt(inputFile, skip_header=1, delimiter=',')

time = data[:, 0]
fx_tot = data[:, 1]/10**6
fy_tot = data[:, 2]/10**6

line_fx, = plt.plot(time, fx_tot, label=u'$X$向龙卷风合力')
line_fy, = plt.plot(time, fy_tot, label=u'$Y$向龙卷风合力')
# plt.plot(time, fy_tot)
plt.ylim(-15,6)
plt.xlabel('$t(\mathrm{s})$')
plt.ylabel('$\sum F_i (X10^6 \mathrm{N})$')
plt.legend()
plt.savefig('post.pdf', format='pdf')
plt.close()
