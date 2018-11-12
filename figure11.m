clear all
close all
addpath('functions')

d_data = 0.07;
d_est = 0.001;

sigma = [0.025, 0.025, 0.025, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4];
letters = 'abcdefghi';

for i = 1:9
    averagedM_trial(d_data, d_est, sigma(i), i, ...
        ['data/figure11/figure11', letters(i)])
end