# This code creates Figure 8.
# To be able to run this code you must download the data folder or
# first run figure8_I.py and figure8_II.m.

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from set_style import set_style

set_style('article', w=1, h=1)

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

data = sio.loadmat('../data/figure8/figure8.mat')

## Figure A ##
x = data['Hx_est'][0]
y = data['Hy_est'][0]
X, Y = np.meshgrid(x,y)
Z = data['P_smooth']
cmap = cm.Reds
levels = np.arange(0,4.26,0.1)
cset = ax1.contourf(X, Y, Z, levels, cmap=cm.get_cmap(cmap), zorder=-9)
ax1.set_rasterization_zorder(-1)
ax1.set_aspect('equal')
fig.colorbar(cset, ax=ax1, fraction=0.035, ticks=np.arange(0,4.1,1))
ax1.set_title('$\hat{P}_\mathrm{smooth}$')
# axes
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()
ax1.set_xlabel('$\hat{x}$')
ax1.set_ylabel('$\hat{y}$', rotation=0, va='center')
ax1.set(xticks=np.arange(0, 4.1, 1))
ax1.set(xticklabels=['-2', '-1', '0', '1', '2'])
ax1.set(yticks=[0.5, 1.5, 2.5])
ax1.set(yticklabels=['-1', '0', '1'])

## Figure B ##
Z = data['del2P']
cmap = cm.bwr
cset = ax2.imshow(Z, extent=[0, max(x), 0, max(y)], origin='lower', cmap=cm.get_cmap(cmap), aspect='equal')
plt.colorbar(cset, ax=ax2, extend='both', fraction=0.0315, ticks=np.arange(0,2.1,0.5))
cset.set_clim(0,2)
ax2.set_title('$\hat{M}\mathrm{_{est}}$')
# axes
ax2.get_xaxis().tick_bottom()
ax2.get_yaxis().tick_left()
ax2.set_xlabel('$\hat{x}$')
ax2.set_ylabel('$\hat{y}$', rotation=0, va='center')
ax2.set(xticks=np.arange(0, 4.1, 1))
ax2.set(xticklabels=['-2', '-1', '0', '1', '2'])
ax2.set(yticks=[0.5, 1.5, 2.5])
ax2.set(yticklabels=['-1', '0', '1'])

# mark vessels
for ax in [ax1,ax2]:
    vessel = mpatches.Circle((1, 1.1), 6./141, facecolor='black')
    ax.add_patch(vessel)
for ax in [ax1,ax2]:
    vessel = mpatches.Circle((2.8, 0.8), 6./141, facecolor='black')
    ax.add_patch(vessel)
for ax in [ax1,ax2]:
    vessel = mpatches.Circle((3, 2), 6./141, facecolor='black')
    ax.add_patch(vessel)

# ABC
ax1.text(-0.05, 1.1, 'A', transform=ax1.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
ax2.text(-0.05, 1.1, 'B', transform=ax2.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

plt.tight_layout()
plt.savefig('figure8.pdf', bbox_inches="tight", dpi=300)
