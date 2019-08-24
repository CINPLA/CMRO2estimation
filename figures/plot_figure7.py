# To run this code you must download the data folder or
# first run figure7_I.py and figure7_II.m.

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from set_style import set_style

set_style('article', w=1, h=2)

fig = plt.figure()
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

data = sio.loadmat('../data/figure7/figure7.mat')

# Figure A
x = data['Hx_data'][0]
y = data['Hy_data'][0]
X, Y = np.meshgrid(x,y)
Z = data['P']
print Z.max()
cmap = cm.Reds
cset = ax1.plot_surface(X, Y, Z, cmap=cm.get_cmap(cmap), linewidth=0, rstride=10, cstride=10)
plt.colorbar(cset, ax=ax1, ticks=np.arange(1,4.1,1))
cset.set_clim(1,4.25)
ax1.set_title('$\hat{P}$', y=1.05)
ax1.view_init(50,190+45)
## make the panes transparent
ax1.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax1.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax1.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# axes
ax1.set(xticks=np.arange(0, 2.01, 1))
ax1.set(xticklabels=['-1', '0', '1'])
ax1.set(yticks=np.arange(0, 2.01, 1))
ax1.set(yticklabels=['-1', '0', '1'])
ax1.set(zticks=np.arange(1, 4.01, 1))
ax1.set_xlabel('$\hat{x}$')
ax1.set_ylabel('$\hat{y}$')
ax1.xaxis.set_rotate_label(False)
ax1.yaxis.set_rotate_label(False)

# Figure B
Z = data['P_noisy']
levels = np.arange(1, 4.26,0.1)
cmap = cm.Reds
cset = ax2.contourf(X, Y, Z, levels, cmap=cm.get_cmap(cmap))
ax2.set_aspect('equal')
plt.colorbar(cset, ax=ax2, ticks=np.arange(1,4.1,1))
ax2.set_title('$\hat{P}+\hat{P}_{\sigma}$')
cset.set_clim(1,4.25)

# Figure C
Z = data['del2P_panelC']
cmap = cm.bwr
cset = ax3.imshow(Z, extent=[0, max(x), 0, max(y)], origin='lower', cmap=cm.get_cmap(cmap))
plt.colorbar(cset, ax=ax3, ticks=[-0.5, 0.5, 2, 3], extend='both')
cset.set_clim(-0.5,3)
ax3.set_title('$\hat{M}\mathrm{_{est}}$')

# Figure D
x = data['Hx_est'][0]
y = data['Hy_est'][0]
Z = data['del2P_panelD']
cmap = cm.bwr
cset = ax4.imshow(Z, extent=[0, max(x), 0, max(y)], origin='lower', cmap=cm.get_cmap(cmap))
cset.set_clim(-0.5,3)
cbar = plt.colorbar(cset, ax=ax4, ticks=[-0.5, 0.5, 2, 3], extend='both')
ax4.set_title('$\hat{M}\mathrm{_{est}}$')

for ax in [ax2, ax3, ax4]:
    # mark vessel
    vessel = mpatches.Circle((1, 1), 6./141, facecolor='black')
    ax.add_patch(vessel)
    # axes
    ax.set(xticks=np.arange(0, 2.01, 0.5))
    ax.set(xticklabels=['-1', '-0.5', '0', '0.5', '1'])
    ax.set(yticks=np.arange(0, 2.01, 0.5))
    ax.set(yticklabels=['-1', '-0.5', '0', '0.5', '1'])
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()    
    ax.set_xlabel('$\hat{x}$')
    ax.set_ylabel('$\hat{y}$', rotation=0, va='center')

# ABC
ax3.text(-0.15, 2.78, 'A', transform=ax3.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
ax2.text(-0.15, 1.1, 'B', transform=ax2.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
ax3.text(-0.15, 1.1, 'C', transform=ax3.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
ax4.text(-0.15, 1.1, 'D', transform=ax4.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

plt.tight_layout()
plt.savefig('figure7.pdf', dpi=300)
