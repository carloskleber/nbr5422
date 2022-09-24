% 8.5.2.4. Fator combinado de vento para cabos - Gc

h = 10:60;
GC = zeros(4,length(h));

for k=1:4
  for i=1:length(h)
    GC(k,i) = fatorVentoCabo(char('A'+k-1), h(i));
  end
end

plot(h,GC,'-',...
     'LineWidth', 2);

set(gca,'FontSize', 14);

%set(gcf,'Position', [100 100 1000 500]);

W = 6; H = 4;
set(gcf,'PaperUnits','inches')
set(gcf,'PaperOrientation','portrait');
set(gcf,'PaperSize',[H,W]);
set(gcf,'PaperPosition',[0,0,W,H]);

legend('A','B','C','D',...
       'Location', 'northwest');

xlabel('Altura do cabo {\it\fontname{serif}h} (m)',...
       'FontSize', 16);
ylabel('Fator {\it\fontname{serif}G_C}',...
       'FontSize', 16);

grid on;
grid minor;
print(gcf, 'graficoGc.png');
