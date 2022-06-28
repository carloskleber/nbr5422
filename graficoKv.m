%Figura X?

v = 0:0.1:50;
k = zeros(1,length(v));

for i=1:length(v)
   k(i) = fatorEfetividadeVento(v(i));
end

plot(v,k,'-',...
     'LineWidth', 2);

set(gca,'FontSize', 14);

%set(gcf,'Position', [100 100 1000 500]);

W = 6; H = 4;
set(gcf,'PaperUnits','inches')
set(gcf,'PaperOrientation','portrait');
set(gcf,'PaperSize',[H,W]);
set(gcf,'PaperPosition',[0,0,W,H]);

xlabel('Velocidade do Vento de Projeto {\it\fontname{serif}V_P} (m/s)',...
       'FontSize', 16);
ylabel('Fator de Efetividade {\it\fontname{serif}K_v}',...
       'FontSize', 16);

xlim([10 35]);
ylim([0.0 1.0]);

grid on;
grid minor;
print(gcf, 'graficoKv.png');
