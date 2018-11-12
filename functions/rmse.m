function [] = generatedata_rmse(filename_bias, filename_std, filename_rmse)
% Root mean squre error Equation 16
%
% Arguments:
%   filename_bias (str): created by running figure4.m
%   filename_std (str): created by running figure5.m
%   filename_rmse (str): name of output file

load(filename_std)
load(filename_bias)

bias = scaled_bias/100;
variance = (scaled_std/100).^2;
mse = variance + bias.^2;
rmse = sqrt(mse);
scaled_rmse = rmse*100;

save(filename_rmse, 'scaled_rmse', 'd_data', 'd_est', 'd_q', 'sigma', 'q', 'H_data', 'H_est', 'N')

end