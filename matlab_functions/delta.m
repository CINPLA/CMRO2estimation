function [delta_matrix, r, H] = delta( d )
% Creates a square single-entry matrix 'delta_matrix' with one as the
% middle element and the rest of the elements set to zero. 
% 
% Arguements: 
%   d (float): grid spacing
%
% Returns: 
%   delta_matrix (matrix)
%   r (matrix): radial position matrix
%   H (vector): position vector

N = ceil(2/d)+1; 
if mod(N,2) == 0
    N = N+1;
end
L = (N-1)*d;
H = 0:d:L;
[X, Y] = meshgrid(H, H);
x0 = L/2.0; y0 = L/2.0;
r = sqrt( (X - x0).^2 + (Y - y0).^2 );
delta_matrix = zeros(size(r));
delta_matrix(ismembertol(r, 0, 1e-15)) = 1;

end
