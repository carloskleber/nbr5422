function kafl = fatorAtmFrenteLenta(dra, h, d)
% FATORATMFRENTELENTA Fator de correcao atmosferico para impulsos de frente
% lenta linhas CA
%  dra - densidade relativa do ar
%  h - umidade absoluta do ar em g/m3
%  d - espaçamento no ar em m
hc = fatorUmidadeCA(h, dra);
g0(d <= 3.5) = 1080 ./(500 .* d(d <= 3.5)) .* log(0.46 .* d(d <= 3.5) + 1);
g0 = 3400 ./ (500 .* d + 4000);
m2 = 1.25 .* g0 .* (g0 - 0.2);
kafl = dra.^m2 .* hc.^m2;
end

