function K3s = fatK3s(regiao)
    %% Fator de tormentas para ventos de 3 s
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

