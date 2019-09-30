from fenics import *
from functions.poisson_rectangle import solvePoisson_rectangle
import numpy as np
import scipy.io as sio
from functions.fenics2nparray import *
import matplotlib.pyplot as plt

resolution = 900

corners = [[0, 0], [4, 3]]
vessel_coor = [[1, 1.1], [2.8, 0.8], [3, 2]]    	

R_star = 141.0	
M_star = 1.0e-3

r_ves = 6/R_star
p_ves = [80/(M_star*R_star**2), 70/(M_star*R_star**2), 50/(M_star*R_star**2)]
M = Constant(1)
         
p_solution, mesh = solvePoisson_rectangle(corners, vessel_coor, r_ves, p_ves, M, resolution)
mesh_coor =  mesh.coordinates()

#meshfig = plot(mesh)
#plt.show()
#fig = plot(p_solution, title="Ground truth pO2 values")
#plt.show()

d = 0.007
filename = 'data/figure8/groundTruth_twoVessel'
x = np.arange(0, 4.0001, d)
y = np.arange(0, 3.0001, d)

p_grid, r1, r2, r3 = fenics2nparray(p_solution, p_ves, r_ves, x, y, vessel_coor)

#plt.imshow(p_grid)
#plt.show()

sio.savemat(filename, {'P':p_grid, 'r1':r1, 'r2':r2, 'r3':r3, 'd_data':d, 'M_star':M_star, 'Hx_data':x, 'Hy_data':y, 'res':resolution})

