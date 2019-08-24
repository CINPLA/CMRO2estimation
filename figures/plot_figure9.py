# To run this code you must download the data folder
# or run figure9.m.

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.font_manager import FontProperties
from set_style import set_style
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable

set_style('article', w=1, h=3)

tableau10cb = np.array([(0,107,164), (95,158,209), (171,171,171), (255,128,14), (89,89,89), (200,82,0)])/255.

fig, axarr = plt.subplots(3,3)
ax1 = axarr[0,1]
ax2 = axarr[1,0]
ax3 = axarr[1,1]
ax4 = axarr[1,2]
ax5 = axarr[2,0]
ax6 = axarr[2,1]
ax7 = axarr[2,2]

### A ###
data = sio.loadmat('../data/figure9/figure9_a')
dq_values = data['dq_values'][0]
dcut_values = data['dcut_values'][0]
scaled_bias = [data['scaled_bias_1'][0], data['scaled_bias_2'][0], data['scaled_bias_3'][0], data['scaled_bias_4'][0], data['scaled_bias_5'][0]]
for j in range(0,5):
    ax1.plot(dq_values, scaled_bias[j], '-', color=tableau10cb[j], label=str(dcut_values[j]))
ax1.set_title('BIAS [\%],$\, \hat{\sigma}\mathrm{_P}=0$')
ax1.legend(bbox_to_anchor=(2, 1), title='$\hat{d}\mathrm{_{cut}}$')

### B ###
data = sio.loadmat('../data/figure9/figure9_b')
x = data['H_est'][0]
y = data['H_est'][0]
sigma = data['sigma']
X, Y = np.meshgrid(x, y)
Z = data['scaled_rmse']
cmap = cm.Reds
cset = ax2.imshow(Z, extent=[min(x),max(x),min(y),max(y)], origin='lower', cmap=cm.get_cmap(cmap))
cset.set_clim(0,500)
divider = make_axes_locatable(ax2)
cax = divider.append_axes("right", size="5%", pad=0.05)
cbar = plt.colorbar(cset, cax=cax, extend='max')

# axes
ax2.set_aspect('equal', 'box')
ax2.set_xlabel('$\hat{x}$')
ax2.set_ylabel('$\hat{y}$')
ax2.set(xticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1), xticklabels=('-1', '0', '1'))
ax2.set(yticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1), yticklabels=('-1', '0', '1'))

ax2.set_title('RMSE [\%], '+'$\hat{\sigma}\mathrm{_P}=%.4f$' % data['sigma'])

### E ###
data = sio.loadmat('../data/figure9/figure9_e')
x = data['H_est'][0]
y = data['H_est'][0]
sigma = data['sigma']
X, Y = np.meshgrid(x, y)
Z = data['scaled_rmse']
cmap = cm.Reds
cset = ax5.imshow(Z, extent=[min(x),max(x),min(y),max(y)], origin='lower', cmap=cm.get_cmap(cmap))
cset.set_clim(0,500)
divider = make_axes_locatable(ax5)
cax = divider.append_axes("right", size="5%", pad=0.05)
cbar = plt.colorbar(cset, cax=cax, extend='max')
ax5.set_title('RMSE [\%], '+'$\hat{\sigma}\mathrm{_P}=%.2f$' % data['sigma']+'\n$\hat{d}\mathrm{_q}=0.1$')

# axes
ax5.set_aspect('equal', 'box')
ax5.set_xlabel('$\hat{x}$')
ax5.set_ylabel('$\hat{y}$')
ax5.set(xticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1), xticklabels=('-1', '0', '1'))
ax5.set(yticks=np.arange(max(x)/2-1, max(x)/2+1.01, 1), yticklabels=('-1', '0', '1'))

### CF ###
filenames = ['../data/figure9/figure9_c', '../data/figure9/figure9_f']
axarr = [ax3, ax6]
for i in range(0,2):

    # load data
    data = sio.loadmat(filenames[i])

    dq_values = data['dq_values'][0]
    dcut_values = data['dcut_values'][0]
    scaled_std = [data['scaled_std_1'][0], data['scaled_std_2'][0], data['scaled_std_3'][0], data['scaled_std_4'][0], data['scaled_std_5'][0]]

    for j in range(0,5):
        axarr[i].plot(dq_values, scaled_std[j], '-', color=tableau10cb[j], label=str(dcut_values[j]))

    # title 
    if i == 0:
        axarr[i].set_title('SD [\%], '+'$\hat{\sigma}\mathrm{_P}=%.4f$' % data['sigma'])
    else:
        axarr[i].set_title('SD [\%], '+'$\hat{\sigma}\mathrm{_P}=%.2f$' % data['sigma'])

### DG ###
filenames = ['../data/figure9/figure9_d', '../data/figure9/figure9_g']
axarr = [ax4, ax7]
for i in range(0,2):

    # load data
    data = sio.loadmat(filenames[i])

    dq_values = data['dq_values'][0]
    dcut_values = data['dcut_values'][0]
    scaled_rmse = [data['scaled_rmse_1'][0], data['scaled_rmse_2'][0], data['scaled_rmse_3'][0], data['scaled_rmse_4'][0], data['scaled_rmse_5'][0]]

    for j in range(0,5):
        axarr[i].plot(dq_values, scaled_rmse[j], '-', color=tableau10cb[j], label=str(dcut_values[j]))

    # title 
    if i == 0:
        axarr[i].set_title('RMSE [\%], '+'$\hat{\sigma}\mathrm{_P}=%.4f$' % data['sigma'])
    else:
        axarr[i].set_title('RMSE [\%], '+'$\hat{\sigma}\mathrm{_P}=%.2f$' % data['sigma'])

i = 0
for ax in [ax1, ax3, ax4, ax6, ax7]:
    # ticks
    ax.set_xlim(0, 0.2)
    ax.set_xticks(np.arange(0,0.21,0.1))
    ax.set_xlabel('$\hat{d}_\mathrm{q}$')
    ax.set_xticklabels(['0', '0.1', '0.2'])
    # frame lines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    i += 1

# ABCDEFG
panel = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
i = 0
for ax in [ax1, ax2, ax3, ax4, ax5, ax6, ax7]:
    ax.text(-0.25, 1.2, panel[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
    i += 1

ax1.set_ylim(-100, 10)
ax3.set_ylim(0, 0.6)
ax4.set_ylim(0, 100)
ax6.set_ylim(0, 60)
ax7.set_ylim(0, 100)

plt.savefig('figure9.pdf')
# Note that the figure has been edited in Inkscape for publication purposes.
