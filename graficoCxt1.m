% 8.8.2.4 - Coeficiente de arrasto para suporte trelicado por perfis planos (Figura 19)

x = 0:0.01:1;
Cxt = zeros(1,length(x));

for i=1:length(x)
  Cxt(1,i) = fatorCxt1(x(i));
end

plot(x,Cxt,'-',...
     'LineWidth', 2);

set(gca,'FontSize', 14);

%set(gcf,'Position', [100 100 1000 500]);
W = 6; H = 4;
set(gcf,'PaperUnits','inches')
set(gcf,'PaperOrientation','portrait');
set(gcf,'PaperSize',[H,W]);
set(gcf,'PaperPosition',[0,0,W,H]);

xlabel('Índice da área exposta {\it\fontname{serif}X}',...
       'FontSize', 16);
ylabel('{\it\fontname{serif}C_{x}}',...
       'FontSize', 16);

grid on;
grid minor;
print(gcf, 'graficoCxt1.png');
