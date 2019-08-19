clear all
close all
addpath('functions')

d_data = 0.035;
d_est = 0.001;
N = 1000;

bias_averagedM(d_data, d_est, 'data/figure9/figure9_a')

sigma = 0.0005;
d_q = 0;
bias(d_data, d_est, d_q, 'data/figure9/spatial_bias_b')
std(d_data, d_est, d_q, sigma, N, 'data/figure9/spatial_std_b')
rmse('data/figure9/spatial_bias_b', 'data/figure9/spatial_std_b', 'data/figure9/figure9_b')
std_averagedM(d_data, d_est, sigma, N, 'data/figure9/figure9_c')
rmse_averagedM('data/figure9/figure9_a', 'data/figure9/figure9_c', 'data/figure9/figure9_d')

sigma = 0.05;
d_q = 0.1;
bias(d_data, d_est, d_q, 'data/figure9/spatial_bias_e')
std(d_data, d_est, d_q, sigma, N, 'data/figure9/spatial_std_e')
rmse('data/figure9/spatial_bias_e', 'data/figure9/spatial_std_e', 'data/figure9/figure9_e')
std_averagedM(d_data, d_est, sigma, N, 'data/figure9/figure9_f')
rmse_averagedM('data/figure9/figure9_a', 'data/figure9/figure9_f', 'data/figure9/figure9_g')

