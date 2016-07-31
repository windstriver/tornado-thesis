import numpy as np
from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas
from matplotlib.figure import Figure

r0 = 0.4
h0 = 0.4
z0 = 0.025
V0 = 0.34
u0 = 7/8*V0*np.power(h0/z0, 1/7)

cfd_dir = ['Vr_r=0.041m_CFD.xy', 'Vt_r=0.041m_CFD.xy', 'Va_r=0.041m_CFD.xy']
cfd_dir2 = ['Vr_r=0.085m_CFD.xy', 'Vt_r=0.085m_CFD.xy', 'Va_r=0.085m_CFD.xy']
exp_dir = ['-u_r=0.041m_Baker.csv', 'v_r=0.041m_Baker.csv', 'w_r=0.041m_Baker.csv']
exp_dir2 = ['-u_r=0.085m_Baker.csv', 'v_r=0.085m_Baker.csv', 'w_r=0.085m_Baker.csv']
out_dir = ['Vr', 'Vt', 'Va']


for i in range(3):
    vp_cfd = np.genfromtxt('./cfd-vs-exp/'+cfd_dir[i], skip_header=4, skip_footer=1)
    vp_baker = np.genfromtxt('./cfd-vs-exp/'+exp_dir[i], delimiter=',')
    vp_cfd2 = np.genfromtxt('./cfd-vs-exp/'+cfd_dir2[i], skip_header=4, skip_footer=1)
    vp_baker2 = np.genfromtxt('./cfd-vs-exp/'+exp_dir2[i], delimiter=',')

    z_cfd = vp_cfd[:,0]/h0
    V_cfd = vp_cfd[:,1]/u0
    z_baker = vp_baker[:,1]/100/h0
    if i==0:
        V_baker = -1.0*vp_baker[:,0]/100/u0
    else:
        V_baker = 1.0*vp_baker[:,0]/100/u0

    z_cfd2 = vp_cfd2[:,0]/h0
    V_cfd2 = vp_cfd2[:,1]/u0
    z_baker2 = vp_baker2[:,1]/100/h0
    if i==0:
        V_baker2 = -1.0*vp_baker2[:,0]/100/u0
    else:
        V_baker2 = 1.0*vp_baker2[:,0]/100/u0
        

    np.savetxt('./cfd-vs-exp/out/'+out_dir[i]+'_cfd.csv', np.column_stack((V_cfd, z_cfd)), fmt='%10.5f', delimiter='   ')
    np.savetxt('./cfd-vs-exp/out/'+out_dir[i]+'_exp.csv', np.column_stack((V_baker, z_baker)), fmt='%10.5f', delimiter='   ')
    np.savetxt('./cfd-vs-exp/out/'+out_dir[i]+'_cfd2.csv', np.column_stack((V_cfd2, z_cfd2)), fmt='%10.5f', delimiter='   ')
    np.savetxt('./cfd-vs-exp/out/'+out_dir[i]+'_exp2.csv', np.column_stack((V_baker2, z_baker2)), fmt='%10.5f', delimiter='   ')


# fig = Figure(figsize=(8, 4), tight_layout=True)
# canvas = FigureCanvas(fig)
# ax1 = fig.add_subplot(1, 2, 1)
# line_vp_cfd, = ax1.plot(V_cfd, z_cfd, 'b-+',label=r'CFD')
# line_vp_baker, = ax1.plot(V_baker, z_baker, 'ro', label=r'Baker')
# ax1.set_ylim(0, 0.3)
# ax1.set_xlim(0, 4)
# ax1.set_title(r'$r/R_0=0.1025$')
# ax1.set_xlabel(r'$V_t/U_0$')
# ax1.set_ylabel(r'$z/H_0$')
# ax1.tick_params(axis='both', labelsize=10)
# ax1.legend(handles=[line_vp_cfd, line_vp_baker], loc='upper left', fontsize=10)
# 
# ax2 = fig.add_subplot(1, 2, 2)
# line_vp_cfd2, = ax2.plot(V_cfd2, z_cfd2, 'b-+',label=r'CFD')
# line_vp_baker2, = ax2.plot(V_baker2, z_baker2, 'ro', label=r'Baker')
# ax2.set_ylim(0, 0.3)
# ax2.set_xlim(0, 4)
# ax2.set_title(r'$r/R_0=0.2125$')
# ax2.set_xlabel(r'$V_t/U_0$')
# ax2.set_ylabel(r'$z/H_0$')
# ax2.tick_params(axis='both', labelsize=10)
# ax2.legend(handles=[line_vp_cfd2, line_vp_baker2], loc='upper right', fontsize=10)
# 
# fig.savefig('velocity_profile_Vt.pdf')
# 