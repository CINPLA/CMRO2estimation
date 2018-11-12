function [] = generatedata_figure2_1D(d_data, sigma, seed, filename)
% Creates a 1D pO2 dataset and writes to file.
% 
% Arguments:
%   d_data (um): spatial spacing
%   sigma (mmHg): used to generate noisy data with normrnd(P, noise)
%   seed
%   filename (str): name of output file   


r_t = 200;
M = 1e-3;
r_ves = 6;
p_ves = 80;

L = ceil(r_t/d_data)*d_data;
r_data = 0:d_data:L;

P = p_ves + 0.25 * M * (r_data.^2 - r_ves^2) - 0.5 * M * r_t^2 * log(r_data ./ r_ves);
P(r_data<r_ves) = p_ves;

r_data = [-1*fliplr(r_data) r_data(2:end)];
P = [fliplr(P) P(2:end)];

rng(seed);
P = normrnd(P, sigma);

save(filename, 'P', 'r_data', 'd_data', 'sigma', 'seed')
end