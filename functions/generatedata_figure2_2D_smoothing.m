function [] = generatedata_figure2_2D_smoothing(d_data, d_est, d_q, sigma, seed, filename)
% Creates a 2D pO2 dataset, smooths it,
% calculates its Laplacian, and writes to file.
% 
% Arguments:
%   d_data: spatial spacing of model data
%   d_est: spatial spacing of estimated data
%   d_q: smoothing length
%   sigma: used to generate noisy data with normrnd(P, noise)
%   seed
%   filename (str): name of output file   

[P, ~, H_data] = analytical_poisson(d_data);
H_est = min(H_data):d_est:max(H_data);

rng(seed);
P = normrnd(P, sigma);

q = calculate_q(d_data, d_q);
p = 1-q;
P_smooth = csaps({H_data, H_data}, P, p, {H_est, H_est});

del2P = 4*del2(P_smooth, d_est);

save(filename, 'P', 'P_smooth', 'del2P', 'H_est', 'H_data', 'd_data', 'd_est', 'd_q', 'sigma', 'sigma')
end

