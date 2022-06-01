%Figura X?

L = 200:800;
GL = zeros(1,length(L));

for i=1:length(L)
   GL(i) = fatorVentoVao(L(i));
end

plot(L,GL,'-',...
     'LineWidth', 2);

set(gca,'FontSize', 16);

set(gcf,'Position', [100 100 1000 500]);

xlabel('Comprimento do vão (L, em metros)',...
       'FontSize', 24);
ylabel('Fator Gl',...
       'FontSize', 24);

grid on;
grid minor;
