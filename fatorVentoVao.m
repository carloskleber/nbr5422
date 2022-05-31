function gl = fatorVentoVao(L)
  %% Fator combinado de vento aplicado a cabos
  % Figura 5
  if L < 200
    gl = 1.0;
  else
    gl = 4e-10*L^3 - 5e-7*L^2 - 1e-4*L + 1.043;
  end
end
