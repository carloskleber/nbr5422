% Teste fator correcao atmosferico - frente lenta
close all
d = 1:0.1:30;
dra = 0.8:0.02:0.95;
h = 11;
figure
for dr1=dra
  fa = fatorAtmFrenteLenta(dr1, h, d);
  plot(d,fa)
  hold on
end

hold off
figure
h = 5:15;
dra = 0.9;
for h1=h
  fa = fatorAtmFrenteLenta(dra, h1, d);
  plot(d,fa)
  hold on
end

