# To to run this code, you must download the data folder 
# or first run figure2.m.

import warnings
warnings.filterwarnings("ignore")
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from set_style import set_style

set_style('article', w=1, h=2)

fig = plt.figure()
gs = gridspec.GridSpec(6, 6)
ax1 = plt.subplot(gs[0:2,0:2])
ax2 = plt.subplot(gs[2:4,0:2])
ax3 = plt.subplot(gs[0:2,2:4])
ax4 = plt.subplot(gs[0:2,4:])
ax5 = plt.subplot(gs[2:4,2:4])
ax6 = plt.subplot(gs[2:4,4:])
ax7 = plt.subplot(gs[4:6,2:4])
ax8 = plt.subplot(gs[4:6,4:])
axarr = [[ax1,ax2], [ax3,ax4], [ax5,ax6], [ax7, ax8]]

# Panel A 
filename = '../data/figure2/figure2_a'
data = sio.loadmat(filename)
r_data = data['r_data'][0]
P = data['P'][0]
ax1.plot(r_data, P, 'r-')
ax1.set_xlim([-200,200])
ax1.set_ylim([10,90])
ax1.set(xticks=np.arange(-200, 201,200),yticks=np.arange(20, 81,20))
ax1.set_xticklabels([-200,  0, '200'])
ax1.axvline(x=-141, linestyle='--', color='k')
ax1.axvline(x=141, linestyle='--', color='k')
ax1.set_title('$P(r)$')

# Panel D
data = sio.loadmat('../data/figure2/figure2_bc')
P = data['P']
data = sio.loadmat('../data/figure2/figure2_def')
x = data['H_data'][0]
y = data['H_data'][0]
X, Y = np.meshgrid(x, y)
Z = data['P']-P
plt.setp(axarr[0][1].get_xticklabels(), visible=False)
axarr[0][1].set_title('$\hat{P}_{\sigma}$')
cmap = cm.Reds
levels = np.arange(-0.0013,0.0013,0.0001)
cset = axarr[0][1].imshow(Z, extent=[0, max(x), 0, max(y)], origin='lower', cmap=cm.get_cmap(cmap))
cbar = plt.colorbar(cset, ax=axarr[0][1], extend='both', ticks=[-0.001, 0, 0.001])
cset.set_clim(-0.0013,0.0013)
# axes
axarr[0][1].set(yticks=np.arange(max(y)/2-1, max(y)/2+1.01, 1))
axarr[0][1].set(xticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1))
axarr[0][1].set(yticklabels=['-1', '0', '1'])
axarr[0][1].set(xticklabels=['-1', '0', '1'])
# mark vessel
vessel = mpatches.Circle((max(x)/2,max(y)/2), 6./141, facecolor='black')
axarr[0][1].add_patch(vessel)

# Panel B, E, G
filenames = ['../data/figure2/figure2_bc', '../data/figure2/figure2_def', '../data/figure2/figure2_gh']
k = 0
for i in range(1,4):
    data = sio.loadmat(filenames[k])
    if i == 1 or i == 2:
        x = data['H_data'][0]
        y = data['H_data'][0]
        X, Y = np.meshgrid(x, y)
        Z = data['P']
        if data['sigma'] == 0:
            axarr[i][0].set_title('$\hat{P}$')
        else:
            axarr[i][0].set_title('$\hat{P} + \hat{P}_{\sigma}$')
        axarr[i][0].set(xticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1))
        axarr[i][0].set(xticklabels=[])
    elif i == 3:
        x = data['H_est'][0]
        y = data['H_est'][0]
        X, Y = np.meshgrid(x, y)
        Z = data['P_smooth']
        axarr[i][0].set_title('$\hat{P}\mathrm{_{smooth}}$')
        axarr[i][0].set(xticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1))
        axarr[i][0].set(xticklabels=['-1', '0', '1'])
    cmap = cm.Reds
    levels = np.arange(0,4.26,0.25)
    cset = axarr[i][0].contourf(X, Y, Z, levels, cmap='Reds', zorder=-9)
    axarr[i][0].set_rasterization_zorder(-1)
    fig.colorbar(cset, ax=axarr[i][0], ticks=np.arange(0, 4.1, 1))
    axarr[i][0].set(yticks=np.arange(max(y)/2-1, max(y)/2+1.01, 1))
    axarr[i][0].set(yticklabels=['-1', '0', '1'])
    vessel = mpatches.Circle((max(x)/2,max(y)/2), 6./141, facecolor='black')
    axarr[i][0].add_patch(vessel)
    k += 1

# Figure C, F, H
k = 0
for i in range(1,4):
    # load data
    data = sio.loadmat(filenames[k])
    if i == 1 or i == 2:
        x = data['H_data'][0]
        y = data['H_data'][0]
        X, Y = np.meshgrid(x, y)
    elif i == 3:
        x = data['H_est'][0]
        y = data['H_est'][0]
        X, Y = np.meshgrid(x, y)
    Z = data['del2P']
    # plot data
    cmap = cm.bwr
    if i == 1 or i == 3:
        cset = axarr[i][1].imshow(Z, extent=[0, max(x), 0, max(y)], origin='lower', cmap=cm.get_cmap(cmap))
        cbar = plt.colorbar(cset, ax=axarr[i][1], extend='both', ticks=np.arange(-0,2.01,0.5))
        cset.set_clim(-0.05,2.05)
    elif i == 2:
        cset = axarr[i][1].imshow(Z, extent=[0, max(x), 0, max(y)], origin='lower', cmap=cm.get_cmap(cmap))
        cb = plt.colorbar(cset, ax=axarr[i][1], extend='both', ticks=np.arange(-100,101,50))
        cset.set_clim(-100,100)
    # axes
    axarr[i][1].set(yticks=np.arange(max(y)/2-1, max(y)/2+1.01, 1))
    axarr[i][1].set(xticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1))
    axarr[i][1].set(yticklabels=[])
    axarr[i][1].set(xticklabels=[])
    # mark vessel
    vessel = mpatches.Circle((max(x)/2,max(y)/2), 6./141, facecolor='black')
    axarr[i][1].add_patch(vessel)
    axarr[i][1].set_title('$\hat{M}\mathrm{_{est}}$')
    k += 1
ax8.set(xticklabels=['-1', '0', '1'])

# labels
for ax in [ax2, ax3, ax7]:
    ax.set_ylabel('$\hat{y}$')
ax2.set_xlabel('$\hat{x}$')
axarr[3][0].set_xlabel('$\hat{x}$')
axarr[3][1].set_xlabel('$\hat{x}$')
ax5.set(yticklabels=[])

# ABC
panel = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
i = 0
for ax in [ax1, ax3, ax4, ax2, ax5, ax6, ax7, ax8]:
    ax.text(-0.2, 1.3, panel[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
    i += 1

plt.tight_layout(pad=0.5, w_pad=0.1, h_pad=0.1)
plt.savefig('figures_pdf/figure2.pdf', dpi=300)
