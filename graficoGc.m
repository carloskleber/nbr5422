%Figura X?

h = 10:60;
GC = zeros(4,length(h));

for k=1:4
  for i=1:length(h)
    GC(k,i) = fatorVentoCabo(char('A'+k-1), h(i));
  end
end

plot(h,GC,'-',
     'LineWidth',2);
legend('A','B','C','D',
       'Location','northwest');
grid on;
grid minor;
