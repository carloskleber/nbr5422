function kafl = fatorAtmFrenteLenta(dra, hc, d)
% FATORATMFRENTELENTA Fator de correcao atmosferico para impulsos de frente
% lenta
%  Formulas 11, 12, 13
if (d <= 3.5)
  g0 = 1080/(500 * d) * log(0.46 * d + 1);
else
  g0 = 3400 / (500 * d + 4000);
end
m2 = 1.25 * g0*(g0 - 0.2);
kafl = dra^m2 * hc^m2;
end

