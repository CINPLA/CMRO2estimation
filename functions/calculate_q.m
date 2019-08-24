function [q] = calculate_q(d_data, d_q)
% Calculates the smoothing factor q from Equation 13
% given the grid spacing d_data and the smoothing length d_q.

q = ((d_q/1.4)^4)/d_data;

end

