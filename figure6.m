% To be able to run this code you must first run figure4.m and figure5.m.

clear all
close all
addpath('matlab_functions')

letters = 'abcdefghi';

for letter = letters
    rmse(['data/figure4/bias_', letter], ...
        ['data/figure5/std_', letter], ...
        ['data/figure6/rmse_', letter])
end