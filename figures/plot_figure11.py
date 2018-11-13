# This code creates Figure 11.
# To be able to run this code you must download the data folder or
# run figure11.m.

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from set_style import set_style

set_style('article', w=1, h=4)

filename = np.array([['../data/figure11/figure11a', '../data/figure11/figure11b', '../data/figure11/figure11c'], ['../data/figure11/figure11d', '../data/figure11/figure11e', '../data/figure11/figure11f'], ['../data/figure11/figure11g', '../data/figure11/figure11h', '../data/figure11/figure11i']])

panel = np.array([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])

tableau10cb = np.array([(0,107,164), (255,128,14), (171,171,171), (89,89,89), (95,158,209), (200,82,0)])/255.

fig, axarr = plt.subplots(3, 3)

for i in range(0,3):
    for j in range(0,3):

        # load data
        data = sio.loadmat(filename[i,j])
        seed = data['seed']
        noise = data['sigma']
        dq_values = data['dq_values'][0]
        dcut_values = data['dcut_values'][0]
        estimates = [data['estimates_1'][0], data['estimates_2'][0], data['estimates_3'][0], data['estimates_4'][0], data['estimates_5'][0], data['estimates_6'][0]]

        for k in range(0, len(dcut_values)):
            axarr[i,j].plot(dq_values, estimates[k], 'o-', color=tableau10cb[k], markeredgecolor=tableau10cb[k], label=str(dcut_values[k]))

        # legend
#        if j == 2:
#            axarr[i][j].legend()

        # titles and labels
        if i == 0:
            axarr[i][j].set_title('$\hat{\sigma}$ = %.3f' % (noise))
        else:
            axarr[i][j].set_title('$\hat{\sigma}$ = %.1f' % (noise))
        if i == 2:
            axarr[i][j].set_xlabel('$\hat{d}\mathrm{_q}$')
        if j == 0:
            axarr[i][j].set_ylabel('$M_\mathrm{est}$')

        # frame lines
        axarr[i][j].spines['top'].set_visible(False)
        axarr[i][j].spines['right'].set_visible(False)

        # ticks
        axarr[i,j].set_xticks(np.arange(0,0.51,0.1))
        axarr[i,j].set_xticklabels(['0', '0.1', '0.2', '0.3', '0.4', '0.5'])
        axarr[i,j].tick_params(axis='x', rotation=45)
        axarr[i][j].get_xaxis().tick_bottom()
        axarr[i][j].get_yaxis().tick_left()

        # axes
        axarr[i][j].set_xlim(0,0.5)
        if i == 0:
            axarr[i][j].set_ylim(-1.25,1.25)
        elif i == 1:
            axarr[i][j].set_ylim(-1.25,1.25)
        elif i == 2:
            axarr[i][j].set_ylim(-4,4)

        # ABC
        axarr[i,j].text(-0.15, 1.1, panel[i,j], transform=axarr[i,j].transAxes, fontsize=22, fontweight='bold', va='top', ha='right')

axarr[2,1].legend(loc='upper center', bbox_to_anchor=(0.4, -0.2), ncol=3)

plt.tight_layout()
plt.savefig('figure11.pdf', bbox_inches='tight')

