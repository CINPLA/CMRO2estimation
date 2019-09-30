function [] = rmse_averagedM(filename_bias, filename_std, filename_rmse)
% Root mean squre error calculated from Equation 16.
%
% Arguments:
%   filename_bias (str): created by running figure10.m
%   filename_std (str): created by running figure10.m
%   filename_rmse (str): name of output file

load(filename_std)
load(filename_bias)

bias_1 = scaled_bias_1/100;
bias_2 = scaled_bias_2/100;
bias_3 = scaled_bias_3/100;
bias_4 = scaled_bias_4/100;
bias_5 = scaled_bias_5/100;

variance_1 = (scaled_std_1/100).^2;
variance_2 = (scaled_std_2/100).^2;
variance_3 = (scaled_std_3/100).^2;
variance_4 = (scaled_std_4/100).^2;
variance_5 = (scaled_std_5/100).^2;

mse_1 = variance_1 + bias_1.^2;
mse_2 = variance_2 + bias_2.^2;
mse_3 = variance_3 + bias_3.^2;
mse_4 = variance_4 + bias_4.^2;
mse_5 = variance_5 + bias_5.^2;

rmse_1 = sqrt(mse_1);
rmse_2 = sqrt(mse_2);
rmse_3 = sqrt(mse_3);
rmse_4 = sqrt(mse_4);
rmse_5 = sqrt(mse_5);

scaled_rmse_1 = rmse_1*100;
scaled_rmse_2 = rmse_2*100;
scaled_rmse_3 = rmse_3*100;
scaled_rmse_4 = rmse_4*100;
scaled_rmse_5 = rmse_5*100;

save(filename_rmse, 'scaled_rmse_1', ...
    'scaled_rmse_2', ...
    'scaled_rmse_3', ...
    'scaled_rmse_4', ...
    'scaled_rmse_5', ...
    'd_data', 'd_est', 'dq_values', 'dcut_values', 'sigma', 'N')

end

