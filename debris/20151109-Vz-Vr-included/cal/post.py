# Post processing
import case1 as c1

from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas
from matplotlib.figure import Figure

fig = Figure(tight_layout=True)
canvas = FigureCanvas(fig)
ax1 = fig.add_subplot(1, 2, 1)
line_u_z, = ax1.plot(c1.time, c1.u_z, label=r'Case 1')
ax1.set_xlabel(r'$t / \mathrm{s}$')
ax1.set_ylabel(r'$u_z (\mathrm{m/s})$')
ax2 = fig.add_subplot(1, 2, 2)
line_z, = ax2.plot(c1.time, c1.z, label=r'Case 1')
ax2.set_xlabel(r'$t / \mathrm{s}$')
ax2.set_ylabel(r'$z (\mathrm{m})$')
fig.savefig('z_hist.pdf')


fig2 = Figure(tight_layout=True)
canvas = FigureCanvas(fig2)
ax1 = fig2.add_subplot(1, 2, 1)
line_u_t, = ax1.plot(c1.time, c1.u_t, label=r'Case 1')
ax1.set_xlabel(r'$t / \mathrm{s}$')
ax1.set_ylabel(r'$u_t (\mathrm{m/s})$')
ax2 = fig2.add_subplot(1, 2, 2)
line_theta, = ax2.plot(c1.time, c1.theta, label=r'Case 1')
ax2.set_xlabel(r'$t / \mathrm{s}$')
ax2.set_ylabel(r'$\theta (\mathrm{\degree})$')
fig2.savefig('theta_hist.pdf')


fig3 = Figure(tight_layout=True)
canvas = FigureCanvas(fig3)
ax1 = fig3.add_subplot(1, 2, 1)
line_u_r, = ax1.plot(c1.time, c1.u_r, label=r'Case 1')
ax1.set_xlabel(r'$t / \mathrm{s}$')
ax1.set_ylabel(r'$u_r (\mathrm{m/s})$')
ax2 = fig3.add_subplot(1, 2, 2)
line_theta, = ax2.plot(c1.time, c1.r, label=r'Case 1')
ax2.set_xlabel(r'$t / \mathrm{s}$')
ax2.set_ylabel(r'$r (\mathrm{m})$')
fig3.savefig('r_hist.pdf')
