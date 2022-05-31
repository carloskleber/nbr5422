function D = distVegetacao(Vef)
%DISTVEGETACAO Distancia cabo vegetacao (baixo risco de incendio)
% Vef - tensao de linha em kV
if (Vef < 87)
  D = 4;
else
  D = 4 + 0.01*(1.1 * Vef/sqrt(3) - 50);
end
end

