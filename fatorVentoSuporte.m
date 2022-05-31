function gt = fatorVentoSuporte(rug, h)
  %% Fator combinado de vento aplicado a suportes e cadeias
  % Tabela 9
  if h < 10
    h = 10;
  end
    switch rug
    case {'A'}
      gt = -0.0002*h^2 + 0.0232 * h + 1.4661;
    case {'B'}
      gt = -0.0002*h^2 + 0.0274 * h + 1.6820;
    case {'C'}
      gt = -0.0002*h^2 + 0.0298 * h + 2.2744;
    case {'D'}
      gt = -0.0002*h^2 + 0.0384 * h + 2.9284;
    otherwise
      error("Classe de rugosidade invalida");
  end
end