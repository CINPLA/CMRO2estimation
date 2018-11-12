import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib.patches as mpatches
from set_style import set_style

set_style('article', w=1, h=2.5)

filename = np.array([['../data/figure4/bias_a', '../data/figure5/std_a', '../data/figure6/rmse_a'], ['../data/figure4/bias_b', '../data/figure5/std_b', '../data/figure6/rmse_b'], ['../data/figure4/bias_c', '../data/figure5/std_c', '../data/figure6/rmse_c'], ['../data/figure4/bias_d', '../data/figure5/std_d', '../data/figure6/rmse_d']])

panel = np.array([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L']])

fig, axarr = plt.subplots(4,3)

# BIAS
for i in range(0,4):
    j = 0

    data = sio.loadmat(filename[i,j])
    x = data['H_est'][0]
    y = data['H_est'][0]
    X, Y = np.meshgrid(x, y)
    Z = data['scaled_bias']
    cmap = cm.bwr

    cset1 = axarr[i,j].imshow(Z, extent=[min(x),max(x),min(y),max(y)], origin='lower', cmap=cm.get_cmap(cmap))
    if i == 0:
        cbar = fig.colorbar(cset1, ax=axarr[i,j], ticks=np.arange(-10, 11, 5), extend='both')
        cbar.ax.set_yticklabels(['-10', '-5', '0', '5', '10'])
        cset1.set_clim(-10, 10)
    else:
        cbar = fig.colorbar(cset1, ax=axarr[i,j], ticks=np.arange(-100, 101, 50), extend='both')
        cbar.ax.set_yticklabels(['-100', '-50', '0', '50', '100'])
        cset1.set_clim(-100, 100)

    axarr[i,0].set_ylabel('$\hat{d}\mathrm{_q}=%.2f$' % data['d_q'])

# STD
for i in range(0,4):
    j = 1

    data = sio.loadmat(filename[i,j])
    x = data['H_est'][0]
    y = data['H_est'][0]
    X, Y = np.meshgrid(x, y)
    Z = data['scaled_std']
    cmap = cm.Reds

    cset1 = axarr[i,j].imshow(Z, extent=[min(x),max(x),min(y),max(y)], origin='lower', cmap=cm.get_cmap(cmap))
    
    if i == 0:
        cset1.set_clim(1e4,1e6)
        cbar = fig.colorbar(cset1, ax=axarr[i,j], ticks=[1e4, 1e6], extend='both')
        cbar.ax.set_yticklabels(['$10^4$', '$10^6$'])
    elif i == 1:
        cset1.set_clim(400,500)
        fig.colorbar(cset1, ax=axarr[i,j], ticks=np.arange(400, 500.1, 25), extend='both')
    elif i == 2:
        cset1.set_clim(10,20)
        fig.colorbar(cset1, ax=axarr[i,j], extend='both')
    elif i == 3: 
        cset1.set_clim(4,8)
        fig.colorbar(cset1, ax=axarr[i,j], ticks=np.arange(4, 8.1, 1), extend='both')
    
# RMSE 
for i in range(0,4):
    j = 2

    a = sio.loadmat(filename[i,j])
    x = a['H_est'][0]
    y = a['H_est'][0]
    X, Y = np.meshgrid(x, y)
    Z = a['scaled_rmse']
    cmap = cm.Reds

    cset1 = axarr[i,j].imshow(Z, extent=[min(x),max(x),min(y),max(y)], origin='lower', cmap=cm.get_cmap(cmap))

    if i == 0:
        cset1.set_clim(1e4,1e6)
        cbar = fig.colorbar(cset1, ax=axarr[i,j], ticks=[1e4, 1e6], extend='both')
        cbar.ax.set_yticklabels(['$10^4$', '$10^6$'])
    elif i == 1:
        cset1.set_clim(0, 500)
        fig.colorbar(cset1, ax=axarr[i,j], ticks=np.arange(0, 500.1, 125), extend='max')
    elif i == 2:
        cset1.set_clim(0, 100)
        fig.colorbar(cset1, ax=axarr[i,j], ticks=np.arange(0, 100.1, 25), extend='max')
    elif i == 3: 
        cset1.set_clim(0, 100)
        fig.colorbar(cset1, ax=axarr[i,j], ticks=np.arange(0, 100.1, 25), extend='max')
    
for i in range(0,4):
    for j in range(0,3):
        # axes
        axarr[i][j].get_xaxis().tick_bottom()
        axarr[i][j].get_yaxis().tick_left()
        axarr[i,j].set_aspect('equal', 'box')
        # mark vessel
        vessel = mpatches.Circle((max(x)/2,max(y)/2), 6./141, facecolor='black')
        axarr[i,j].add_patch(vessel)
        # ABC
        if j == 0:
            axarr[i,j].text(-0.2, 1.1, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
        else:
            axarr[i,j].text(-0.1, 1.1, panel[i,j], transform=axarr[i,j].transAxes, fontsize=16, fontweight='bold', va='top', ha='right')

# axes
for ax in axarr.flat:
    ax.set(xticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1), yticks=np.arange(max(y)/2-1, max(y)/2+1.01, 1))
    ax.set(xticklabels=['-1', '0', '1'])
    ax.set(yticklabels=['-1', '0', '1'])
for i in range(0,3):
    for j in range(0,3):
        plt.setp(axarr[i,j].get_xticklabels(), visible=False)        
for i in range(0,4):
    for j in range(1,3):
        plt.setp(axarr[i,j].get_yticklabels(), visible=False)

axarr[0,0].set_title('BIAS $[\%]$')
axarr[0,1].set_title('SD $[\%]$')
axarr[0,2].set_title('RMSE $[\%]$')

plt.tight_layout()
plt.savefig('figure3.pdf', dpi=300)


