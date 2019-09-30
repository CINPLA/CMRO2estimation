# To run this code, you must download the data folder or first run
# figure1a.m
# figure1c.m and
# figure1e.m
# (The numbers that are used in panel B and D have been extracted manually from A and C.)

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib.gridspec as gridspec
import matplotlib.ticker as mticker
from set_style import set_style

set_style('article', w=1, h=3)

# scientific notation
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
fmt = mticker.FuncFormatter(g)

fig = plt.figure()
gs = gridspec.GridSpec(3, 4)
ax1 = plt.subplot(gs[0,0:2])
ax2 = plt.subplot(gs[0,2:])
ax3 = plt.subplot(gs[1,0:2])
ax4 = plt.subplot(gs[1,2:])
ax5 = plt.subplot(gs[2,1:3])

tableau10cb = np.array([(0,107,164), (255,128,14), (171,171,171), (89,89,89), (95,158,209), (200,82,0)])/255.

## A ##
filenames = ['../data/figure1/delta_vs_r__dfixed__1', '../data/figure1/delta_vs_r__dfixed__2', '../data/figure1/delta_vs_r__dfixed__3', '../data/figure1/delta_vs_r__dfixed__4']
for i in range(0,4):
    data = sio.loadmat(filenames[i])
    delta_smooth = data['delta_smooth_vector']
    r =  data['r']
    q =  data['q'][0][0]
    ax1.plot(r, delta_smooth, '-o', color=tableau10cb[i], markeredgecolor=tableau10cb[i], label="{}".format(fmt(q)))
leg = ax1.legend(frameon=0, fontsize='x-small')
leg.set_title('q', prop={'size':'small'})
# axes
ax1.set_xlim(0, 0.05)
ax1.set_ylim(-0.05, 1)
ax1.set_yticks([0,1])
# dotted line
ax1.axvline(x=3.76e-3, ymax=0.525, color='k', ls=':')
ax1.axhline(y=0.5, xmax=0.0752, color='k', ls=':')
# title and labels
ax1.set_title('$\delta\mathrm{_{smooth}}$ ($\hat{d}=0.005$)')
ax1.set_xlabel('$\hat{r}$')
ax1.set_ylabel('$\delta\mathrm{_{smooth}}$')
# ticks
ax1.set_xticks(np.arange(0,0.051,0.025))
ax1.set_xticklabels(['0', '0.025', '0.05'])

## B ##
q = [1e-8, 1e-7, 1e-6, 1e-5, 1e-4];
d_q = np.array([3.76, 6.59, 11.7, 20.9, 37.3])*1e-3; # d = 0.005 
ax2.loglog(q, d_q, '-o', color=tableau10cb[0], markeredgecolor=tableau10cb[0])
# axes
ax2.set_xlim(1e-8, 1e-4)
ax2.set_ylim(1e-3, 1e-1)
# title and labels
ax2.set_title('$\hat{d}_\mathrm{q}$ vs $q$')
ax2.set_xlabel('$q$')
ax2.set_ylabel('$\hat{d}_\mathrm{q}$')

## C ##
filenames = ['../data/figure1/delta_vs_r__qfixed__1', '../data/figure1/delta_vs_r__qfixed__2', '../data/figure1/delta_vs_r__qfixed__3', '../data/figure1/delta_vs_r__qfixed__4']
for i in range(0,4):
    data = sio.loadmat(filenames[i])
    r =  data['r']
    d =  data['d'][0][0]
    delta_smooth = data['delta_smooth_vector']
    if i >= 3:
        ax3.plot(r, delta_smooth, '-o', color=tableau10cb[i], markeredgecolor=tableau10cb[i], label=str(d))
    else:
        ax3.plot(r, delta_smooth, '-', color=tableau10cb[i], markeredgecolor=tableau10cb[i], label=str(d))
leg = ax3.legend(frameon=0, fontsize='x-small')
leg.set_title('$\hat{d}$', prop={'size':'small'})
# axes
ax3.set_xlim(0, 0.3)
ax3.set_ylim(-0.05, 1)
ax3.set_yticks([0,1])
# dotted line
ax3.axvline(x=4.45e-2, ymax=0.525, color='k', ls=':')
ax3.axhline(y=0.5, xmax=0.148, color='k', ls=':')
# title and labels
ax3.set_title('$\delta_\mathrm{smooth}$ ($q=10^{-3}$)')
ax3.set_xlabel('$\hat{r}$')
ax3.set_ylabel('$\delta\mathrm{_{smooth}}$')
# ticks
ax3.set_xticks(np.arange(0,0.31,0.15))
ax3.set_xticklabels(['0', '0.15', '0.3'])

## D ##
d = [0.001, 0.005, 0.01, 0.05, 0.1];
d_q = np.array([4.45, 6.65, 7.90, 11.7, 13.8])*1e-2; # q = 1e-3
ax4.loglog(d, d_q, '-o', color=tableau10cb[0], markeredgecolor=tableau10cb[0])
# axes
ax4.set_xlim(1e-3, 1e-1)
ax4.set_ylim(1e-2, 1)
# title and labels
ax4.set_title('$\hat{d}_\mathrm{q}$ vs $\hat{d}$')
ax4.set_xlabel('$\hat{d}$')
ax4.set_ylabel('$\hat{d}_\mathrm{q}$')

## E ##
filenames = ['../data/figure1/delta_vs_r__panelE1', '../data/figure1/delta_vs_r__panelE2']
for i in range(0,2):
    data = sio.loadmat(filenames[i])
    r =  data['r']
    d =  data['d'][0][0]
    q = data['q'][0][0]
    delta_smooth = data['delta_smooth_vector']
    if i == 0:
        ax5.plot(r, delta_smooth, '-', color=tableau10cb[i], markeredgecolor=tableau10cb[i], label='$q$ = {}\n'.format(fmt(q))+'$\hat{d}$'+' = {}'.format(fmt(d)))
    elif i == 1:
        ax5.plot(r, delta_smooth, 'o', color=tableau10cb[i], markeredgecolor=tableau10cb[i], label='$q$ = {}\n'.format(fmt(q))+'$\hat{d}$'+' = {}'.format(fmt(d)))
ax5.legend(frameon=0, fontsize='x-small')
# axes
ax5.set_xlim(0, 0.2)
ax5.set_ylim(-0.05, 1)
ax5.set_yticks([0,1])
# dotted line
ax5.axvline(x=5.6e-2, ymax=0.525, color='k', ls=':')
ax5.axhline(y=0.5, xmax=0.28, color='k', ls=':')
# title and labels
ax5.set_title('$\delta\mathrm{_{smooth}}$')
ax5.set_xlabel('$\hat{r}$')
ax5.set_ylabel('$\delta\mathrm{_{smooth}}$')

panel = np.array(['A', 'B', 'C', 'D', 'E'])
i = 0
for ax in [ax1, ax2, ax3, ax4, ax5]:
    # ABC
    if i == 1 or i == 3:
        ax.text(-0.225, 1.1, panel[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
    else:
        ax.text(-0.1, 1.1, panel[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
    # axes
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    i += 1

plt.tight_layout()
plt.savefig('figure1.pdf', dpi=300)
