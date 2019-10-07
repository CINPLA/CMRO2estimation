# To run this code you must download the data folder
# or run figure4.m.

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib.patches as mpatches
from set_style import set_style

set_style('article', w=1, h=2)

filename = np.array([['../data/figure4/bias_a', '../data/figure4/bias_b', '../data/figure4/bias_c'], ['../data/figure4/bias_d', '../data/figure4/bias_e', '../data/figure4/bias_f'], ['../data/figure4/bias_g', '../data/figure4/bias_h', '../data/figure4/bias_i']])

panel = np.array([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])

fig, axarr = plt.subplots(3,3)
plt.draw()
p0 = axarr[2,0].get_position().get_points().flatten()
p1 = axarr[2,1].get_position().get_points().flatten()
p2 = axarr[2,2].get_position().get_points().flatten()

for i in range(0,3):
    for j in range(0,3):

        # load data
        data = sio.loadmat(filename[i,j])
        x = data['H_est'][0]
        y = data['H_est'][0]
        X, Y = np.meshgrid(x, y)
        Z = data['scaled_bias']

        cmap = cm.bwr

        cset1 = axarr[i,j].imshow(Z, extent=[min(x), max(x), min(y), max(y)], origin='lower', cmap=cm.get_cmap(cmap))

        if j == 0:    
            cset1.set_clim(-10, 10)
        else:
            cset1.set_clim(-100, 100)

        # ABC 
        if j == 0:
            axarr[i,j].text(-0.25, 1.1, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
        else:
            axarr[i,j].text(-0.1, 1.1, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

        # first colorbar
        if j == 0 and i == 2:
            ax_cbar0 = fig.add_axes([p0[0], 0.075, p0[2]-p0[0], 0.015])
            cbar = plt.colorbar(cset1, ticks=[-10,-5,0,5,10], cax=ax_cbar0, orientation='horizontal', extend='both')
            cbar.ax.set_xticklabels([-10, -5, 0, 5, 10], rotation=45)
            cbar.ax.tick_params(direction='in')

        # axes
        axarr[i,j].set(xticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1), yticks=np.arange(max(y)/2-1, max(y)/2+1.01, 1))

        axarr[i,j].set(xticklabels=['-1', '0', '1'])
        axarr[i,j].set(yticklabels=['-1', '0', '1'])
        axarr[i,j].xaxis.tick_top()
        axarr[i,j].get_yaxis().tick_left()
        
        # axes equal
        axarr[i,j].set_aspect('equal', 'box')

        # mark vessel
        vessel = mpatches.Circle((max(x)/2, max(y)/2), 6./141, facecolor='black')
        axarr[i,j].add_patch(vessel)

for i in range(1,3):
    for j in range(0,3):
        plt.setp(axarr[i,j].get_xticklabels(), visible=False)
for i in range(0,3):
    for j in range(1,3):
        plt.setp(axarr[i,j].get_yticklabels(), visible=False)

# d_data and q_data 
for i in range(0,3):
    a = sio.loadmat(filename[i,0])
    if i == 0:
        axarr[i,0].set_ylabel('$\hat{d}\mathrm{_{data}}=$\n$%.4f$' % a['d_data'], labelpad=10)
    else:
        axarr[i,0].set_ylabel('$\hat{d}\mathrm{_{data}}=$\n$%.3f$' % a['d_data'], labelpad=10)
    a = sio.loadmat(filename[0,i])
    if i == 0:
        axarr[0,i].set_xlabel('$\hat{d}\mathrm{_q}=%d$' % a['d_q'])
    else:
        axarr[0,i].set_xlabel('$\hat{d}\mathrm{_q}=%.2f$' % a['d_q'])
    axarr[0,i].xaxis.set_label_position('top')

# colorbars
ax_cbar1 = fig.add_axes([p1[0], 0.075, p1[2]-p1[0], 0.015])
ax_cbar2 = fig.add_axes([p2[0], 0.075, p2[2]-p2[0], 0.015])
for ax in [ax_cbar1, ax_cbar2]:
    cbar = plt.colorbar(cset1, ticks=[-100,-50,0,50,100], cax=ax, orientation='horizontal', extend='both')
    cbar.ax.set_xticklabels([-100, -50, 0, 50, 100], rotation=45)
    cbar.ax.tick_params(direction='in')

plt.savefig('figures_pdf/figure4.pdf', dpi=300)
