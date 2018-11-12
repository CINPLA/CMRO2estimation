# This figure creates Figure 5.
# To be able to run run this code you must download the data folder
# or run figure5.m.

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm, ticker
import matplotlib.patches as mpatches
from set_style import set_style

set_style('article', w=1, h=2)

filename = np.array([['../data/figure5/std_a', '../data/figure5/std_b', '../data/figure5/std_c', '../data/figure5/std_d'], ['../data/figure5/std_e', '../data/figure5/std_f', '../data/figure5/std_g', '../data/figure5/std_h'], ['../data/figure5/std_i', '../data/figure5/std_j', '../data/figure5/std_k',  '../data/figure5/std_l'],  ['../data/figure5/std_m', '../data/figure5/std_n', '../data/figure5/std_o', '../data/figure5/std_p']])

panel = np.array([['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K',  'L'],  ['M', 'N', 'O', 'P']])

fig, axarr = plt.subplots(4,4)

plt.draw()
p0 = axarr[3,0].get_position().get_points().flatten()
p1 = axarr[3,1].get_position().get_points().flatten()
p2 = axarr[3,2].get_position().get_points().flatten()
p3 = axarr[3,3].get_position().get_points().flatten()

for i in range(0,4):
    for j in range(0,4):

        # load data
        data = sio.loadmat(filename[i,j])
        x = data['H_est'][0]
        y = data['H_est'][0]
        X, Y = np.meshgrid(x, y)
        Z = data['scaled_std']

        cmap = cm.Reds

        cset1 = axarr[i,j].imshow(Z, extent=[min(x), max(x), min(y), max(y)], origin='lower', cmap=cm.get_cmap(cmap))
        
        # ABC
        if j == 0:
            axarr[i,j].text(-0.25, 1.1, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
        else:
            axarr[i,j].text(-0.1, 1.1, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

        if j == 0:
            cset1.set_clim(0,1e4)
        elif j == 1:
            cset1.set_clim(0,4e3)
        elif j == 2:
            cset1.set_clim(0,200)
        elif j == 3:
            cset1.set_clim(0,50)

        # colorbars
        if j == 0 and i == 0:
            ax_cbar0 = fig.add_axes([p0[0], 0.075, p0[2]-p0[0], 0.015])
            cbar = plt.colorbar(cset1, ticks=[1e4], cax=ax_cbar0, orientation='horizontal', extend='max')
            cbar.ax.set_xticklabels(['$10^4$'])
        elif j == 1 and i == 3:
            ax_cbar1 = fig.add_axes([p1[0], 0.075, p1[2]-p1[0], 0.015])
            cbar = plt.colorbar(cset1, ticks = [4e3], cax=ax_cbar1, orientation='horizontal', extend='max')
            cbar.ax.minorticks_on()
        elif j == 2 and i == 3:
            ax_cbar2 = fig.add_axes([p2[0], 0.075, p2[2]-p2[0], 0.015])
            cbar = plt.colorbar(cset1, ticks=[200], cax=ax_cbar2, orientation='horizontal', extend='max')
        elif j == 3 and i == 3:
            ax_cbar3 = fig.add_axes([p3[0], 0.075, p3[2]-p3[0], 0.015])
            cbar = plt.colorbar(cset1, ticks=[50], cax=ax_cbar3, orientation='horizontal', extend='max')

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

# axes
for i in range(1,4):
    for j in range(0,4):
        plt.setp(axarr[i,j].get_xticklabels(), visible=False)        
for i in range(0,4):
    for j in range(1,4):
        plt.setp(axarr[i,j].get_yticklabels(), visible=False)        
    
# d_data and q_data 
for i in range(0,4):
    a = sio.loadmat(filename[i,0])
    axarr[i,0].set_ylabel('$\hat{d}\mathrm{_{data}}=$\n$%.3f$' % a['d_data'])
    a = sio.loadmat(filename[0,i])
    axarr[0,i].set_xlabel('$\hat{d}\mathrm{_q}=%.2f$' % a['d_q'])
    axarr[0,i].xaxis.set_label_position('top')

#plt.tight_layout()
plt.savefig('figure5.pdf', dpi=300)
