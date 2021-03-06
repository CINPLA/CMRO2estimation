from fenics import *
from python_functions.poisson_rectangle import solve_poisson_rectangle
import numpy as np
import scipy.io as sio
from python_functions.fenics2nparray import fenics2nparray
import matplotlib.pyplot as plt

resolution = 900

corners = [[0, 0], [2, 2]]
vessel_coor = [[1, 1]]    	

R_star = 141.0	
M_star = 1.0e-3

r_ves = 6/R_star
p_ves = [80/(M_star*R_star**2)]
M = Expression("2-1.5*( (pow((x[1]-1),2) + pow((x[0]-1),2)) > 0.7 )", degree=4)
         
p_solution, mesh = solve_poisson_rectangle(corners, vessel_coor, r_ves, p_ves, M, resolution)
mesh_coor =  mesh.coordinates()

#meshfig = plot(mesh)
#plt.show()
#fig = plot(p_solution, title="Ground truth pO2 values")
#plt.show()

d = 0.007
filename = 'data/figure7/ground_truth_varying_M.mat'
x = np.arange(0, 2.0001, d)
y = np.arange(0, 2.0001, d)

p_grid, r1 = fenics2nparray(p_solution, p_ves, r_ves, x, y, vessel_coor)

#plt.imshow(p_grid)
#plt.show()

sio.savemat(filename, {'P':p_grid, 'r':r1, 'd_data':d, 'M_star':M_star, 'Hx_data':x, 'Hy_data':y, 'res':resolution})
