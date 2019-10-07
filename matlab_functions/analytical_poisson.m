function [P, r, H] = analytical_poisson( d_data )
% This function creates, based on the Krogh-Erlang equation, 
% a grid of pO2 values around a vessel centered in the midle of the grid.
%
% Arguments:
%   d_data (float): grid spacing
%
% Returns:
%   P (2D array): pO2 values
%   r (2D array): distances to the vessel center
%   H (1D array): x (and y) positions
%
% All input and output arguments are dimensionless.


r_star = 141.;    % [um]
M_star = 1.e-3;   % [mmHg um^-2]
r_ves = 6/r_star;
r_t = 200/r_star;
p_ves = 80/(M_star*r_star^2);

N = ceil(2/d_data)+1; 
if mod(N,2) == 0
    N = N+1;
end
L = (N-1)*d_data;
H = 0:d_data:L;
[X, Y] = meshgrid(H, H);
x0 = L/2.0; y0 = L/2.0;
r = sqrt( (X - x0).^2 + (Y - y0).^2 );
r(r < r_ves) = r_ves;

P = p_ves + 0.25 * (r.^2 - r_ves^2) - 0.5 * r_t^2 * log(r ./ r_ves);

end