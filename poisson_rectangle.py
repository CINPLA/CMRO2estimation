from fenics import *
from mshr import *
import numpy as np
import scipy.io as sio
from fenics2nparray import *
import matplotlib.pyplot as plt

def solvePoisson_rectangle(corners, hole_coor, r_hole, hole_boundary_value, M, resolution):
    """
    Solves the Poissons equtaion
    nabla**2 p = M
    on a rectangle mesh with one to three holes.

    Boundary conditions:
	    dp/dr = 0 at outer boundaries
	    p = hole_boundary_value at hole boundaries

    Arguments:
	    corners (array): mesh corners coordinates
	    r_hole (int): hole radius
	    hole_boundary_value (array): value of p at hole boundaries
	    M (float): constant
	    resolution (int): resolution of fenics mesh

    Returns:
	    p_solution (fenics solution)
	    mesh (fenics mesh)
    """

    r = Rectangle(Point(corners[0][0],corners[0][1]), Point(corners[1][0],corners[1][1]))
    domain = r
    for i in range(len(hole_coor)):
        hole = Circle(Point(hole_coor[i][0], hole_coor[i][1]), r_hole)
        domain = domain - hole

    mesh = generate_mesh(domain, resolution)

    V = FunctionSpace(mesh, 'CG', 1)

    p = TrialFunction(V)
    v = TestFunction(V)
    form = (inner(nabla_grad(p), nabla_grad(v)) + M*v )*dx
    (a,L) = system(form)

    def boundary1(x, on_boundary):
        r = np.sqrt((x[0]-hole_coor[0][0])**2 + (x[1]-hole_coor[0][1])**2)
        b = ((r < r_hole+0.5) and on_boundary)
        return b
    bc1 = DirichletBC(V, hole_boundary_value[0], boundary1)
    bcs = [bc1]

    if len(hole_coor)>1:
        def boundary2(x, on_boundary):
            r = np.sqrt((x[0]-hole_coor[1][0])**2 + (x[1]-hole_coor[1][1])**2)
            b = ((r < r_hole+0.5) and on_boundary)
            return b
        bc2 = DirichletBC(V, hole_boundary_value[1], boundary2)
        bcs.append(bc2)

    if len(hole_coor)==3:
        def boundary3(x, on_boundary):
            r = np.sqrt((x[0]-hole_coor[2][0])**2 + (x[1]-hole_coor[2][1])**2)
            b = ((r < r_hole+0.5) and on_boundary)
            return b
        bc3 = DirichletBC(V, hole_boundary_value[2], boundary3)
        bcs.append(bc3)

    p_solution = Function(V)
    solve(a==L, p_solution, bcs)

    return p_solution, mesh


if __name__ == "__main__":

    resolution = 900

    corners = [[0, 0], [2, 2]]
    centre = 1
    hole_coor = [[0.75, 0.75], [1.25, 1.25]]

    R_star = 141.0
    M_true = 1.0e-3

    r_ves = 6/R_star
    p_ves = [80/(M_true*R_star**2), 80/(M_true*R_star**2)]
    M = 1

    p_solution, mesh = solvePoisson_rectangle(corners, hole_coor, r_ves, p_ves, M, resolution)
    mesh_coor =  mesh.coordinates()

    meshfig = plot(mesh)
    plt.show()
    fig = plot(p_solution, title="Ground truth pO2 values")
    plt.show()

    d = 0.007
    filename = 'TwoVessel_groundTruth'
    x = np.arange(0, 2.0001, d)
    y = np.arange(0, 2.0001, d)

    p_grid, r1, r2 = fenics2nparray(p_solution, p_ves[0], x, y, hole_coor) # + r2 if two holes

    plt.imshow(p_grid)
    plt.show()

    sio.savemat(filename, {'P':p_grid, 'r1':r1, 'r2':r2, 'd':d, 'M_true':M, 'Hx':x, 'Hy':y, 'res':resolution}) # two holes
    #sio.savemat(filename, {'P':p_grid, 'r':r1, 'd':d[i], 'M_true':M, 'Hx':x, 'Hy':y, 'res':resolution}) # one hole
