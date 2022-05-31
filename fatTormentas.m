function K3s = fatTormentas(regiao)
    %% Fator de tormentas
  % Tabela 4
  switch regiao
    case {'S'}
      K3s = 1.48;
    case {'SE', 'CO'}
      K3s = 1.61;
    case {'N', 'NE'}
      K3s = 1.72;
    otherwise
      error("Regiao invalida");
  end
end

