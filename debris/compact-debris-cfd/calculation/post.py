# Post processing
from case1 import *
from case2 import *
from case3 import *
import case4
import case5

from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas
from matplotlib.figure import Figure

fig = Figure(tight_layout=True)
canvas = FigureCanvas(fig)
ax1 = fig.add_subplot(1, 2, 1)
line_u_t1, = ax1.plot(time, u_t, label=r'Case 1')
line_u_t2, = ax1.plot(time2, u_t2, '--', label=r'Case 2')
line_u_t3, = ax1.plot(time3, u_t3, '-.', label=r'Case 3')
ax1.set_xlabel(r'$t / \mathrm{s}$')
ax1.set_ylabel(r'$u_t (\mathrm{m/s})$')
ax1.legend(handles=[line_u_t1, line_u_t2, line_u_t3], loc='upper left')

ax2 = fig.add_subplot(1, 2, 2)
line_u_z1, = ax2.plot(time, u_z, label=r'Case 1')
line_u_z2, = ax2.plot(time2, u_z2, '--', label=r'Case 2')
line_u_z3, = ax2.plot(time3, u_z3, '-.', label=r'Case 3')
ax2.set_xlabel(r'$t / \mathrm{s}$')
ax2.set_ylabel(r'$u_z (\mathrm{m/s})$')
ax2.legend(handles=[line_u_z1, line_u_z2, line_u_z3])

fig.savefig('velocity_history.pdf')

fig2 = Figure(tight_layout=True)
canvas2 = FigureCanvas(fig2)
ax1 = fig2.add_subplot(1, 2, 1)
line_u_t3, = ax1.plot(time3, u_t3, '', label=r'Case 3')
line_u_t4, = ax1.plot(case4.time, case4.u_t, '--', label=r'Case 4')
line_u_t5, = ax1.plot(case5.time, case5.u_t, '-.', label=r'Case 5')
ax1.set_xlabel(r'$t / \mathrm{s}$')
ax1.set_ylabel(r'$u_t (\mathrm{m/s})$')
ax1.legend(handles=[line_u_t3, line_u_t4, line_u_t5], loc='upper left')

ax2 = fig2.add_subplot(1, 2, 2)
line_u_z3, = ax2.plot(time3, u_z3, label=r'Case 3')
line_u_z4, = ax2.plot(case4.time, case4.u_z, '--', label=r'Case 4')
line_u_z5, = ax2.plot(case5.time, case5.u_z, '-.', label=r'Case 5')
ax2.set_xlabel(r'$t / \mathrm{s}$')
ax2.set_ylabel(r'$u_z (\mathrm{m/s})$')
ax2.legend(handles=[line_u_z3, line_u_z4, line_u_z5])


fig2.savefig('velocity_history2.pdf')
