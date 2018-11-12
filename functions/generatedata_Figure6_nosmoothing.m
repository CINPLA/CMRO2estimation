function [] = generatedata_Figure6_nosmoothing(inputfile, noise_sigma, outputfile)

load(inputfile)

%rng(seed);
P = normrnd(P, noise_sigma);
del2P = 4*del2(P, d);

Hx_data = Hx;
Hy_data = Hy;
d_data = d;

save(outputfile, 'P', 'del2P', 'Hx_data', 'Hy_data', 'd_data', 'noise_sigma')
end

