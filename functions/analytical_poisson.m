function [P, r, H] = analytical_poisson( d_data )
% P = P_ves if r < Rves
% P = P_ves + 0.25 * M * (r^2 - R_ves^2) - 0.5 * M * R_t^2 * ln(r / R_ves)
% if r >= R_ves
%
% All parameters are dimensionless.

r_star = 141.; % [um]
M_star = 1.e-3; %[mmHg um^-2]
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