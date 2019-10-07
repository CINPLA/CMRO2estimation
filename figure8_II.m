% To run this code, you must first run figure8_I.py in Python.

clear all
close all
addpath('matlab_functions')

sigma = 0.0005;
d_est = 0.001;
d_q = 0.04;
seed = 1;

load('data/figure8/groundTruth_twoVessel.mat')
Hx_est = min(Hx_data):d_est:max(Hx_data);
Hy_est = min(Hy_data):d_est:max(Hy_data);

rng(seed);
P_noisy = normrnd(P, sigma);
q = calculate_q(d_data, d_q);
p = 1-q;
P_smooth = csaps({Hy_data, Hx_data}, P_noisy, p, {Hy_est, Hx_est});
del2P = 4*del2(P_smooth, d_est);

save('data/figure8/figure8', 'P', 'P_noisy', 'P_smooth', 'del2P',...
    'd_data', 'd_est', 'sigma', 'd_q', 'seed', 'Hx_data', 'Hy_data', ...
    'Hx_est', 'Hy_est')