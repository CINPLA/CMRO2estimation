clear all
close all
addpath('functions')

sigma = 0.013;
d_est = 0.001;
d_q = 0.09;
seed = 1;

load('data/figure7/groundTruth_varyingM.mat')
Hx_est = min(Hx_data):d_est:max(Hx_data);
Hy_est = min(Hy_data):d_est:max(Hy_data);

del2P_panelC = 4*del2(P, d_data);

rng(seed);
P_noisy = normrnd(P, sigma);
q = calculate_q(d_data, d_q);
p = 1-q;
P_smooth = csaps({Hy_data, Hx_data}, P_noisy, p, {Hy_est, Hy_est});
del2P_panelD = 4*del2(P_smooth, d_est);

save('data/figure7/figure7', 'P', 'P_noisy', 'del2P_panelC', 'del2P_panelD', ...
    'd_data', 'd_est', 'sigma', 'd_q', 'seed', 'Hx_data', 'Hy_data', ...
    'Hx_est', 'Hy_est')