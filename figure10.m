clear all
close all
addpath('functions')

d_data = 0.07;
d_est = 0.001;
filename = 'data/figure10/figure10_a';
bias_averagedM(d_data, d_est, filename)

N = 1000;
sigma = 0.025;
filename = 'data/figure10/figure10_b';
std_averagedM(d_data, d_est, sigma, N, filename)

sigma = 0.1;
filename = 'data/figure10/figure10_d';
std_averagedM(d_data, d_est, sigma, N, filename)

sigma = 0.4;
filename = 'data/figure10/figure10_f';
std_averagdeM(d_data, d_est, sigma, N, filename)

rmse_averagedM('data/figure10/figure10_a', 'data/figure10/figure10_b', 'data/figure10/figure10_c')
rmse_averagedM('data/figure10/figure10_a', 'data/figure10/figure10_d', 'data/figure10/figure10_e')
rmse_averagedM('data/figure10/figure10_a', 'data/figure10/figure10_f', 'data/figure10/figure10_g')