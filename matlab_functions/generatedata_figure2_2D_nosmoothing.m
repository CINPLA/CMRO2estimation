function [] = generatedata_figure2_2D_nosmoothing(d_data, sigma, seed, filename)
% Creates a 2D pO2 dataset, calculates its Laplacian, and writes to file.
% 
% Arguments:
%   d_data (float): spatial spacing
%   sigma (float): used to generate noisy data with normrnd(P, noise)
%   seed (int)
%   filename (str): name of output file   

[P, r_data, H_data] = analytical_poisson(d_data);

rng(seed);
P = normrnd(P, sigma);
del2P = 4*del2(P, d_data);

save(filename, 'P', 'del2P', 'r_data', 'H_data', 'd_data', 'sigma', 'sigma')
end

