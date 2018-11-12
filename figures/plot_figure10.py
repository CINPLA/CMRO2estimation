# This code creates Figure 10. 
# To be able to tun this code you must download the data folder
# or run figure10.m.

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.font_manager import FontProperties
from set_style import set_style

set_style('article', w=1, h=4)

tableau10cb = np.array([(0,107,164), (255,128,14), (171,171,171), (89,89,89), (95,158,209), (200,82,0)])/255.

fig = plt.figure()
gs = gridspec.GridSpec(4, 4)
ax1 = plt.subplot(gs[0,1:3])
ax2 = plt.subplot(gs[1,0:2])
ax3 = plt.subplot(gs[1,2:])
ax4 = plt.subplot(gs[2,0:2])
ax5 = plt.subplot(gs[2,2:])
ax6 = plt.subplot(gs[3,0:2])
ax7 = plt.subplot(gs[3,2:])

# A
data = sio.loadmat('../data/figure10/figure10_a')
dq_values = data['dq_values'][0]
dcut_values = data['dcut_values'][0]
scaled_bias = [data['scaled_bias_1'][0], data['scaled_bias_2'][0], data['scaled_bias_3'][0], data['scaled_bias_4'][0], data['scaled_bias_5'][0], data['scaled_bias_6'][0]]
for j in range(0,6):
    ax1.plot(dq_values, scaled_bias[j], 'o-', color=tableau10cb[j], markeredgecolor=tableau10cb[j], label=str(dcut_values[j]))
ax1.legend(bbox_to_anchor=(1.7, 1.2), title='$d\mathrm{_{cut}}$')
ax1.set_title('BIAS,$\, \hat{\sigma}=0$')
ax1.set_ylabel('BIAS$[\%]$')

# BDF
filenames = ['../data/figure10/figure10_b', '../data/figure10/figure10_d', '../data/figure10/figure10_f']
axarr = [ax2, ax4, ax6]
for i in range(0,3):

    # load data
    data = sio.loadmat(filenames[i])

    dq_values = data['dq_values'][0]
    dcut_values = data['dcut_values'][0]
    scaled_std = [data['scaled_std_1'][0], data['scaled_std_2'][0], data['scaled_std_3'][0], data['scaled_std_4'][0], data['scaled_std_5'][0], data['scaled_std_6'][0]]

    for j in range(0,6):
        axarr[i].plot(dq_values, scaled_std[j], 'o-', color=tableau10cb[j], markeredgecolor=tableau10cb[j], label=str(dcut_values[j]))

    # title, label
    if i == 0:
        axarr[i].set_title('SD,$\, \hat{\sigma}=%.3f$' % data['sigma'])
    else:
        axarr[i].set_title('SD,$\, \hat{\sigma}=%.1f$' % data['sigma'])
    axarr[i].set_ylabel('SD $[\%]$')

# BDF
filenames = ['../data/figure10/figure10_c', '../data/figure10/figure10_e', '../data/figure10/figure10_g']
axarr = [ax3, ax5, ax7]
for i in range(0,3):
    # load data
    data = sio.loadmat(filenames[i])

    dq_values = data['dq_values'][0]
    dcut_values = data['dcut_values'][0]
    scaled_rmse = [data['scaled_rmse_1'][0], data['scaled_rmse_2'][0], data['scaled_rmse_3'][0], data['scaled_rmse_4'][0], data['scaled_rmse_5'][0], data['scaled_rmse_6'][0]]

    for j in range(0,6):
        axarr[i].plot(dq_values, scaled_rmse[j], 'o-', color=tableau10cb[j], markeredgecolor=tableau10cb[j], label=str(dcut_values[j]))

    # title, label
    if i == 0:
        axarr[i].set_title('RMSE, $\, \hat{\sigma}=%.3f$' % data['sigma'])
    else:
        axarr[i].set_title('RMSE, $\, \hat{\sigma}=%.1f$' % data['sigma'])
    axarr[i].set_ylabel('RMSE $[\%]$')

panel = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
i = 0
for ax in [ax1, ax2, ax3, ax4, ax5, ax6, ax7]:
    ax.set_xticks(np.arange(0,0.51,0.1))
    # ticks
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left()  
    # frame lines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # ABC
    ax.text(-0.15, 1.15, panel[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
    i += 1

ax2.set_yticks(np.arange(0,21,5))
ax3.set_yticks(np.arange(0,251,50))
ax4.set_yticks(np.arange(0,81,20))
ax5.set_yticks(np.arange(0,251,50))
ax6.set_yticks(np.arange(0,301,50))
ax7.set_yticks(np.arange(0,301,50))

plt.tight_layout()
plt.savefig('figure10.pdf')
