function Ktur = fatTurb(regiao)
    %% Fator de turbulencia
  % Tabela 3
  switch regiao
    case {'S'}
      Ktur = 1.08;
    case {'SE', 'CO'}
      Ktur = 1.12;
    case {'N', 'NE'}
      Ktur = 1.16;
    otherwise
      error("Regiao invalida");
  end
end