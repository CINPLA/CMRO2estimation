clear all
close all
addpath('matlab_functions')

% A
d_data = 1;
sigma = 0;
seed = 1;
filename = 'data/figure2/figure2_a';
generatedata_figure2_1D(d_data, sigma, seed, filename)

% CD
d_data = 0.007;
sigma = 0;
seed = 1;
filename = 'data/figure2/figure2_bc';
generatedata_figure2_2D_nosmoothing(d_data, sigma, seed, filename)

% EF
d_data = 0.007;
sigma = 0.0005;
seed = 1;
filename = 'data/figure2/figure2_def';
generatedata_figure2_2D_nosmoothing(d_data, sigma, seed, filename)

% GH
d_data = 0.007;
d_est = 0.001;
d_q = 0.04;
sigma = 0.0005;
seed = 1;
filename = 'data/figure2/figure2_gh';
generatedata_figure2_2D_smoothing(d_data, d_est, d_q, sigma, seed, filename)