% Comparação dos valores kafl (seção 4.8.4.1)
% Utilizado para demonstrar a variação de kafl, visto que seu uso para calcular o espaçamento
% também é um parâmetro de entrada.
clear all;

d = 1:0.2:10;
t = 0:5:40;
p = 995:5:1015;
figure;
for i=1:length(t)
  for j=1:length(p)
    dr = dra(p(j), t(i));
    h = umidAbs(dr, t(i));
    kafl = fatorAtmFrenteLenta(dr, h, d);
    plot(d,kafl,'LineWidth', 2);
    hold on;
  end
end
set(gca,'FontSize', 14);
W = 6; H = 4;
set(gcf,'PaperUnits','inches')
set(gcf,'PaperOrientation','portrait');
set(gcf,'PaperSize',[H,W]);
set(gcf,'PaperPosition',[0,0,W,H]);
hold off;
xlabel('Distância no ar (m)',...
       'FontSize', 16);
ylabel('Fator k_{afl}',...
       'FontSize', 16, 'interpreter', 'tex');
