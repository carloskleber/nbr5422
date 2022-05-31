%Figura X?

L = 200:800;
GL = zeros(1,length(L));

for i=1:length(L)
   GL(i) = fatorVentoVao(L(i));
end

plot(L,GL,'-',
     'LineWidth',2);
grid on;
grid minor;
