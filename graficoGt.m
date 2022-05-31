%Figura X?

h = 10:60;
GT = zeros(4,length(h));

for k=1:4
  for i=1:length(h)
    GT(k,i) = fatorVentoSuporte(char('A'+k-1), h(i));
  end
end

plot(h,GT,'-',
     'LineWidth', 2);

set(gca,'FontSize', 16);

set(gcf,'Position', [100 100 1000 500]);

legend('A','B','C','D',
       'Location', 'northwest');

xlabel('Altura do condutor (H, em metros)',
       'FontSize', 24);
ylabel('Fator Gt',
       'FontSize', 24);

grid on;
grid minor;
