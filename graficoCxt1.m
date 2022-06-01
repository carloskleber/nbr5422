%Figura X?

x = 0:0.01:1;
Cxt = zeros(1,length(x));

for i=1:length(x)
  Cxt(1,i) = fatorCxt1(x(i));
end

plot(x,Cxt,'-',
     'LineWidth', 2);

set(gca,'FontSize', 16);

set(gcf,'Position', [100 100 1000 500]);

legend('Cxt1',
       'Location', 'northeast');

xlabel('Índice de área exposta (X)',
       'FontSize', 24);
ylabel('Fator Cxt1',
       'FontSize', 24);

grid on;
grid minor;
