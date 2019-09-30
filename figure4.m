clear all
close all
addpath('functions')

d_values = [0.0035, 0.007, 0.014];
dq_values = [0.0, 0.02, 0.04];
letters = 'abcdefghi';
d_est = 0.001;

k = 1;
for d_data = d_values
    for d_q = dq_values        
        filename = ['data/figure4/bias_', num2str(letters(k)), '.mat'];
        bias(d_data, d_est, d_q, filename)        
        k = k+1;
    end
end

%load chirp
%sound(y,Fs)