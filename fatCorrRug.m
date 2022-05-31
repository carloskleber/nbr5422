function Krug = fatCorrRug(rug)
  %% Fator de correcao de rugosidade
  % Tabela 1
  switch rug
    case {'A'}
      Krug = 1.08;
    case {'B'}
      Krug = 1.;
    case {'C'}
      Krug = 0.85;
    case {'D'}
      Krug = 0.67;
    otherwise
      error("Classe de rugosidade invalida");
  end
end