clear all
close all
addpath('functions')

d_data = 0.07;
d_est = 0.001;
seed = 1;
sigma = 0.1;

[P, r_data, H_data] = analytical_poisson(d_data);
rng(seed);
P_noisy = normrnd(P, sigma);          

save('data/figure9/figure9', 'P_noisy', 'r_data', 'H_data', ...
    'd_data', 'sigma', 'seed')
