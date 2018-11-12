function [q] = calculate_q(d_data, d_q)
% Calculates the smoothing factor q given the spatial spacing d_data and
% smoothing length d_q. Equation 13.

q = ((d_q/1.4)^4)/d_data;

end

