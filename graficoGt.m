% 8.6.3. Fator combinado de vento para suportes e cadeias de isoladores - Gt
clear all;

h = 10:60;
GT = zeros(4,length(h));

for k=1:4
  for i=1:length(h)
    GT(k,i) = fatorVentoSuporte(char('A'+k-1), h(i));
  end
end

plot(h,GT,'-','LineWidth', 2);
set(gca,'FontSize', 14);
%set(gcf,'Position', [100 100 1000 500]);
W = 6; H = 4;
set(gcf,'PaperUnits','inches')
set(gcf,'PaperOrientation','portrait');
set(gcf,'PaperSize',[H,W]);
set(gcf,'PaperPosition',[0,0,W,H]);

legend('A','B','C','D',...
       'Location', 'eastoutside');

xlabel('Altura do condutor {\it\fontname{serif}h} (m)',...
       'FontSize', 16);
ylabel('Fator {\it\fontname{serif}G_t}',...
       'FontSize', 16, 'interpreter', 'tex');

grid on;
grid minor;
% Testes de formato
%saveas(gcf, 'graficoGt.pdf');
%print(gcf, 'graficoGt.svg');
print(gcf, 'graficoGt.png');
