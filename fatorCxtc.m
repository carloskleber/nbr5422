function cxtc = fatorCxtc(Re)
  %% Fator combinado de vento aplicado a cabos
  % Figura X?
  if Re < 3e5
    cxtc = 1.2
  elseif Re > 4.5e5
    cxtc = 0.75
  else
    cxtc = -1.1098 * log(Re) + 15.197
  end
end

