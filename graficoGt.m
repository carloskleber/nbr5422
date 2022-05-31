%Figura X?

h = 10:60;
GT = zeros(4,length(h));

for k=1:4
  for i=1:length(h)
    GT(k,i) = fatorVentoSuporte(char('A'+k-1), h(i));
  end
end

plot(h,GT,'-',
     'LineWidth',2);
legend('A','B','C','D',
       'Location','northwest');
grid on;
grid minor;
