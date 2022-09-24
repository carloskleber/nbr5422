function k = kIntNovo(i, regiao)
  %% fator de tormentas corrigido pelo tempo de integracao - rotina proposta
  % i - tempo de integracao da media em segundos
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
  k = 1 + (K3s - 1) * log(i/600)/log(1/200);
end

