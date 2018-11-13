# This code creates Figure 2.
# To be able to run this code, you must download the data folder 
# or first run figure2.m.

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib.patches as mpatches
from set_style import set_style

set_style('article', w=1, h=4)

fig, axarr = plt.subplots(4,2)

# Figure A og B
filenames = ['../data/figure2/figure2_a', '../data/figure2/figure2_b']
for i in range(0,2):
    data = sio.loadmat(filenames[i])
    r_data = data['r_data'][0]
    P = data['P'][0]
    axarr[0,i].plot(r_data, P, 'r-')
    axarr[0,i].set_xlim([-100,200])
    axarr[0,i].set_ylim([10,90])
    axarr[0,i].set(xticks=np.arange(-200, 201,100),yticks=np.arange(20, 81,10))
    axarr[0,i].set_xticklabels([-200, -100, 0, 100, '$r$'])
    axarr[0,i].axvline(x=-141, linestyle='--', color='k')
    axarr[0,i].axvline(x=141, linestyle='--', color='k')
    if data['sigma'] == 0:
        axarr[0,i].set_title('$P$')
    else:
        axarr[0,i].set_title('$P+P_{\sigma}$')
plt.setp(axarr[0,1].get_yticklabels(), visible=False)

# Figure C, E, G
filenames = ['../data/figure2/figure2_cd', '../data/figure2/figure2_ef', '../data/figure2/figure2_gh']
k = 0
for i in range(1,4):
    data = sio.loadmat(filenames[k])
    if i == 1 or i == 2:
        x = data['H_data'][0]
        y = data['H_data'][0]
        X, Y = np.meshgrid(x, y)
        Z = data['P']
        plt.setp(axarr[i,0].get_xticklabels(), visible=False)
        if data['sigma'] == 0:
            axarr[i,0].set_title('$\hat{P}$')
        else:
            axarr[i,0].set_title('$\hat{P} + \hat{P}_{\sigma}$')
    elif i == 3:
        x = data['H_est'][0]
        y = data['H_est'][0]
        X, Y = np.meshgrid(x, y)
        Z = data['P_smooth']
        axarr[i,0].set_title('$\hat{P}\mathrm{_{smooth}}$')
    cmap = cm.Reds
    levels = np.arange(0,4.26,0.25)
    cset = axarr[i,0].contourf(X, Y, Z, levels, cmap='Reds', zorder=-9)
    axarr[i,0].set_rasterization_zorder(-1)
    fig.colorbar(cset, ax=axarr[i,0], ticks=np.arange(0, 4.1, 1))
    # axes
    axarr[i,0].set(yticks=np.arange(max(x)/2-1, max(x)/2+1.01, 0.5))
    axarr[i,0].set(yticklabels=['-1', '-0.5', '0', '0.5', '1'])
    # mark vessel
    vessel = mpatches.Circle((max(x)/2,max(y)/2), 6./141, facecolor='black')
    axarr[i,0].add_patch(vessel)
    k += 1

# Figure D, F, H
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
        cset = axarr[i,1].imshow(Z, extent=[0, max(x), 0, max(y)], origin='lower', cmap=cm.get_cmap(cmap))
        cbar = plt.colorbar(cset, ax=axarr[i,1], extend='both', ticks=np.arange(-0,2.01,0.5))
        cset.set_clim(-0.05,2.05)
    elif i == 2:
        cset = axarr[i,1].imshow(Z, extent=[0, max(x), 0, max(y)], origin='lower', cmap=cm.get_cmap(cmap))
        cb = plt.colorbar(cset, ax=axarr[i,1], extend='both', ticks=np.arange(-1000,1001,500))
        cset.set_clim(-1000,1000)
    # axes
    axarr[i,1].set(yticks=np.arange(max(x)/2-1, max(x)/2+1.01, 0.5))
    # remove tick labels 
    if i == 1 or i == 2:
        plt.setp(axarr[i,1].get_xticklabels(), visible=False)
    plt.setp(axarr[i,1].get_yticklabels(), visible=False)
    # mark vessel
    vessel = mpatches.Circle((max(x)/2,max(y)/2), 6./141, facecolor='black')
    axarr[i,1].add_patch(vessel)
    axarr[i,1].set_title('$\hat{M}\mathrm{_{est}}$')
    k += 1

# axes equal
for i in range(1,4):
    for j in range(0,2):
        axarr[i,j].set_aspect('equal', 'box')

# axes
for i in range(0,4):
    for j in range(0,2):
        if i != 0:
            axarr[i,j].set(xticks=np.arange(max(x)/2-1, max(x)/2+1.01, 0.5))
        axarr[i][j].get_xaxis().tick_bottom()
        axarr[i][j].get_yaxis().tick_left() 
for j in range(0,2):
    axarr[3,j].set(xticklabels=['-1', '-0.5', '0', '0.5', '1'])

# labels
axarr[0,0].set_ylabel('$P$')
axarr[3,0].set_xlabel('$\hat{x}$')
axarr[3,1].set_xlabel('$\hat{x}$')
for i in range(1,4):
    axarr[i,0].set_ylabel('$\hat{y}$')

# ABC
panel = np.array([['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H']])
for i in range(0,4):
    for j in range(0,2):
        if i == 0:
            axarr[i,j].text(-0.02, 1.2, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
        else:
            axarr[i,j].text(-0.09, 1.2, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

plt.tight_layout()
plt.savefig('figure2.pdf', dpi=300)
