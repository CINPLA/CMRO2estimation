function [ ] = bias(d_data, d_est, d_q, filename)
% Bias calculated from Equation 14.
%
% Arguments:
%   d_data (float): grid spacing of input data
%   d_est (float): grid spacing of output data
%   d_q (float): smoothing length
%   filename (str): name of output file   

q = calculate_q(d_data, d_q);
p = 1-q;

[P, ~, H_data] = analytical_poisson(d_data);
H_est = min(H_data):d_est:max(H_data);

P_smooth = csaps({H_data, H_data}, P, p, {H_est, H_est});
del2P = 4*del2(P_smooth, d_est);         

bias = del2P-1;    
scaled_bias = 100*bias;

save(filename, 'scaled_bias', 'd_data', 'd_est', 'd_q', 'H_data', 'H_est')
end