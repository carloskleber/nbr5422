function gl = fatorVentoVao(L)
  %% Fator de vento para correção do comprimento do vão
  % 8.5.2.5, Figura 12
  if L < 200
    gl = 1.0;
  else
    gl = 4e-10*L^3 - 5e-7*L^2 - 1e-4*L + 1.0403;
  end
end
