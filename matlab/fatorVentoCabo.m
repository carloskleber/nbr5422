function gc = fatorVentoCabo(rug, h)
  %% Fator combinado de vento aplicado a cabos
  % Tabela 8
  if h < 10
    h = 10;
  end
    switch rug
    case {'A'}
      gc = 0.2914*log(h) + 1.0468;
    case {'B'}
      gc = 0.3733*log(h) + 0.9762;
    case {'C'}
      gc = 0.4936*log(h) + 0.9214;
    case {'D'}
      gc = 0.6153*log(h) + 0.8144;
    otherwise
      error("Classe de rugosidade invalida");
  end
end