function cxtc = fatorCxtc(d, Vp)
  %% Fator combinado de vento aplicado a cabos
  % Figura 15

  % Viscosidade cinematica do ar
  nu = 1.45e-5;

  % 8.8.3.2. Numero de Reynolds
  Re = d * Vp / nu;

  % 8.8.3.2.2
  if Re < 3e5
    cxtc = 1.2
  elseif Re > 4.5e5
    cxtc = 0.75
  else
    cxtc = -1.1098 * log(Re) + 15.197
  end
end

