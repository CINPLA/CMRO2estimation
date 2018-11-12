function [] = generatedata_Figure6_smoothing(inputfile, d_est, d_q, noise_sigma, outputfile)

load(inputfile);
Hx_est = min(Hx):d_est:max(Hx);
Hy_est = min(Hy):d_est:max(Hy);

%rng(seed);
P_noisy = normrnd(P, noise_sigma);

q = calculate_q(d, d_q);
p = 1-q;
P_smooth = csaps({Hy, Hx}, P_noisy, p, {Hy_est, Hx_est});

del2P = 4*del2(P_smooth, d_est);

Hx_data = Hx;
Hy_data = Hy;
d_data = d;
save(outputfile, 'P_noisy', 'P_smooth', 'del2P', 'Hx_est', 'Hy_est', 'Hx_data', 'Hy_data', ...
    'd_data', 'd_est', 'd_q', 'noise_sigma')
end

