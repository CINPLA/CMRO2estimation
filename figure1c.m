clear all
close all
addpath('functions')

q = 1e-3;
d_values = [0.001, 0.005, 0.01, 0.05, 0.1];

figure(2)
hold on
i = 1;
for d = d_values   
    [delta_smooth_vector, r] = delta_smooth(d, q);   
    save(['data/figure1/delta_vs_r__qfixed__', num2str(i)], 'd', 'q', 'delta_smooth_vector', 'r')    
    plot(r, delta_smooth_vector, '-o', 'MarkerSize', 2, 'Displayname', ['d=',num2str(d)]);
    i = i + 1;
end

title('Normalized $\delta_\mathrm{{smooth}}$ as a function of $\hat{r}$', 'Interpreter', 'Latex')
legend('show')
set(gca, 'fontsize', 16);
xlim([0,0.3]); ylim([-0.05, 1])
set(gca,'XMinorTick','on'); set(gca,'YMinorTick','on')
xlabel('$\hat{r}$', 'Interpreter', 'Latex'); ylabel('$\delta_\mathrm{{smooth}}$', 'Interpreter', 'Latex')
l = line([0,1], [0.5 0.5], 'Displayname', 'ref'); l.Color = 'k'; l.LineStyle = ':';
ax = gca; ax.XMinorGrid = 'on';
