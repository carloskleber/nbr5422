%Figura X?

L = 200:800;
GL = zeros(1,length(L));

for i=1:length(L)
   GL(i) = fatorVentoVao(L(i));
end

plot(L,GL,'-',...
     'LineWidth', 2);

set(gca,'FontSize', 14);

%set(gcf,'Position', [100 100 1000 500]);

W = 6; H = 4;
set(gcf,'PaperUnits','inches')
set(gcf,'PaperOrientation','portrait');
set(gcf,'PaperSize',[H,W]);
set(gcf,'PaperPosition',[0,0,W,H]);

xlabel('Comprimento do vão {\it\fontname{serif}L} (m)',...
       'FontSize', 16);
ylabel('Fator {\it\fontname{serif}G_L}',...
       'FontSize', 16);

grid on;
grid minor;
print(gcf, 'graficoGl.png');
