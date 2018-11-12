clear all
close all
addpath('functions')

% A
d_data = 1;
sigma = 0;
seed = 1;
filename = 'data/figure2/figure2_a';
generatedata_figure2_1D(d_data, sigma, seed, filename)

% B
d_data = 1;
sigma = 0.25;
seed = 1;
filename = 'data/figure2/figure2_b';
generatedata_figure2_1D(d_data, sigma, seed, filename)

% CD
d_data = 0.007;
sigma = 0;
seed = 1;
filename = 'data/figure2/figure2_cd';
generatedata_figure2_2D_nosmoothing(d_data, sigma, seed, filename)

% EF
d_data = 0.007;
sigma = 0.013;
seed = 1;
filename = 'data/figure2/figure2_ef';
generatedata_figure2_2D_nosmoothing(d_data, sigma, seed, filename)

% GH
d_data = 0.007;
d_est = 0.001;
d_q = 0.09;
sigma = 0.013;
seed = 1;
filename = 'data/figure2/figure2_gh';
generatedata_figure2_2D_smoothing(d_data, d_est, d_q, sigma, seed, filename)