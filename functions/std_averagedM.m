function [] = std_averageM(d_data, d_est, sigma, N, filename)
% Standard deviation of spatially averaged M (as a function of d_q 
% for different values of d_cut). Equation 15
%
% Arguments:
%   d_data: spatial spacing of model data
%   d_est: spatial spacing of estimated data
%   sigma: used to generate noisy data with normrnd(P, noise)
%   N (int): number of trials
%   filename (str): name of output file   

dq_values = [0:0.01:0.2];
dcut_values = [0.1, 0.2, 0.3, 0.4, 0.5];

M = length(dq_values);

scaled_std_1 = zeros(1,M);
scaled_std_2 = zeros(1,M);
scaled_std_3 = zeros(1,M);
scaled_std_4 = zeros(1,M);
scaled_std_5 = zeros(1,M);

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
    estimate1_s = zeros(1,N);       
    for s = 1:N
        rng(s);
        P_noisy = normrnd(P, sigma);          
        P_smooth = csaps({H_data, H_data}, P_noisy, p, {H_est, H_est});       
        del2P = 4*del2(P_smooth, d_est);                 
        
        estimate1_s(s) = mean(del2P(r_est > dcut_values(1)));
        estimate2_s(s) = mean(del2P(r_est > dcut_values(2)));
        estimate3_s(s) = mean(del2P(r_est > dcut_values(3)));
        estimate4_s(s) = mean(del2P(r_est > dcut_values(4)));
        estimate5_s(s) = mean(del2P(r_est > dcut_values(5)));
    end    
    variance_1 = var(estimate1_s);
    variance_2 = var(estimate2_s);
    variance_3 = var(estimate3_s);
    variance_4 = var(estimate4_s);    
    variance_5 = var(estimate5_s);              
    
    scaled_std_1(i) = 100*sqrt(variance_1);
    scaled_std_2(i) = 100*sqrt(variance_2);
    scaled_std_3(i) = 100*sqrt(variance_3);
    scaled_std_4(i) = 100*sqrt(variance_4);
    scaled_std_5(i) = 100*sqrt(variance_5);
    
end

save(filename, 'scaled_std_1', ...
    'scaled_std_2', ...
    'scaled_std_3', ...
    'scaled_std_4', ...
    'scaled_std_5', ...
    'dq_values', 'dcut_values', 'd_data', 'd_est', 'sigma', 'N')
end