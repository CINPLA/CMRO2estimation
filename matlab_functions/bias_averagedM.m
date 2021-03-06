function [] = bias_averagedM(d_data, d_est, filename)
% Bias of spatially averaged M (as a function of d_q 
% for different values of d_cut) calculated from Equation 14.
%
% Arguments: 
%   d_data (float): grid spacing of input data
%   d_est (float): grid spacing of output data
%   filename (str): name of output file 

dq_values = [0:0.01:0.2];
dcut_values = [0.1, 0.2, 0.3, 0.4, 0.5];

M = length(dq_values);

scaled_bias_1 = zeros(1,M);
scaled_bias_2 = zeros(1,M);
scaled_bias_3 = zeros(1,M);
scaled_bias_4 = zeros(1,M);
scaled_bias_5 = zeros(1,M);

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
    P_smooth = csaps({H_data, H_data}, P, p, {H_est, H_est});       
    del2P = 4*del2(P_smooth, d_est);                         
    
    bias_1 = mean(del2P(r_est > dcut_values(1))) - 1;
    bias_2 = mean(del2P(r_est > dcut_values(2))) - 1;
    bias_3 = mean(del2P(r_est > dcut_values(3))) - 1;
    bias_4 = mean(del2P(r_est > dcut_values(4))) - 1;
    bias_5 = mean(del2P(r_est > dcut_values(5))) - 1;  
       
    scaled_bias_1(i) = 100*bias_1;
    scaled_bias_2(i) = 100*bias_2;
    scaled_bias_3(i) = 100*bias_3;
    scaled_bias_4(i) = 100*bias_4;
    scaled_bias_5(i) = 100*bias_5;
end

save(filename, 'scaled_bias_1', ...
    'scaled_bias_2', ...
    'scaled_bias_3', ...
    'scaled_bias_4', ...
    'scaled_bias_5', ...
    'dq_values',  'dcut_values', 'd_data', 'd_est')
end

