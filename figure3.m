clear all
close all
addpath('functions')

d_data = 0.007;
d_q = 0.08;
d_est = 0.001;
sigma = 0.0005;
N = 10^4;

bias(d_data, d_est, d_q, 'data/figure3/bias.mat')       
std(d_data, d_est, d_q, sigma, N, 'data/figure3/std.mat')
rmse('data/figure3/bias', 'data/figure3/std', 'data/figure3/rmse')
        
load chirp
sound(y,Fs)