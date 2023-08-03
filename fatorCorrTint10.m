function kint = fatorCorrTint10(rug)
% Fator de correção pelo período de integração 10 minutos
% Seção 4.9.4.3
  switch rug
    case {'A'}
      Kint = 1.31;
    case {'B'}
      Krug = 1.41;
    case {'C'}
      Krug = 1.58;
    case {'D'}
      Krug = 1.88;
    otherwise
      error("Classe de rugosidade invalida");
  end
end