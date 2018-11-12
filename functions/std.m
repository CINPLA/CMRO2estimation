function [ ] = std(d_data, d_est, d_q, sigma, N, filename)
% Standard deviation Equation 15
%
% Arguments:
%   d_data: spatial spacing of model data
%   d_est: spatial spacing of estimated data
%   d_q: smoothing length
%   sigma: used to generate noisy data with normrnd(P, noise)
%   N (int): number of trials
%   filename (str): name of output file   

q = calculate_q(d_data, d_q);
p = 1-q;

[P, ~, H_data] = analytical_poisson(d_data);
H_est = min(H_data):d_est:max(H_data);

HH = length(H_est);
pixel_sum = zeros(HH, HH);
variance_sum = zeros(HH, HH);

for s = 1:N
    rng(s);
    P_noisy = normrnd(P, sigma);
    P_smooth = csaps({H_data, H_data}, P_noisy, p, {H_est, H_est});
    del2P = 4*del2(P_smooth, d_est);         
    pixel_sum = pixel_sum + del2P;    
end
    pixel_average = pixel_sum./N;

for s = 1:N
    rng(s);
    P_noisy = normrnd(P, sigma);          
    P_smooth = csaps({H_data, H_data}, P_noisy, p, {H_est, H_est});
    del2P = 4*del2(P_smooth, d_est);         
    variance_sum = variance_sum + (del2P-pixel_average).^2;    
end
 
variance = variance_sum./N;
scaled_std = 100*sqrt(variance);

save(filename, 'scaled_std', 'd_data', 'd_est', 'd_q', 'sigma', 'q', 'H_data', 'H_est', 'N')
end