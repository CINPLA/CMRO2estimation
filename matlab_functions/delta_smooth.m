function [delta_smooth_vector, r] = delta_smooth(d, q)
% Smooths a square single-entry matrix with one as the
% middle element and the rest of the elements set to zero. 
% 
% Arguments:
%   d (float): grid spacing
%   q (float): smoothing factor
%
% Returns:
%   delta_smooth_vector (vector)
%   r (vector): radial distance vector

p = 1-q;
[delta_matrix, r, H] = delta(d);
[r, I] = sort(r(:));
delta_smoothed = csaps({H, H}, delta_matrix, p, {H, H});
delta_smooth_vector = delta_smoothed(:);
delta_smooth_vector = delta_smooth_vector(I);    
delta_smooth_vector = delta_smooth_vector./delta_smooth_vector(1);

end

