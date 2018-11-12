clear all
close all
addpath('functions')

figure(1)
hold on

q = 5e-4;
d = 0.005;
[delta_smooth_vector, r] = delta_smooth(d, q);
save('data/figure1/delta_vs_r__panelE1', 'd', 'q', 'delta_smooth_vector', 'r')    
plot(r, delta_smooth_vector, '-o', 'MarkerSize', 2);

q = 2.56e-4;
d = 1e-2;
[delta_smooth_vector, r] = delta_smooth(d, q);
save('data/figure1/delta_vs_r__panelE2', 'd', 'q', 'delta_smooth_vector', 'r')    
plot(r, delta_smooth_vector, '-o', 'MarkerSize', 2);


title('Normalized $\delta_\mathrm{{smooth}}$ as a function of $\hat{r}$', 'Interpreter', 'Latex')
set(gca, 'fontsize', 16)
xlim([0,0.2]); ylim([-0.05, 1])
set(gca,'XMinorTick','on'); set(gca,'YMinorTick','on')
xlabel('$\hat{r}$', 'Interpreter', 'Latex'); ylabel('$\delta_\mathrm{{smooth}}$', 'Interpreter', 'Latex')
l = line([0,1], [0.5 0.5], 'Displayname', 'ref'); l.Color = 'k'; l.LineStyle = ':';
ax = gca; ax.XMinorGrid = 'on';