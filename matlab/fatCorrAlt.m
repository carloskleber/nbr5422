function Kalt = fatCorrAlt(rug, alt)
  %% Fator de correcao da altura
  % Tabela 2
  switch rug
    case {'A'}
      alfa = 0.110;
    case {'B'}
      alfa = 0.160;
    case {'C'}
      alfa = 0.220;
    case {'D'}
      alfa = 0.280;
    otherwise
      error("Classe de rugosidade invalida");
  end
  Kalt = (alt/10)^alfa;
end

