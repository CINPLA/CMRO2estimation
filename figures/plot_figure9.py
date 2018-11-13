# This code creates Figure 9. 
# To be able to run this code you must download the data folder
# or run figure9.m.

import scipy.io as sio
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm
from set_style import set_style

set_style('article', w=0.5, h=1)

data = sio.loadmat('../data/figure9/figure9')
x = data['H_data'][0]
y = data['H_data'][0]
X, Y = np.meshgrid(x, y)
Z = data['P_noisy']
r = data['r_data']
levels = np.arange(0,4.26,0.1)
cmap = cm.Reds
cset = plt.contourf(X, Y, Z, levels, cmap='Reds')
plt.colorbar(ticks=np.arange(0,4.1,1))
# dcut
plt.contour(X, Y, r, [0.21, 0.35, 0.49], colors='black')

# axes
plt.axes().set_aspect('equal')
plt.yticks(np.arange(max(y)/2-1, max(y)/2+1.01, 0.5), ('-1', '-0.5', '0', '0.5', '1'))
plt.xlabel('$\hat{x}$')
plt.ylabel('$\hat{y}$')
plt.xticks(np.arange(max(x)/2-1, max(x)/2+1.01, 0.5), ('-1', '-0.5', '0', '0.5', '1'))
plt.yticks(np.arange(max(y)/2-1, max(y)/2+1.01, 0.5), ('-1', '-0.5', '0', '0.5', '1'))
plt.xlabel('$\hat{x}$')
plt.ylabel('$\hat{y}$')

plt.title('$\hat{P}+\hat{P}_\sigma$')

plt.savefig('figure9.pdf', bbox_inches="tight", dpi=300)
