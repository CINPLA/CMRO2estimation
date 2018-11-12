clear all
close all
addpath('functions')

d = 0.005;
q_values = [1e-8, 1e-7, 1e-6, 1e-5, 1e-4];

figure(1)
hold on
i = 1;
for q = q_values
    [delta_smooth_vector, r] = delta_smooth(d, q);
    save(['data/figure1/delta_vs_r__dfixed__', num2str(i)], 'd', 'q', 'delta_smooth_vector', 'r')    
    plot(r, delta_smooth_vector, '-o', 'MarkerSize', 2, 'Displayname', ['q=',num2str(q)]);
    i = i + 1;
end

title('Normalized $\delta_\mathrm{{smooth}}$ as a function of $\hat{r}$', 'Interpreter', 'Latex')
legend('show')
set(gca, 'fontsize', 16)
xlim([0,0.05]); ylim([-0.05, 1])
set(gca,'XMinorTick','on'); set(gca,'YMinorTick','on')
xlabel('$\hat{r}$', 'Interpreter', 'Latex'); ylabel('$\delta_\mathrm{{smooth}}$', 'Interpreter', 'Latex')
l = line([0,1], [0.5 0.5], 'Displayname', 'ref'); l.Color = 'k'; l.LineStyle = ':';
ax = gca; ax.XMinorGrid = 'on';