clear all
close all
addpath('functions')

d_values = [0.0035, 0.007, 0.014];
dq_values = [0.0, 0.02, 0.04];
letters = 'abcdefghi';
d_est = 0.001;
sigma = 0.0005;
N = 10^4;

k = 1;
for d_data = d_values
    for d_q = dq_values        
        filename = ['data/figure5/std_', num2str(letters(k)), '.mat'];        
        std(d_data, d_est, d_q, sigma, N, filename)
        k = k+1;
    end
end

%load chirp
%sound(y,Fs)