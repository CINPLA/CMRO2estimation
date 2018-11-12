function [] = averagedM_trial(d_data, d_est, sigma, seed, filename)
% Calcaulates spatially-averaged M as a function of d_q
% for a specific trial (seed).
%
% Arguments:
%   d_data: spatial spacing of model data
%   d_est: spatial spacing of estimated data
%   sigma: used to generate noisy data with normrnd(P, noise)
%   seed (int)
%   filename (str): name of output file   

dq_values = [0:0.01:0.25 0.3 0.4 0.5];
dcut_values = [0.14, 0.21, 0.28, 0.35, 0.42, 0.49];

M = length(dq_values);

estimates_1 = zeros(1,M);
estimates_2 = zeros(1,M);
estimates_3 = zeros(1,M);
estimates_4 = zeros(1,M);
estimates_5 = zeros(1,M);
estimates_6 = zeros(1,M);

[P, ~, H_data] = analytical_poisson(d_data);
H_est = min(H_data):d_est:max(H_data);
[X, Y] = meshgrid(H_est, H_est);
x0 = max(H_data)/2.0; y0 = max(H_data)/2.0;
r_est = sqrt( (X - x0).^2 + (Y - y0).^2 );
r_ves = 6/141;
r_est(r_est < r_ves) = r_ves;

for i = 1:M
    d_q = dq_values(i);   
    q = calculate_q(d_data, d_q);
    p = 1-q;
        
    rng(seed);
    P_noisy = normrnd(P, sigma);          
    P_smooth = csaps({H_data, H_data}, P_noisy, p, {H_est, H_est});       
    del2P = 4*del2(P_smooth, d_est);                 

    estimates_1(i) = mean(del2P(r_est > dcut_values(1)));
    estimates_2(i) = mean(del2P(r_est > dcut_values(2)));
    estimates_3(i) = mean(del2P(r_est > dcut_values(3)));
    estimates_4(i) = mean(del2P(r_est > dcut_values(4)));
    estimates_5(i) = mean(del2P(r_est > dcut_values(5)));
    estimates_6(i) = mean(del2P(r_est > dcut_values(6)));    
    
end

save(filename, 'estimates_1', 'estimates_2', 'estimates_3', ...
    'estimates_4', 'estimates_5', 'estimates_6', ...
    'dq_values',  'dcut_values', 'd_data', 'd_est', 'sigma', 'seed')
end

