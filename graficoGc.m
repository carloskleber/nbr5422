%Figura X?

h = 10:60;
GC = zeros(4,length(h));

for k=1:4
  for i=1:length(h)
    GC(k,i) = fatorVentoCabo(char('A'+k-1), h(i));
  end
end

plot(h,GC,'-',
     'LineWidth', 2);

set(gca,'FontSize', 16);

set(gcf,'Position', [100 100 1000 500]);

legend('A','B','C','D',
       'Location', 'northwest');

xlabel('Altura do condutor (H, em metros)',
       'FontSize', 24);
ylabel('Fator Gc',
       'FontSize', 24);

grid on;
grid minor;
